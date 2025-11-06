from django.urls import path
from .views import index, test, crear_abogado, crear_perito, lista_abogados, crear_jurisdicciones, eliminar_abogado, modificar_abogado
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", index, name="index"),
    path("test/", test , name="test"),
    path("abogados/nuevo", crear_abogado, name= "abogado_form"),
    path("peritos/nuevo", crear_perito, name= "perito_form"),
    path("abogados/", lista_abogados, name="abogados_list"),
    path("jurisdicciones/", crear_jurisdicciones, name="jurisdicciones_form"),
    path("abogado/<int:nro_abogado>/eliminar", eliminar_abogado, name="eliminar_abogado"),
    path("abogado/<int:nro_abogado>/modificar", modificar_abogado, name="modificar_abogado"),
    path('login/', auth_views.LoginView.as_view(template_name='coder/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]