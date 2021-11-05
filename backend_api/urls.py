from django.urls import path, include

from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),

]
