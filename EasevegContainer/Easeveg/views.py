
from django.http import HttpResponse,JsonResponse
from django.template import loader
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.shortcuts import redirect, render
from .models import Restaurant, WebUser
#formulario propio
from .forms import MyAuthenticationForm, MyUserCreationForm

#Renderiza la página principal mostrnado un mapa con restaurantes señalados.
def index(request):
    template = loader.get_template("Easeveg/map.html")
    #Exluye aquelos sitios con vlores en longitude y latitude no válidos
    restaurants=Restaurant.objects.exclude(longitude =None , latitude=None)
    #Respuesta del servidor con el contenido renderizado(representado graficamente)
    return HttpResponse(template.render({'restaurants': restaurants}, request))

#Gestión registro de usuarios
def register(request):
    #Solicitud de envio al servidor
    if request.POST:
        print(request.POST)
        #Se crea un objeto formulario con los datos que llegan por post
        register_form=MyUserCreationForm(request.POST)
        #Si el formulario es válido 
        if  register_form.is_valid():
                # Se guarda el usuario de django y crea un WebUser relacionado con User
                user = register_form.save()
                WebUser.objects.create(user=user).save()
                #Se redirige a la página principal
                return redirect("/") 
    else:
        #si no hay datos en el formulario se cargar otra vez, vacío
        register_form=MyUserCreationForm()
    #Se renderiza la vista del formulario
    return render(request, "Easeveg/signup.html", {"register_form": register_form})

#Gestión inicio de sesión
#Recibe objeto request con información de la solicitud http que activa la vista
def login(request):
    #Comprueba si el usuario ha hecho una solicitud post al servidor enviando datos
    if request.POST:
        #Crea instancia de formulario de utenticación personalizado con parametros de datos del formulario
        login_form=MyAuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            #Se coge el objeto usuario realcionado a los datos del formulario
            user=login_form.get_user()
            #Comprueba si el usuario es válid, si lo es inicia sesión
            if user is not None:
                #Permite crear la sesión en la solicitud actul sin que se borre en cada request
                django_login(request, user)
                #Una vez autenticado se redirige a la página principal
                return redirect("/")
    else:
        #Si hay algún error en la solicitud POST se crea una instancia del formulario
        login_form=MyAuthenticationForm()   
    #Renderiza la plantilla de login
    return render(request, "Easeveg/login.html", {"login_form": login_form}) 

#Gestiona cierre de sesión
def logout(request):
    #Llamada a función de Django  que cierra l asesión asociada a los datos en el objeto request
    django_logout(request)
    return redirect("/")

#Gestiona el guardado de restaurantes como favoritos tomando como argumentos el objeto request y el id del sitio marcado
def keep_favourite(request,restaurant_id):
    #TODO: hacer algo cuando no hay usuario logueado (request.user == None) LO HACEMOS EN TEMPLATE
    #request.user:objeto de usuario logueado
    #[0]: se toma primer resultado consulta.
    web_user = WebUser.objects.filter(user = request.user)[0]
    #Se coge un objeto Restaurant según su clave primaria que es restaurant_id
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    #Agrega el objeto restaurant a la lista de restaurantes del usuario usando el cmpo muchos a muchos de WebUser fav_restaurants
    web_user.fav_restaurants.add(restaurant)
    #Guarda el objeto web_user modificado
    web_user.save()
    #Se devuelve una respuesta HTTP que indica que se a guarddo con éxito
    return HttpResponse('recibido')

#Gestiona la acción de mostrar sitios favoritos de un usuario
def show_favourites(request):
    #Filtra los WebUser hasta encontrar el registrado ahora(request.user)
    web_user = WebUser.objects.filter(user = request.user)[0]
    restaurant_list=[]
    #Iteración sobre los objetos restaurant de fav_restaurant de web_user 
    for restaurant in web_user.fav_restaurants.all():
        # Crea diccionario con: nombre, direccion y coordenadas
        dic={
                'id':restaurant.id,
                'name':restaurant.name,
                'direction':restaurant.direction,
                'latitude':restaurant.latitude,
                'longitude':restaurant.longitude
            
        }
        # Añade ese diccionario a una lista
        restaurant_list.append(dic)
    
    #Respuesta HTTP en formato JSON con JsonResponse con la lista de Python que requiere que configurar safe a false par auna serialización correcta de los objetos Python
    return JsonResponse(restaurant_list,safe=False) 