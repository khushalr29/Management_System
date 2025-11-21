from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone 
from django.shortcuts import get_object_or_404
from rest_framework import status
from shared.shared.models.brand_and_model_service.brand import Brand
from ..serializers.brandSerializer import BrandSerializer

class BrandAPIView(APIView):
    def get(self , request , id=None):
        if id:
            bd = Brand.objects.filter(id=id , deleted_at__isnull=True)
            serializer = BrandSerializer(bd)
            return Response(serializer.data , status=status.HTTP_200_OK)
        user= request.user
        brand = Brand.objects.filter(deleted_at__isnull =True)
        serializer = BrandSerializer(brand , many= True)
        return Response(serializer.data , status= status.HTTP_200_OK)
    
    def post(self , request):
        serializer = BrandSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save(created_at = timezone.now())
            return Response(status=status.HTTP_201_CREATED)
                
    def patch(self , request , id):
        brand = get_object_or_404(Brand ,id = id , deleted_at__isnull= True)
        serializer = BrandSerializer(brand ,data=request.data ,partial = True)
        if serializer.is_valid():
            serializer.save(updated_at = timezone.now())
            return Response(serializer.data , status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request ,id):
        if id :
            brand = get_object_or_404(Brand , id=id , deleted_at__isnull= True)
            serializer = BrandSerializer(brand , data = request.data)
            if serializer.is_valid():
                serializer.save(updated_at = timezone.now())
                return Response(serializer.data , status =status.HTTP_202_ACCEPTED)
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self ,request , id=None):
        if id:
            brand =get_object_or_404(Brand , id=id ,deleted_at__isnull = True)
            brand.save(deleted_at = timezone.now())
            return Response({'message':f'{id } of Brand is Deleted Successfully .'},status=status.HTTP_200_OK)    
        ids = request.data.get('ids',[])
        if not ids or not isinstance(ids,list):
            return Response({"error": "ids must be a non-empty list."},status=status.HTTP_400_BAD_REQUEST)
        instance =Brand.objects.filter(id__in=ids)
        if not instance.exists():
            return Response({'error':"NO valid Ids Found!"} , status=status.HTTP_400_BAD_REQUEST)
        instance.update(deleted_at = timezone.now())
        return Response({'message':'IDS deleted successfully .' , 'deleted_ids':ids}, status=status.HTTP_200_OK)
           
