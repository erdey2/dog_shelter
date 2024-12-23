from django.shortcuts import render, get_object_or_404
from dog_shelters_app.models import Shelter, Dog
from . import models
from django.views import generic
from django.urls import reverse_lazy
from rest_framework import generics
from .serializers import DogSerializer, ShelterSerializer


# Create your views here.
def login(request):
    return render(request, template_name='login.html')

def index(request):
    return render(request, 'index.html')

def shelters_list(request):
    shelters = Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelters_list.html', context)

def shelter_detail(request, pk):
    # shelter = get_object_or_404(Shelter, pk=pk)
    shelter = Shelter.objects.get(pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

class DogDetailView(generic.DetailView):
    model = models.Dog
    template_name = 'dog_detail.html'
    context_object_name = 'dog'

class DogsListView(generic.ListView):
    template_name = 'dogs_list.html'
    context_object_name = 'dogs'

    def get_queryset(self):
        return Dog.objects.all()

class DogCreateView(generic.CreateView):
    model = Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

class DogUpdateView(generic.UpdateView):
    model = Dog
    template_name = 'dog_form.html'
    fields = ['name', 'description', 'shelter']

class DogDeleteView(generic.DeleteView):
    model = Dog
    success_url = reverse_lazy('dogs_list')

# api
class DogListView(generics.ListCreateAPIView):
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class ShelterListView(generics.ListCreateAPIView):
    queryset = Shelter.objects.all()
    serializer_class = ShelterSerializer






