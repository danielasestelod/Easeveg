from django.urls import path
from . import views
#Este archivo perite la navegación dentro de una aplicación Django
#Lista de rutas de las funciones de views.py
urlpatterns = [
    
    path("", views.index, name="index"),
    #La url "/register" se accede a la vista register y se asigna un nombre register
    #Los nombres s eusan para poder referirse a la ruta en el código
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    #Una ruta dinámina que con un parámetro restaurant_id que es un entero y permite ñadir  a lista de favoritos
    #Ej:/favourites/1
    path("favourites/<int:restaurant_id>",views.keep_favourite,name="favourites"),
    path("show_favourites",views.show_favourites,name="show_favourites"),  
]