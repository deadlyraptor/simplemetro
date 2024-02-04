from django.views.generic import TemplateView

from .api import Metro

trains = Metro()
class IndexView(TemplateView):
    template_name = 'core/index.html'
    extra_context = {'title': 'Simple Metro'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lines'] = trains.get_lines().data
        return context
    
class StationListView(TemplateView):
    template_name = 'core/station_list.html'
    extra_content = {'title': 'Stations'}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stations'] = trains.get_stations(self.kwargs['line_code']).data
        return context