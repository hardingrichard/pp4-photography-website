from django.urls import path, include

# Include all URL patterns to project
urlpatterns = [
    path('admin/', admin.site.urls),
    # Community photosharing app
    path('', include('community.urls')),
]
