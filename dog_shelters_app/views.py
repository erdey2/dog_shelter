from django.shortcuts import render, get_object_or_404
from dog_shelters_app.models import Shelter

# Create your views here.
def shelter_list(request):
    shelters = Shelter.objects.all()
    context = {'shelters': shelters}
    return render(request, 'shelter_list.html', context)

def shelter_detail(request, pk):
    shelter = get_object_or_404(Shelter, pk=pk)
    context = {'shelter': shelter}
    return render(request, 'shelter_detail.html', context)

