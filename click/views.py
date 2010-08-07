from django.http import HttpResponse, HttpResponseNotFound, HttpResponseBadRequest
from hotclick.click.models import *
from django.db.utils import IntegrityError

def process_click(request):
	click = Click()

	if not 'HTTP_REFERER' in request.META:
		return HttpResponseBadRequest('NOT OK - Referer')
	try:
		click.siteurl = SiteURL.objects.get(url=request.META['HTTP_REFERER'])
	except SiteURL.DoesNotExist:
		return HttpResponseNotFound('Site does not exist')

	for attr in request.GET:
		if hasattr(click, attr):
			setattr(click, attr, request.GET[attr])

	try:
		click.save()
	except IntegrityError as error:
		return HttpResponseBadRequest("Missing argument: " + error.args[0])

	return HttpResponse('OK')
