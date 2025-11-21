from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from ..serializers.varientsSerializer import VarientsSerializer
from shared.shared.models.brand_and_model_Service.varients import Varients
from django.utils import timezone
from django.shortcuts import get_object_or_404

class VarientsAPIView(APIView):
    def get(self , request ,id=None):
        if id:
            data = get_object_or_404(Varients , id = id , deleted_at__isnull = True)
            serializer= VarientsSerializer(data)
            return Response(serializer.data , status= status.HTTP_200_OK)
        user= request.data
        data = Varients.objects.filter(deleted_at__isnull = True)
        serializer = VarientsSerializer(data, many = True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self , request):
        serializer = VarientsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_at= timezone.now())
            return Response(serializer.data , {'message':'varient is created Successfully .'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def put(self , request  , id):
        varient = get_object_or_404(Varients , id = id,  deleted_at__isnull = True)
        serializer = VarientsSerializer(varient , data =request.data)
        if serializer.is_valid():
            serializer.save(updated_at = timezone.now())
            return Response(serializer.data, {'message':'Update data Successfully .'} , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self , request , id):
        varient = get_object_or_404(Varients , id = id,  deleted_at__isnull = True)
        serializer = VarientsSerializer(varient , data =request.data ,partial = True)
        if serializer.is_valid():
            serializer.save(updated_at = timezone.now())
            return Response(serializer.data, {'message':'Update data Successfully .'} , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self , request, id = None):
        if id :
            varient = get_object_or_404(Varients , id=id , deleted_at__isnull= True)
            varient.save(deleted_at =timezone.now())
            return Response(varient.data ,{'message':'id deleted successfully .'} , status=status.HTTP_200_OK)
        ids = request.data.get('ids' , [])
        if not ids or not isinstance(ids , list):
            return Response({"error": "ids must be a non-empty list."},status=status.HTTP_400_BAD_REQUEST)
        instance = Varients.objects.filter(id__in = ids)
        if not instance.exists():
            return Response({'error':"NO valid Ids Found!"} , status=status.HTTP_400_BAD_REQUEST)
        instance.update(deleted_at=timezone.now())
        return Response({'message':'ids deleted Successfully.'} ,status=status.HTTP_200_OK )
