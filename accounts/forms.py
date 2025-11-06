from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from accounts.models import Usuario


class UsuarioCreationForm(UserCreationForm):
    class Meta:
        model = Usuario
        fields = ("username", "email", )

class UsuarioChangeForm(UserChangeForm):
    class Meta:
        model = Usuario
        exclude = ("id",)
        


