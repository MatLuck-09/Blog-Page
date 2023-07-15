from django.urls import path
from . import views

urlpatterns = [

    path('', views.blog, name="Blog" ),

    path('recomendaciones/', views.recomendacion_view, name='recomendaciones'),

    path('recomendacion/<int:recomendacion_id>/editar/', views.editar, name='EditarRecomendacion')

]