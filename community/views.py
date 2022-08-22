from django.shortcuts import render
from .models import Photoshare

def index(request):
    # Import Photoshare and save to database
    photo = Photoshare.objects.all()
    # Add context
    ctx = {'photo':photo}
    return render(request, 'index.html', ctx)