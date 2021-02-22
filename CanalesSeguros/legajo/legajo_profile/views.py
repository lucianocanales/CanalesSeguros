from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import request
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from core.models import User
from .forms import UpdateProfile
from localflavor.ar.ar_provinces import PROVINCE_CHOICES

# Create your views here.


class UpdateProfileView(UserPassesTestMixin, UpdateView):
    model = User
    form_class = UpdateProfile
    template_name = 'UpdateProfile.html'
    success_url = reverse_lazy('home')
    permission_denied_message = 'Usuario Incorrecto'
    raise_exception = True

    def test_func(self):

        chek = self.request.user.id
        if self.kwargs['pk'] == chek:
            return True
        else:
            return False

    def dispatch(self, request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for provinca in PROVINCE_CHOICES:
            if User.objects.get(id=self.kwargs['pk']).provincia == provinca[0]:
                context['provincia_completo'] = provinca[1]

        context['title'] = 'acutalizar perfil'
        return context
