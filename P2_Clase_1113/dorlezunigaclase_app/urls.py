from django.contrib import path
from . import views
urlpatterns = [
    path('',views.hola, name='dorlezunigaclase_app'),
]