from django.urls import path 
from .views.carViews import CarDetailView , CarListView

urlpatterns = [
  path("cars" ,CarListView.as_view(), name ="cars-list-create"),
  path("cars/<int:id>" , CarDetailView.as_view() , name ="cars-detail")
]  
    