from core.views.base import BaseTemplateView
from portifolio.models import DadosPrincipais, SecaoContato, SecaoSobre


# Views Inicial Portifolio
class PortifolioIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Portifolio
    template_name = "portifolio/index.html"
    context_object_name = "portifolio"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['dadosprincipais'] = DadosPrincipais.objects.filter(deleted=False).first()
        context['secaosobre'] = SecaoSobre.objects.filter(deleted=False).first()
        context['secaocontato'] = SecaoContato.objects.filter(deleted=False).first()
