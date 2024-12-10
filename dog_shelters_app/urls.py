from django.urls import path
from . import views

urlpatterns = [
    path('', views.shelters_list, name='shelters_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),

    path('dogs', views.DogsListView.as_view(), name='dogs_list'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),
]

