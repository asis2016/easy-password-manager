from django.contrib import admin
from django.urls import path, include

from passwordmanager.views import (
    PasswordManagerListView, 
    PasswordManagerCreateView, 
    PasswordManagerDetailView, 
    PasswordManagerUpdateView, 
    PasswordManagerDeleteView, password_manager_logout
)

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', password_manager_logout, name='pm_logout'),
    path('admin/', admin.site.urls),
    path('<int:pk>/', PasswordManagerDetailView.as_view(), name='password_manager_detail'),
    path('<int:pk>/edit/', PasswordManagerUpdateView.as_view(), name='password_manager_update'),
    path('<int:pk>/delete/', PasswordManagerDeleteView.as_view(), name='password_manager_delete'),
    path('create', PasswordManagerCreateView.as_view(), name='password_manager_add'),
    path('', PasswordManagerListView.as_view(), name='password_manager_list'),
]
