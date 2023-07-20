# users/urls.py
from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('create-account/', views.CreateAccountView.as_view(), name='createAccount'),
    path('account/', views.account_page, name='account')
]