from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.dashboard, name='dashboard'),
    path('add/', views.entry_create, name='entry_create'),
    path('delete/<int:pk>/', views.entry_delete, name='entry_delete'),
]