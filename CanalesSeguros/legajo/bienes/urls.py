from django.urls import path
from . import views


urlpatterns = [
    path(
        'bienes/',
        views.BienesListView.as_view(),
        name='bienes'
    ),

]
