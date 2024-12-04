from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logins/', auth_views.LoginView.as_view(
        template_name='cadastro/login.html'
    ), name='login'),
    
    path('cadastro/', views.cadastro, name='cadastro'),
]