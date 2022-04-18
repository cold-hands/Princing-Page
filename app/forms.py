from django.forms import ModelForm
from app.models import Planos

# Create the form class.
class PlanosForm(ModelForm):
    class Meta:
        model = Planos
        fields = ['nome', 'preco', 'repositorios', 'membros', 'tamanho', 'suporte']