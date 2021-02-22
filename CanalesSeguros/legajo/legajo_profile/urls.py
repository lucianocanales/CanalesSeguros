from django.urls import path
from . import views


urlpatterns = [
    path(
        'UpdateProfile/<int:pk>/',
        views.UpdateProfileView.as_view(),
        name='updateProfile'
    ),

]
