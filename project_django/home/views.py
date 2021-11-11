from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Usuario, Analist, Planta, Incident


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        analists = Analist.objects.all()

        context['analists'] = analists

        return context

class CreateTicketView(TemplateView):
    template_name = 'create-ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
