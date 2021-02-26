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
    path(
        'update_bici/<int:pk>/',
        views.BicicletaUpdateView.as_view(),
        name='update_bicicleta'
    ),
    path(
        'delete_bici/<int:pk>/',
        views.BicicletaDeleteView.as_view(),
        name='delete_bici'
    ),
    path(
        'crear_accesorio/<int:pk>/',
        views.AccesorioCreateView.as_view(),
        name='crear_accesorio'
    ),
]
