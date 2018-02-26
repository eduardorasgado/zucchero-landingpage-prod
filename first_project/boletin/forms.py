#forms
from django import forms
from .models import Registrado
#import re

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		"""
		email_base,proveeder = email.split("@")
		dominio, extension= proveeder.split(".")  #ojo este metodo solo funciona para estos correos: correo@dominio.edu
		if not extension =="edu":
			raise forms.ValidationError("Si usted es miembro de esta universidad por favor utilice el email escolar")
		return email
		"""
		#####if not re.search("edu",email):
		email_ref = []
		if not "@" in email or not ".edu" in email:
			raise forms.ValidationError("Si usted es miembro de esta universidad por favor utilice el email escolar")
		else:
			for i in range(0,len(email)):
				if email[i]=="@":
					email_ref.append(i)
					for k in range(i,len(email)):
						if email[k:(k+4)] ==".edu":
							email_ref.append(k)
							
			#print(email_ref)
			if len(email_ref)==1:
				raise forms.ValidationError("Si usted es miembro de esta universidad por favor utilice el email escolar")
			elif len(email_ref)==2:
				if email_ref[0] < email_ref[1]:
					return email
	
	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		#validaciones
		return nombre

class ContactForm(forms.Form):
	nombre = forms.CharField(required=False)
	email = forms.EmailField()
	mensaje = forms.CharField(widget=forms.Textarea)