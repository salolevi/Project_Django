from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from .models import Usuario, Analist, Planta, Incident


# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        incidentes = Incident.objects.all()

        context['incidentes'] = incidentes

        return context

class CreateTicketView(View):
    template_name = 'create-ticket.html'

    def get(self, *args, **kwargs):
        context = {}
        usuarios = Usuario.objects.all()
        analistas = Analist.objects.all()
        plantas = Planta.objects.all()
        context['usuarios'] = usuarios
        context['analistas'] = analistas
        context['plantas'] = plantas

        return render(self.request, self.template_name, context)

    def post(self, *args, **kwargs):
        new_incident = Incident()
        new_incident.desc = self.request.POST.get('desc', None)
        new_incident.usuario = Usuario.objects.filter(id=self.request.POST.get('user', None))[0]
        new_incident.analista = Analist.objects.filter(id = self.request.POST.get('analist', None))[0]
        new_incident.planta = Planta.objects.filter(id = self.request.POST.get('planta', None))[0]
        new_incident.save()

        return redirect('main_index')


# class CreateTicket(View):
#
#     template_name = 'create-ticket.html'
#
#     def post(self, *args, **kwargs):
#         new_incident = Incident()
#         new_incident.desc = self.request.POST.get('desc', None)
#         new_incident.usuario = Usuario.objects.filter(id=self.request.POST.get('user', None))
#         new_incident.analista = Analist.objects.filter(id = self.request.POST.get('analist', None))
#         new_incident.planta = Planta.objects.filter(id = self.request.POST.get('planta', None))
#         new_incident.save()
