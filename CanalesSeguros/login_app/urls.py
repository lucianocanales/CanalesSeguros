from django.urls import path
from login_app import views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
