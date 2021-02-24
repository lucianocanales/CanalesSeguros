from django.urls import path
from . import views


urlpatterns = [
    path(
        '',
        views.BienesListView.as_view(),
        name='bienes'
    ),

]
