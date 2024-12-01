

# Create your views here.
from django.urls import path
from . import views
from .views import PaginaInicial
urlpatterns=[
    path('teste/', PaginaInicial.as_view(), name='teste'),
]