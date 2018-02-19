from django.views.generic import TemplateView, CreateView
from .forms import UserCreateForm
from django.urls import reverse_lazy
# Create your views here.


class SignUpView(CreateView):
    template_name = 'accounts/signup.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('accounts:login')


class ThanksView(TemplateView):
    template_name = 'accounts/thanks.html'
