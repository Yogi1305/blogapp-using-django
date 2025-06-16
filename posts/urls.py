# copy from blogs urls

from django.urls import path
from . import views

# format for path is first is routes ,second is views.py(that is function or logic) and last one name
urlpatterns = [
    path('', views.index,name='index'),
]