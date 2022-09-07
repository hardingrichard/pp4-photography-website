from django.views.generic import CreateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


# Allows the user to register and create a new login
class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('image:list')

    # Log the user in before redirecting
    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        login(self.request, user)
        return to_return


# Custom template for the login page
class UserLoginView(LoginView):
    template_name = 'users/login.html'
