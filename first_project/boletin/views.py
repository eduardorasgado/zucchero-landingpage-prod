# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#para testing email
from django.core.mail import send_mail
from django.conf import settings

from django.shortcuts import render
from .models import Registrado
from .forms import RegModelForm, ContactForm
# Create your views here.

def inicio(request):
	titulo = "Regístrate a nuestro boletin semanal, es sencillo."
	if request.user.is_authenticated():
		titulo = "Bienvenido(a) %s" %(request.user)
	form = RegModelForm(request.POST or None)

	context = {"titulo":titulo,"el_form":form}
	
	#print(dir(form))  #truquillo para ver en consola todas las opciones de form
	if  form.is_valid():
		#para cuentas .edu
		instance = form.save(commit=False) #guardar sin registrar
		#operaciones de preguardado aqui en medio
		nombre = form.cleaned_data.get("nombre")
		email = form.cleaned_data.get("email")
		#ahora se guarda
		instance.save()

		context = {"titulo":"Gracias %s! Ahora tendrás acceso a más contenido." %(nombre)}

		print(instance)
		print(instance.timestamp)

		#solo para RegForm---->no considera cuentas .edu
		#form_data = form.cleaned_data
		#emaill = form_data.get("email")
		#name_tap = form_data.get("nombre")
		#obj = Registrado.objects.create(email=emaill,nombre=name_tap)
		
		#otra forma
		#obj = Registrado()
		#obj.email = emaill
		#obj.nombre = name_tap
		#obj.save()

	#context = {"titulo":titulo,"el_form":form}

	if request.user.is_authenticated() and request.user.is_staff:
		    context = {
		        "queryset" : ['abc','1'],
		    }

	return render(request,"inicio.html",context)

def contact(request):
	titulo = "Dudas, sugerencias, o algo en especial, contáctanos!"
	form = ContactForm(request.POST or None)
	context = {"form": form,"titulo":titulo}

	if form.is_valid():
		titulo = "Gracias por tus mensajes, nos ayudas a crecer :)"
		form_mensaje = form.cleaned_data.get("mensaje")
		form_correo = form.cleaned_data.get("email")
		form_nombre = form.cleaned_data.get("nombre")
		if form_nombre == None:
			form_nombre = "Persona"
		#envio de mensaje del cliente de la web, tomando mi correo para hacer el envio a mi propio correo
		#mi correo es un medio
		#se puede crear otro correo con motivo de enviar a otro correo llamado sugerencias

		asunto = 'Form de Contacto. Sugerencias'
		email_from = settings.EMAIL_HOST_USER
		email_to = [email_from]
		email_mensaje = "%s: %s, enviado por %s" %(form_nombre,form_mensaje,form_correo)
		send_mail(asunto, email_mensaje, email_from, email_to,fail_silently=False)
		
		print(form_mensaje, form_correo)
		context = {"titulo":titulo,}


	return render(request,"forms.html",context)