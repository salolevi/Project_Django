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

class UsuariosView(View):
    template_name = 'usuarios.html'

    def get(self, *args, **kwargs):
        context = {}
        users = Usuario.objects.all()
        context['usuarios'] = users
        return render(self.request, self.template_name, context)

class CrearUsuario(View):
    template_name = 'create-user.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)

    def post(self, *args, **kwargs):
        new_user = Usuario()
        new_user.name = self.request.POST.get('user_name', None)
        new_user.lastn = self.request.POST.get('user_lastn', None)
        new_user.sector = self.request.POST.get('user_sector', None)
        new_user.costCenter = self.request.POST.get('user_costc', None)

        new_user.save()

        return redirect('usuarios')

class AnalistasView(View):

    template_name = 'analistas.html'

    def get(self, *args, **kwargs):
        context = {}
        analistas = Analist.objects.all()
        context['analistas'] = analistas
        return render(self.request, self.template_name, context)

class CrearAnalista(View):

    template_name = 'create-analist.html'

    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
    
    def post(self, *args, **kwargs):

        new_analist = Analist()
        new_analist.name = self.request.POST.get('analist_name', None)
        new_analist.lastn = self.request.POST.get('analist_lastn', None)
        new_analist.save()

        return redirect('analistas')
    
class PlantasView(View):
    
    template_name = 'plantas.html'
    
    def get(self, *args, **kwargs):
        context = {}
        plantas = Planta.objects.all()
        context['plantas'] = plantas
        return render(self.request, self.template_name, context)

class CrearPlanta(View):
    
    template_name = 'create-plant.html'
    
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
    
    def post(self, *args, **kwargs):
        new_plant = Planta()
        new_plant.plantaName = self.request.POST.get('plant_name', None)
        new_plant.plantaLocation = self.request.POST.get('plant_location', None)
        new_plant.save()
        
        return redirect('plantas')
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
