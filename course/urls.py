from django.urls import path,include
from . views import all

urlpatterns = [
    path('all' , all)
]
