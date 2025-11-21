from django.utils import timezone
from rest_framework.views import APIView
from ..car import Car
from ..serializers.carSerializer import CarSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 

class CarListView(APIView):
    def get(self , request):
        user= request.user
        cars = Car.objects.filter(deleted_at__isnull=True)
        serializer = CarSerializer(cars , many=True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    
    def post(self , request):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_at = timezone.now())
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

class CarDetailView(APIView):

    def delete(self, request ,id):
        car = get_object_or_404(Car ,id=id)
        car.deleted_at=timezone.now()
        car.save(update_fields=['deleted_at'])
        return Response({"Car is  Deleted Successfully ."} ,status=status.HTTP_204_NO_CONTENT)
    
    def get(self , request, id):
        car = get_object_or_404( Car,id=id , deleted_at__isnull=True)
        serializer = CarSerializer(car)
        if car:
            return Response(serializer.data , status=status.HTTP_200_OK)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request ,id):
        car = get_object_or_404(Car,id=id , deleted_at__isnull =True)
        serializer = CarSerializer(car, data = request.data)
        if serializer.is_valid():
            serializer.save(updated_at=timezone.now())
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_404_NOT_FOUND)


