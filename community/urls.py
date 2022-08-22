from django.urls import path, include
from django.contrib import admin
from Photoshare import views

# Include all URL patterns to project
urlpatterns = [
    path('admin/', admin.site.urls),
    # Community photosharing app
    path('', include('community.urls')),
    path('', views.index, name='index'),
]
