from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'core/index.html'
    extra_context = {'title': 'Simple Metro'}