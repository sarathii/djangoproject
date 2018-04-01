from django.http import HttpResponse



def home(request):
    return HttpResponse('<html><title>django</title><body><h1>finallly django !!!!</h1></body></html>')