from django.shortcuts import get_object_or_404 # Raise a 404 exception
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # CRUD functionality
from django.core.exceptions import PermissionDenied # Raise a 403 exception
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Force permissions for view access
from django.urls import reverse_lazy # redirect users
from .models import Photoshare # Retrieve and update database



# from django.shortcuts import render

# def index(request):
#     # Import Photoshare and save to database
#     photo = Photoshare.objects.all()
#     # Add context
#     ctx = {'photo':photo}
#     return render(request, 'index.html', ctx)