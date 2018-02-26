 #*- coding: utf-8 -*-

from django.shortcuts import render

def about(request):

	#context = {"titulo":titulo,"el_form":form}
	return render(request,"about.html",{})
