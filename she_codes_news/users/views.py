from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

@login_required
def account_page(request):
    context = {
        'user': request.user,
    }
    return render(request, 'users/account.html', context)