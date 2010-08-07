from django.http import HttpResponse, Http404
from hotclick.click.models import *

def process_click(request):
	click = Click()

	if not 'HTTP_REFERER' in request.META:
		return HttpResponse('NOT OK - Referer')
	try:
		click.site = Site.objects.get(url=request.META['HTTP_REFERER'])
	except Site.DoesNotExist:
		return HttpResponse('Site does not exist')

	for attr in request.GET:
		if hasattr(click, attr):
			setattr(click, attr, request.GET[attr])

	click.save()

	return HttpResponse('OK')
