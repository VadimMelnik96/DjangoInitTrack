from django.contrib import admin

from .models import Encounter, Monster, Player

# Register your models here.
admin.site.register(Encounter)
admin.site.register(Monster)
admin.site.register(Player)