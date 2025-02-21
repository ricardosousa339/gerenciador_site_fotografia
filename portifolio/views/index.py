from core.views.base import BaseTemplateView


# Views Inicial Portifolio
class PortifolioIndexTemplateView(BaseTemplateView):
    # Views para renderizar a tela inicial Portifolio
    template_name = "portifolio/index.html"
    context_object_name = "portifolio"

    def get_context_data(self, **kwargs):
        context = super(PortifolioIndexTemplateView, self).get_context_data(**kwargs)
        return context
