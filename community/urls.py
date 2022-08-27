from django.urls import path, include
from django.contrib import admin
from Photoshare import views

# Import views and functions from views.py
from .views import (
    PhotoshareListView,
    PhotoshareTagListView,
    PhotoshareDeleteView, 
    PhotoshareDetailView,
    PhotoshareCreateView,
    PhotoshareUpdateView
)

# Declares namespace of the app
app_name = 'image'

# Receives arguments of the route, view and name used in the namespace
urlpatterns = [ 
    path('', PhotoshareListView.as_view(), name = 'list'),
    path('image/<int:pk>/', PhotoshareDetailView.as_view(), name = 'detail'),
    path('tag/<slug:tag>/', PhotoshareTagListView.as_view(), name = 'tag'),
    path('image/create/', PhotoshareCreateView.as_view(), name = 'create'),
    path('image/<int:pk>/update/' PhotoshareUpdateView.as_view(), name = 'update'),
    path('image/<int:pk>/delete/' PhotoshareDeleteView.as_view(), name = 'delete'),
]