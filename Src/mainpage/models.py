from django.db import models


# Create your models here.

class PageModule(models.Model):
	pageModule_text = models.CharField(max_length=200)
	url_text = models.URLField(max_length=200)
	# ...
	def __unicode__(self):
		return u'%s %s' % (self.pageModule_text, self.url_text)

class SingleModule(models.Model):
	pageModule = models.ForeignKey(PageModule)
	singleModule_text = models.CharField(max_length=200)
	singleModule_url_text = models.URLField(max_length=200)

	def __unicode__(self):
		return u'%s %s' % (self.singleModule_text, self.singleModule_url_text)
