from django.http import HttpResponse

def bienvenue(request):
    return HttpResponse("Bienvenue sur mon premier projet Django !")
