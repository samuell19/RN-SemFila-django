

# Create your views here.
from django.urls import path
from . import views
from .views import PaginaInicial
urlpatterns=[
    path('lista/', PaginaInicial.as_view(), name='lista'),
    path('cadastros/', views.CadastrosView.as_view(), name='cadastros'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('esqueceu-senha/', views.EsqueceuView.as_view(), name='esqueceu'),
    path('esqueceu-senha2/', views.Esqueceu2View.as_view(), name='esqueceu2'), #isso vai mudar
]