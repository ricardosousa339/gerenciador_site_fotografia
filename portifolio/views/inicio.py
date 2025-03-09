from django.views.generic import TemplateView
from portifolio.models import DadosPrincipais, ImagemHeader, SecaoContato, SecaoSobre  # adjust import if necessary

class InicioView(TemplateView):
    template_name = "portifolio/inicio/inicio.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dadosprincipais'] = DadosPrincipais.objects.filter(deleted=False).first()
        context['secaosobre'] = SecaoSobre.objects.filter(deleted=False).first()
        context['secaocontato'] = SecaoContato.objects.filter(deleted=False).first()
        
        return context