from django.shortcuts import render, get_object_or_404
from dog_shelters_app.models import Shelter, Dog
from . import models
from django.views import generic

# Create your views here.
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

