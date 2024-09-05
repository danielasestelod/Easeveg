# 🌱Mapa Interactivo de Restaurantes Veganos y Vegetarianos
Esto es un proyecto de un mapa interactivo para localizar restaurantes veganos y vegetarianos. Este mapa permite a los usuarios visualizar fácilmente los sitios cercanos que ofrecen opciones veganas o vegetarianas, con características personalizables como favoritos, rutas y más.
  
## 🚀 Funcionalidades  
- Visualización de restaurantes: Los restaurantes aparecen distribuidos en el mapa mediante pines que marcan su ubicación exacta.  
- Detalles de los sitios: Al hacer clic en un pin, se muestra el nombre del restaurante.  
- Favoritos: Los usuarios logueados pueden marcar restaurantes como favoritos.  
- Creación de rutas: Indica un punto de inicio y un destino para obtener una ruta detallada.
- Búsqueda por dirección: Encuentra una ubicación exacta en el mapa.
- Modos de vista: Alterna entre modo oscuro (dark mode) o vista normal.

  
## 🛠️ Tecnologías Utilizadas  

[![JavaScript,HTML,CSS,Django,MySql,Selenium](https://skillicons.dev/icons?i=js,html,css,django,mysql,selenium)](https://skillicons.dev)

 
## 📚 Instalación y Configuración  
### Requisitos Previos
- Python 3^
- Django
- MySQL
- Librerías necesarias:
~~~
pip install django mysqlclient
~~~
### Pasos para Instalar
1. Clona el repositorio:
~~~
git clone https://github.com/danielasestelod/Easeveg.git
~~~
~~~
cd nombre-proyecto
~~~
2. Instala virtualenv:
~~~
pip install virtualenv
~~~
3. Configura el entorno virtual:
~~~
virtualenv venv
~~~
~~~
source venv/bin/activate   # En macOS/Linux
venv\Scripts\activate      # En Windows
~~~

4. Instala las dependencias del backend:


5. Configura la base de datos en settings.py: Asegúrate de que el archivo settings.py tenga las credenciales correctas para tu base de datos MySQL:
~~~
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nombre_base_datos',
        'USER': 'tu_usuario',
        'PASSWORD': 'tu_contraseña',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
~~~
6. Aplica las migraciones:
~~~
python manage.py migrate
~~~
7. Ejecuta el servidor:
~~~
python manage.py runserver
~~~

8. Accede a la aplicación: Abre tu navegador y ve a http://127.0.0.1:8000/ para interactuar con la aplicación.  

## 🎨 La aplicación:  

<img src="https://github.com/user-attachments/assets/4e6c7fdb-cd06-4450-bc48-09e7a736038d" alt="pines en el mapa" width="400"/>
<img src="https://github.com/user-attachments/assets/37c8df4e-2362-4f2c-8de1-c7992b7f748b" alt="información de un local" width="300"/>
<img src="https://github.com/user-attachments/assets/f4247da4-c169-40be-9f26-5d82334fb6bc" alt="ruta" width="400"/>
<img src="https://github.com/user-attachments/assets/904ae919-c5f9-4cb7-881b-471db6b3fbed" alt="lista de favoritos" width="600"/></br>
<img src="https://github.com/user-attachments/assets/6b8225c8-70c9-44f7-abc9-c8263afbad56" alt="busqueda dirección" width="400"/>

## 🤝 Contribuciones  
Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama:
~~~
git checkout -b nombre-rama
~~~
4. Realiza tus cambios:
~~~
git commit -m 'Añadir nueva funcionalidad'
~~~
5. Sube la rama:
 ~~~
 git push origin nombre-rama
 ~~~
7. Haz un Pull Request.

## 💡 Agradecimientos
A la comunidad de Leaflet por su librería de mapas.
