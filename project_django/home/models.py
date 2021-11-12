from django.db import models


# Create your models here.

class Usuario(models.Model):
    name = models.CharField(max_length=50)
    lastn = models.CharField(max_length=50)
    sector = models.CharField(max_length=50)
    costCenter = models.PositiveBigIntegerField()
    def __str__(self):
        user = str(self.id) + ': ' + self.name + ' ' + self.lastn + ', ' + str(self.sector)
        return user


class Analist(models.Model):
    name = models.CharField(max_length=50)
    lastn = models.CharField(max_length=50)
    sector = models.CharField(max_length=50, default='Sistemas')
    def __str__(self):
        ana = str(self.id) + ': ' + self.name + ' ' + self.lastn + ', ' + str(self.sector)
        return ana



class Planta(models.Model):
    plantaName = models.CharField(max_length=50)
    plantaLocation = models.CharField(max_length=50)
    def __str__(self):
        planta = str(self.id) + ': ' + self.plantaName + ', ' + self.plantaLocation
        return planta

class Incident(models.Model):
    analista = models.ForeignKey(Analist, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    planta = models.ForeignKey(Planta, on_delete=models.CASCADE)
    desc = models.CharField(max_length=100, default="Incident description")
    def __str__(self):
        incident = 'ID: ' + str(self.id) + ', Issue: ' + self.desc + ', Affected User: ' + str(self.usuario.id) + ', Assigned Analist: ' + str(self.analista.id)
        return incident

