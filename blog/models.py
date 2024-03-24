from django.db import models

class Post(models.Model):
    # define your fields here    
    pass
class Voetbalspeler(models.Model):
    naam = models.CharField(max_length=255)
    club = models.CharField(max_length=255)
    auteur = models.CharField(max_length=255)
    datum_invoer = models.DateTimeField(auto_now_add=True)
    datum_laatste_aanpassing = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.naam

    def opslaan_en_publiceren(self):
        self.save()
        self.publiceren()
