from django.contrib.auth.forms import UserCreationForm
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy
from django.views.generic import CreateView


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'registration/register.html'
  success_url = reverse_lazy('login')
  form_class = UserCreationForm
  success_message = "Your profile was created successfully"