from django.urls import path, include

from rest_framework.routers import DefaultRouter
from backend_api import views

router = DefaultRouter()
router.register('products', views.ProductViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls)),

]
from django.urls import path,include
from . import views
from django.contrib.auth import views
from rest_framework.authtoken.views import obtain_auth_token
from .views import (ProductListView,ProductCreateView,ProductUpdateView,ProductDeleteView,UserProductListView,)

urlpatterns = [
    path('',views.first_view,name='track-home'),
    path('all/', ProductListView.as_view(), name='track-list-all-products'),
    path('WhyToUse/', views.why, name='track-why'),
    path('benefits/', views.benefits, name='track-benefits'),
    path('announcements/', views.announce, name='track-announcements'),
    path('product/new/',  ProductCreateView.as_view(), name='product-create'),
    path('about/', views.about,name="track-about"),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('user/<str:username>', UserProductListView.as_view(), name='user-products'),
    path('api/products/', views.ProductList.as_view(),name="all_projects_api"),
    path('api/profiles/',views.ProfileList.as_view(),name="all_profiles_api"),
    path('accounts/', include('registration.backends.simple.urls')),
    path('logout/', views.LogoutView.as_view(), {"next_page": '/'}),
    path('api-token-auth/', obtain_auth_token),

]
