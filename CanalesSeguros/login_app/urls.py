from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    # olvide password
    path(
        'forgot_passwoed/',
        views.ForgotPassword.as_view(),
        name='forgot_passwoed',
    ),
    path(
        'forgot_passwoed/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/clave_reset_done.html',
            extra_context={'title': 'Se ha enviado un email de recuperación'}
        ),
        name='forgot_passwoed_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        views.RecoverPassword.as_view(),
        name='forgot_passwoed_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='registration/clave_reset_complete.html',
            extra_context={'title': 'Contraseña restablecida con éxito'}
        ),
        name='password_reset',
    ),

]
