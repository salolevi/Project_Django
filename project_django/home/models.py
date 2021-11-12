from django.db import models


# Create your models here.

class Usuario(models.Model):
    usuario_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastn = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    costCenter = models.PositiveBigIntegerField()
    def __str__(self):
        user = str(self.usuario_id) + ': ' + self.name + ' ' + self.lastn + ', ' + str(self.sector)
        return user


class Analist(models.Model):
    analista_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)
    lastn = models.CharField(max_length=50)
    sector = models.CharField(max_length=50, default='Sistemas')
    def __str__(self):
        ana = str(self.analista_id) + ': ' + self.name + ' ' + self.lastn + ', ' + str(self.sector)
        return ana



class Planta(models.Model):
    planta_id = models.BigAutoField(primary_key=True)
    plantaName = models.CharField(max_length=50)
    plantaLocation = models.CharField(max_length=50)
    def __str__(self):
        planta = str(self.planta_id) + ': ' + self.plantaName + ', ' + self.plantaLocation
        return planta

class Incident(models.Model):
    incident_id = models.BigAutoField(primary_key=True)
    analista_id = models.ForeignKey(Analist, on_delete=models.CASCADE)
    usuario_id = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    planta_id = models.ForeignKey(Planta, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100, default="Incident description")
    def __str__(self):
        incident = 'ID: ' + str(self.incident_id) + ', Issue: ' + self.desc + ', Affected User: ' + Usuario.objects.get(usuario_id = self.usuario_id) + ', Assigned Analist: ' + Analist.objects.get(analist_id = self.analist_id)
        return incident

