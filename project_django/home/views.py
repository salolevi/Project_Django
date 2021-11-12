from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Usuario, Analist, Planta, Incident


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        incidentes = Incident.objects.all()

        context['incidentes'] = incidentes

        return context

class CreateTicketView(TemplateView):
    template_name = 'create-ticket.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarios = Usuario.objects.all()
        analistas = Analist.objects.all()
        plantas = Planta.objects.all()
        context['usuarios'] = usuarios
        context['analistas'] = analistas
        context['plantas'] = plantas

        return context
