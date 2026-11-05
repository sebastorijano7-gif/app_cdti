from django.urls import path
from . import views

urlpatterns = [
    path('cdti/equipos/', views.lista_equipos, name='lista_equipos'),
    path('cdti/prestar/', views.prestar_equipo, name='prestar_equipo'),
    path('cdti/equipo/<int:id>/', views.detalle_equipo, name='detalle_equipo'),
]