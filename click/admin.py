from hotclick.click.models import *
from django.contrib import admin

class SiteAdmin(admin.ModelAdmin):
	list_display = ['name']

class SiteURLAdmin(admin.ModelAdmin):
	list_display = ['site', 'url']

class ClickAdmin(admin.ModelAdmin):
	list_display = ['timestamp', 'x', 'y', 'siteurl', 'link']

admin.site.register(Site, SiteAdmin)
admin.site.register(SiteURL, SiteURLAdmin)
admin.site.register(Click, ClickAdmin)
