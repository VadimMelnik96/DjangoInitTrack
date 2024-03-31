from django.forms import ModelForm
from .models import Player, Monster, Encounter


class EncounterForm(ModelForm):
    class Meta:
        model = Encounter
        fields = "__all__"


class MonsterForm(ModelForm):
    class Meta:
        model = Monster
        fields = "__all__"


class PlayerForm(ModelForm):
    class Meta:
        model = Player
        fields = "__all__"
