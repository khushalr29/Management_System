from django.urls import path , include
from .views.brandView import BrandAPIView
from .views.carnameView import CarNameAPIView
from .views.varientView import VarientsAPIView

urlpatterns = [
    path('brands',BrandAPIView.as_view() , name='Create-delete-list'),
    path('brands/<int:id>' , BrandAPIView.as_view() , name='id-CRUD'),
    path('car-name' ,CarNameAPIView.as_view() , name='Create-delete-list'),
    path('car-name/<int:id>',CarNameAPIView.as_view() , name = 'id-CRUD'),
    path('varients' , VarientsAPIView.as_view() , name = 'create-delete-list'),
    path('varients/<int:id>',VarientsAPIView.as_view() , name = 'id - CRUD'),
]

