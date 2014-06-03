#-*- coding: utf-8 -*-
from django.contrib import admin
from miniurl.models import MiniURL

class MiniURLAdmin(admin.ModelAdmin):
	list_display=('url_long','code', 'date', 'pseudo','nb_acces',)
	list_filter=('pseudo',)
	date_hierarchy='date'
	ordering=('date',)
	search_fields=('url_long',)
	
admin.site.register(MiniURL, MiniURLAdmin)
