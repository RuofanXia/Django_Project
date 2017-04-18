from django.contrib import admin
from scgarden.models import ImageGallery


class ImagesAdmin(admin.ModelAdmin):
	#fieldsets = [
	#	(None,				 {'fields':['image_text']}),
	#	('Date information', {'fields':['pub_date'], 'classes': ['collapse']}),
		#('Image', {'fields':['image_tag']}),
	#]
	#readonly_fields = ('image_tag',)
	#list_display = ('image_text', 'pub_date', 'image_tag',)
	list_display = ('image_text', 'pub_date', 'was_published_recently', 'image_tag',)
	list_filter = ['pub_date']
	search_fields = ['image_text']

admin.site.register(ImageGallery, ImagesAdmin)
#admin.site.register(ImageContent)
# Register your models here.

