
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.urls import reverse_lazy

from core.models import User
from .forms import UpdateProfile

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
        print(self.get_redirect_field_name())
        if not request.user.is_authenticated:
            return redirect('login')
        else:
            return super().dispatch(request, *args, **kwargs)
