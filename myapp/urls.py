from . import views
from django.urls import path

from .views import *
urlpatterns = [
    # path('products/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    # path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
    path('', views.product_list_create_view, name='product-list-create'),
    path('products/<int:pk>/', views.product_detail_view, name='product-detail'),
    path('products/<int:pk>/update/', views.product_update_view, name='product-update'),
    path('products/<int:pk>/delete/', views.product_delete_view, name='product-delete'),

]