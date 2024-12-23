from django.urls import path
from . import views
from .views import DogListView, ShelterListView
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('', views.index, name='index'),
    path('shelters', views.shelters_list, name='shelters_list'),
    path('shelter/<int:pk>', views.shelter_detail, name='shelter_detail'),

    path('dogs', views.DogsListView.as_view(), name='dogs_list'),

    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog_detail'),

    path('dog/register', views.DogCreateView.as_view(), name='dog_register'),
    path('dog/update/<int:pk>/', views.DogUpdateView.as_view(), name='dog_update'),
    path('dog/delete/<int:pk>/', views.DogDeleteView.as_view(), name='dog_delete'),

    # api
    path('api/dogs/', DogListView.as_view(), name='dog_list'),
    path('api/shelters/', ShelterListView.as_view(), name='shelters_list'),


]


