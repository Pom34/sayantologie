#-*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from miniurl.models import MiniURL
from miniurl.forms import MiniURLForm

def display_miniurls(request):
	miniurls=MiniURL.objects.order_by('-date')
	return render(request, 'miniurl/listofshortenurl.html', locals())


def shorten_url(request):
	if request.method=="POST":
		form=MiniURLForm(request.POST)
		if form.is_valid():
			envoi=True
			form.save()
			return redirect(display_miniurls)
	else:
		form=MiniURLForm()
	return render(request, 'miniurl/shortenurl.html', locals())


def redirect_from_code(request, code_in_url):
	url_to_redirect = get_object_or_404(MiniURL,code=code_in_url)
	url_to_redirect.nb_acces+=1
	url_to_redirect.save()
	return redirect(url_to_redirect.url_long, permanent=True) #Comprendre ce que fait permanent

def redirect_to_allurl_for_non_existent_url(request):
	return redirect(display_miniurls)