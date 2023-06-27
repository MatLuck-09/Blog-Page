from django.urls import path
from . import views

urlpatterns = [

    path('', views.battles, name="Batallas" ),
    
]