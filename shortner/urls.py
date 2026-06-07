from django.urls import path
from .views import dashboard_view, create_url_view, edit_url_view, delete_url_view, redirect_view

urlpatterns = [
    path('dashboard/', dashboard_view, name='dashboard'),
    path('create/', create_url_view, name='create_url'),
    path('edit/<uuid:pk>/', edit_url_view, name='edit_url'),
    path('delete/<uuid:pk>/', delete_url_view, name='delete_url'),
    path('redirect/<str:short_key>/', redirect_view, name='redirect'),
]