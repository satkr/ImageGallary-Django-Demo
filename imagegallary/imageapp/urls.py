from django.urls import path
from imageapp.views import index # show, edit, update, delete


urlpatterns = [
    path('', index, name='index'),
]