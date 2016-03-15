from django.shortcuts import render
from .models import Thing

def index(request):
    things = Thing.objects.all().order_by('name')
    return render(request, 'index.html', {'things':things,})
