from django.db import models

# Create your models here.
class Giornalista(models.Model):

    nome = models.CharField(max_length=28)
    cognome = models.CharField(max_length=28)

    def __str__(self):
        return self.nome + " "+ self.cognome

class Articolo(models.Model):

    titolo = models.CharField(max_length=100)
    contenuto = models.CharField()
    giornalista = models.ForeignKey(Giornalista, on_delete=models.CASCADE, related_name="articoli")

    def __str__(self):
        return self.titolo