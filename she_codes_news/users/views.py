from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .forms import CustomUserCreationForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from news.models import NewsStory



class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('news:index')
        return super(CreateAccountView, self).dispatch(request, *args, **kwargs)

@login_required
def account_page(request):
    context = {
        'user': request.user,
    }
    return render(request, 'users/account.html', context)

