from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from django.shortcuts import get_object_or_404
from shared.shared.models.brand_and_model_Service.carname import CarName
from ..serializers.carnameSerializer import CarNameSerializer
from rest_framework import status

class CarNameAPIView(APIView):
    def get(self , request , id=None):
        if id:
            car = get_object_or_404(CarName , id =id , deleted_at__isnull = True)
            serializer = CarNameSerializer(car)
            return Response({'message':f'Get {id} CarName Data Successfully .'} , serializer.data , status=status.HTTP_200_OK)
        user = request.user
        cars = CarName.objects.filter(deleted_at__isnull = True)
        serializer = CarNameSerializer(cars , many = True)
        return Response(serializer.data , {'message':'Get all data Successfully .'} , status=status.HTTP_200_OK)
    
    def post (self , request):
        serializer = CarNameSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save(created_at= timezone.now())
            return Response(serializer.data , {'message':'Car Data Created Successfully .'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request , id=None):
        if id:
            car = get_object_or_404(CarName , id=id , deleted_at__isnull= True)
            car.save(deleted_at =timezone.now())
            return Response(car.data ,{'message':'id deleted successfully .'} , status=status.HTTP_200_OK)
        ids = request.data.get('ids',[])
        if not ids or not isinstance(ids , list):
            return Response({"error": "ids must be a non-empty list."},status=status.HTTP_400_BAD_REQUEST)
        instance =CarName.objects.filter(id__in=ids)
        if not instance.exists():
            return Response({'error':"NO valid Ids Found!"} , status=status.HTTP_400_BAD_REQUEST)
        instance.update(deleted_at = timezone.now())
        return Response({'message':'IDS deleted Successfully . '},status=status.HTTP_200_OK)
    
    def put(self , request , id):
        if id :
            car = get_object_or_404(id=id)
            serializer = CarNameSerializer(car , data = request.data)
            if serializer.is_valid():
                serializer.save(updated_at = timezone.now())
                return Response(serializer.data , {'message':'updated data'} , status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def patch(self ,request ,id):
        if id:
            car = get_object_or_404(id=id)
            serializer = CarNameSerializer(car , data = request.data , partial = True)
            if serializer.is_valid():
                serializer.save(updated_at = timezone.now())
                return Response(serializer.data , {'message':'updated data'} , status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



