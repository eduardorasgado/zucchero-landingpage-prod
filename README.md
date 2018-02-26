# zucchero-django-bootstrap
Una landing page creada en Python y Django, Bootstrap y Font Awesome. Para ser integrada en un ambiente virtual. 

**Es de importancia**: 

Instalar virtualenv en tu ordenador.
Crear un ambiente virtual.
Copiar el contenido del proyecto(si lo clonó) y pegarlo dentro de la carpeta del ambiente virtual.
Instalar requirements.txt


COnsideraciones:

Crea un correo Gmail especial para recibir los mensajes de los usuarios, este también actúa como sender usando protocolo smtp, modificalo en seetings para q los usuarios puedan recibir su link de comprobación.

Sin la llave de comprobación enviada el usuario no se podrá loguear, es decir si no configuras el correo antes mencionado no podrás tener usuarios.

No olvides crear un superuser con python manage.py createsuperuser,
sin esto no podras entrar a administrador.

No olvides quitar el modo debug en seetings.py si planeas hacer deployment.

Cree un static root en el base_dir del enviroment virtual, en pocas palabras hay una base de datos para imagenes de usuarios y aparte hay una para archivos de la pagina, esto no es óptimo en producción me parece, cambiala para desarrollo.

Hay muchas cosas que cambiar para modo producción pero el proyecto está ahi para su personalización.

Los usuarios registrados en boletin estan en una base distinta a los usuarios registrados en el sitio

El proyecto web está en la carpeta first_project
