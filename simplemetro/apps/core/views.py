from django.views.generic import TemplateView

from .utils import RestAdapter
class IndexView(TemplateView):
    template_name = 'core/index.html'
    extra_context = {'title': 'Simple Metro'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        trains = RestAdapter()
        context['lines'] = trains.get('jLines')
        return context