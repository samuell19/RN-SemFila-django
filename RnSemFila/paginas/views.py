from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name="paginas/lista.html"

class CadastrosView(TemplateView):
    template_name="paginas/cadastros.html"

class LoginView(TemplateView):
    template_name="paginas/login.html"

class EsqueceuView(TemplateView):
    template_name="paginas/esqueceusenha.html"

class Esqueceu2View(TemplateView): #isso vai mudar
    template_name="paginas/esqueceusenha2.html"