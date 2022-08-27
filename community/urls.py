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

# Include all URL patterns to project
urlpatterns = [
    path('admin/', admin.site.urls),
    # Community photosharing app
    path('', include('community.urls')),
    path('', views.index, name='index'),
]
