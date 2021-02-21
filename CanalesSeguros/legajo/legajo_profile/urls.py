from django.urls import path
from . import views


urlpatterns = [
    path(
        'UpdateProfile/',
        views.UpdateProfileView.as_view(),
        name='updateProfile'
    ),

]
