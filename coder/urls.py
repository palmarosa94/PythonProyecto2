from django.urls import path
from .views import index, test, crear_abogado, crear_perito, lista_abogados, crear_jurisdicciones

urlpatterns = [
    path("", index, name="index"),
    path("test/", test , name="test"),
    path("abogados/nuevo", crear_abogado, name= "abogado_form"),
    path("peritos/nuevo", crear_perito, name= "perito_form"),
    path("abogados/", lista_abogados, name="abogado_list"),
    path("jurisdicciones/", crear_jurisdicciones, name="jurisdicciones_form"),
]