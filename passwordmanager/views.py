from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import PasswordManager



class PasswordManagerCreateView(LoginRequiredMixin, CreateView):
    model = PasswordManager
    template_name = 'passwordmanager/password_add.html'
    fields = '__all__'
    login_url = 'login'


class PasswordManagerListView(LoginRequiredMixin, ListView):
    model = PasswordManager
    template_name = 'passwordmanager/password_list.html'
    login_url = 'login'


class PasswordManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = PasswordManager
    template_name = 'passwordmanager/password_update.html'
    fields = '__all__'
    login_url = 'login'


class PasswordManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = PasswordManager
    template_name = 'passwordmanager/password_delete.html'
    success_url = reverse_lazy('password_manager_list')
    login_url = 'login'


class PasswordManagerDetailView(LoginRequiredMixin, DetailView):
    model = PasswordManager
    template_name = 'passwordmanager/password_detail.html'
    login_url = 'login'


def password_manager_logout(request):
    logout(request)
    return redirect('login')