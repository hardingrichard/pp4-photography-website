from django.urls import path
from django.contrib.auth.views import LogoutView  # Default view
from .views import SignUpView, UserLoginView  # Custom views

app_name = 'user'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]
