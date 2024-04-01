from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import Encounter


# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class EncounterListView(ListView):

    template_name = "user_encounters.html"
    context_object_name = "encounters"

    def get_queryset(self):
        return Encounter.objects.filter(user=self.request.user)


class EncounterDetailView(DetailView):
    model = Encounter
    template_name = "encounter_detail.html"
