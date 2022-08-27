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

