#-*- coding: utf-8 -*-
from django.db import models
import string, random

class MiniURL(models.Model):
	url_long=models.URLField(unique=True)
	code=models.CharField(max_length=6, unique=True)
	date=models.DateTimeField(auto_now_add=True, auto_now=False,verbose_name="Date de création du raccourci")
	pseudo=models.CharField(max_length=10)
	nb_acces=models.IntegerField(default=0)

	def __unicode__(self):
		return u"[{0}] {1}".format(self.code, self.url_long)

	def save(self, *args, **kwargs):  #comprendre le fonctionnement de args/kwargs
		if self.pk is None:
			self.generer(6)
		super(MiniURL,self).save(*args, **kwargs)  #comprendre le fonctionnement de super

	def generer(self,N):
		caracteres=string.letters+string.digits
		aleatoire=[random.choice(caracteres) for _ in xrange(N)]
		self.code=''.join(aleatoire)

	class Meta: #comprendre le fonctionnement de Meta
		verbose_name="Mini URL"
		verbose_name_plural="Minis URL"