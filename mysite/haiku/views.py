from django.http import HttpResponse

# Create your views here.
def index(reqest):
  return HttpResponse("Hello world.")