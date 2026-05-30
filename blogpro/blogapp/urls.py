from django.urls import path
from . import views

app_name = 'blogapp'

urlpatterns = [
    path('category/', views.category_list, name='category_list'),
    path('category/create/', views.category_create, name='category_create'),
    path('category/<int:pk>/', views.category_detail, name='category_detail'),
    path('category/<int:pk>/edit/', views.category_edit, name='category_edit'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),
]