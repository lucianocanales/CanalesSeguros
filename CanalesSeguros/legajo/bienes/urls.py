from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.BienesListView.as_view(),
        name='bienes'
    ),
    path(
        'crear_bici/',
        views.BicicletaCreateView.as_view(),
        name='create_bicicleta'
    ),
]
