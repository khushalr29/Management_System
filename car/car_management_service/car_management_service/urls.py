from django.contrib import admin
from django.urls import path , include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
   path('api/v1/', include([
        path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
        path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
        path('', include('cars.urls')),
    ])),
    path("admin/", admin.site.urls),
    path("swagger/" , TemplateView.as_view(template_name= 'swagger.html',extra_context ={'schema_url' :'openapi-schema'}) , name='swagger'),
]
