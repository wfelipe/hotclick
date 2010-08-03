from hotclick.click.models import *
from django.contrib import admin

class SiteAdmin(admin.ModelAdmin):
	list_display = ['name', 'url']

class ClickAdmin(admin.ModelAdmin):
	list_display = ['timestamp', 'x', 'y', 'site', 'link']

admin.site.register(Site, SiteAdmin)
admin.site.register(Click, ClickAdmin)
