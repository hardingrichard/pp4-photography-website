# Raise a 404 exception
from django.shortcuts import get_object_or_404
# CRUD functionality
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
    )
# Raise a 403 exception
from django.core.exceptions import PermissionDenied
# Force permissions for view access
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# redirect users
from django.urls import reverse_lazy
# Retrieve and update database
from .models import Photoshare


# Passes context of all photos uploaded by user and inherit ListView
class PhotoshareListView(ListView):
    model = Photoshare
    template_name = 'community/list.html'
    context_object_name = 'images'


# 3rd party code used and modified to suit needs for ListView
# sitepoint.com/django-photo-sharing-app
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
class PhotoshareCreateView(LoginRequiredMixin, CreateView):
    model = Photoshare
    fields = ['title', 'description', 'image', 'tags']
    template_name = 'community/create.html'
    success_url = reverse_lazy('image:list')

    # Labels user as submitter of the photograph
    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)


# Checks to see if the user trying to amend photo was the original submitter
class UserIsSubmitter(UserPassesTestMixin):
    # Method that returns an image, if the image doesnt exist raise 404 error
    def get_image(self):
        return get_object_or_404(Photoshare, pk=self.kwargs.get('pk'))

    # Return true if logged in user otherwise raise PermissionDenied exception
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_image().submitter
        else:
            raise PermissionDenied(
                'You are not logged in to make changes to the photo'
                )


# Inherits test function from UserIsSubmitter and updates UpdateView
# Allows user to edit information about the image but not the image itself
class PhotoshareUpdateView(UserIsSubmitter, UpdateView):
    model = Photoshare
    fields = ['title', 'description', 'tags']
    template_name = 'community/update.html'
    context_object_name = 'image'
    success_url = reverse_lazy('image:list')


# Inherits test function from UserIsSubmitter and allows user to delete image
class PhotoshareDeleteView(UserIsSubmitter, DeleteView):
    model = Photoshare
    template_name = 'community/delete.html'
    context_object_name = 'image'
    success_url = reverse_lazy('image:list')
