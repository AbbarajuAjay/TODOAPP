from django.urls import path
from . import views

urlpatterns = [
    path('', views.listview, name='list-view'),
    path('update/<str:pk>/', views.updateview, name='update-view'),
    path('delete/<str:pk>/', views.deleteview, name='delete-view'),
]