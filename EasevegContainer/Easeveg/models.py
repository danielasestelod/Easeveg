from django.db import models
#objeto User de django
from django.contrib.auth.models import User

#Clase que hereda de model.Model de django por lo que es un modelo de base de datos
class Restaurant(models.Model):
    url=models.URLField(unique=True)
    name=models.CharField(max_length=250)
    direction=models.CharField(max_length=250)
    latitude=models.FloatField(null=True)
    longitude=models.FloatField(null=True )

#Clase que hereda de model.Models 
class WebUser(models.Model):
    # Relacion con User de Django. 
    # user: campo onoToOneField que estale relación uno a uno con User de django, un modelo. on_delete=models.CASCADE: cuando borras un usuario se borra el usuario de Django correspondiente.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Relacion webUser con restaurants
    # fav_restaurants: relación muchos a muchos con modelo Restaurants para que WebUser tenga varios restaurantes favoritos
    fav_restaurants = models.ManyToManyField(Restaurant)

    # Se crea el modeo WebUser para extender las funcionalidades de User de Django usando OneToOneField y así pudiendo extender las características del modelo usuario.
    # Como existe un modelo de user se puede crear una relación muchos a muchos con restaurants para que los usurios tengan varios favoritos y vicersa.
   