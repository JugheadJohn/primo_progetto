from django.db import models

# Create your models here.
class Genere_SR(models.Model):
    contenuto = models.CharField()

    def __str__(self):
        return self.contenuto
    
    class Meta:
        verbose_name = "Genere"
        verbose_name_plural = "Generi"

class Autore_SR(models.Model):
    nome = models.CharField()
    cognome = models.CharField()

    def __str__(self):
            return self.nome + " "+ self.cognome
    
    class Meta:
        verbose_name = "Autore"
        verbose_name_plural = "Autori"

class Libro_SR(models.Model):
    titolo = models.CharField()
    isbn = models.CharField(max_length=18)
    pubblicazione = models.ManyToManyField(Genere_SR)
    autore = models.ForeignKey(Autore_SR, on_delete=models.CASCADE, related_name='libri')

    def __str__(self):
        return self.titolo

    class Meta:
        verbose_name = "Libro"
        verbose_name_plural = "Libri"