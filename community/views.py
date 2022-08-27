from django.shortcuts import get_object_or_404 # Raise a 404 exception
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # CRUD functionality
from django.core.exceptions import PermissionDenied # Raise a 403 exception
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin # Force permissions for view access
from django.urls import reverse_lazy # redirect users
from .models import Photoshare # Retrieve and update database

# Passes context of all photos uploaded by user and inherit ListView
class PhotoshareListView(ListView):
    model = Photoshare
    template_name = 'community/list.html'
    context_object_name = 'image'

# 3rd party code for ListView taken from sitepoint.com/django-photo-sharing-app and modified to suit needs
# Inherits attributes from PhotoshareListView and tag slug argument
class PhotoshareTagListView(PhotoshareListView):
    template_name = 'community/taglist.html'

    # Receives the tag slug from response and returns
    def get_tag(self):
        return self.kwargs.get('tag')
    
    # Returns only photo objects tagged with slug
    def get_queryset(self):
        return self.model.objects.filter(tags__slug=self.get_tag())
    
    # Returns tag passed to URL to display in template
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag()
        return context

# Displays unique image data of title, description and tag
class PhotoshareDetailView(DetailView):
    model = Photoshare
    template_name = 'community/detail.html'
    context_object_name = 'image'

# Allows user to share a photo only if logged in otherwise redirect to login. 
# Submits photo information to form and redirects to dashboard if successful.
class Photoshare(LoginRequiredMixin, CreateView):
    model = Photoshare
    fields = ['title', 'description', 'image', 'tags']
    template_name = 'community/create.html'
    success_url = reverse_lazy('image:list')

    # Labels user as submitter of the photograph
    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
