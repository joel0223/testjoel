from django.contrib import admin
from django.urls import path, include  # include permet de déléguer les URLs à une app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('monpremiertuto.urls')),  # monapp doit être remplacé par le nom réel de votre app
]
