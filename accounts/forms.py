from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email", )

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "avatar",
            "fecha_de_nacimiento",
            "direccion",
        ]
        labels = {
            "username": "Nombre de usuario",
            "first_name": "Nombre",
            "last_name": "Apellido",
            "email": "Correo electrónico",
            "avatar": "Foto de perfil",
            "fecha_de_nacimiento": "Fecha de nacimiento",
            "direccion": "Dirección",
        }
        


