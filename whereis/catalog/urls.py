from django.urls import path
from . import views

urlpatterns = [
    path('add', views.create_person_view),
    path('', views.person_list_view, 'home'),
]