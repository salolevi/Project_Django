from django.contrib import admin
from .models import Administrador, Usuario, Analist, Incident, Planta
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Analist)
admin.site.register(Incident)
admin.site.register(Planta)
admin.site.register(Administrador)
