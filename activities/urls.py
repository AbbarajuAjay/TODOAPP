from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (
    PostListView,
    PostUpdateView,
    PostCreateView,
    PostDeleteView,
)

urlpatterns = [
    path('', PostListView.as_view(), name='viewall-view'),
    path('post/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/create/', PostCreateView.as_view(), name='post-create'),
    path('delete/<str:pk>/', PostDeleteView.as_view(), name='delete-view'),
    path('login/', auth_views.LoginView.as_view(template_name='activities/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='activities/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
]