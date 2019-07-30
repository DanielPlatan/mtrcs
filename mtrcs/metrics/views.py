from metrics.parser import parse

# Create your views here.
from django.http import HttpResponse
def index(request):
    parse()
    return HttpResponse("Parsing OK")
