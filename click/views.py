from django.http import HttpResponse

def process_click(request):
	import pprint
	pp = pprint.PrettyPrinter(indent=4)
	return HttpResponse(request.GET['x'])
