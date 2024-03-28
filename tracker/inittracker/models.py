from datetime import datetime
from time import timezone

from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField

STATUSES = (
    ('bl', "Blinded"),
    ("ch", "Charmed"),
    ("df", "Deafened"),
    ("fr", "Frightened"),
    ("inc", "Incapacitated"),
    ("inv", "Invisible"),
    ("par", "Paralyzed"),
    ("pet", "Petrified"),
    ("pois", "Poisoned"),
    ("pr", "Prone"),
    ("rt", "Restrained"),
    ("st", "Stunned"),
    ("unc", "Unconscious")
)


class Encounter(models.Model):
    name = models.CharField(max_length=150)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

class Monster(models.Model):
    name = models.CharField(max_length=150)
    initiative = models.IntegerField(default=0)
    armour_class = models.IntegerField()
    hit_points = models.IntegerField()
    status = ArrayField(models.CharField(choices=STATUSES, blank=True))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    encounters = models.ManyToManyField(Encounter)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Player(models.Model):
    name = models.CharField(max_length=150)
    initiative = models.IntegerField(default=0)
    armour_class = models.IntegerField()
    status = ArrayField(models.CharField(choices=STATUSES, blank=True))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    encounters = models.ManyToManyField(Encounter)
    description = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

