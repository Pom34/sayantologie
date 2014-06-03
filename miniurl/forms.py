#-*- coding: utf-8 -*-
from django import forms
from miniurl.models import MiniURL

class MiniURLForm(forms.ModelForm):
	class Meta:
		model=MiniURL
		fields=('url_long','pseudo')