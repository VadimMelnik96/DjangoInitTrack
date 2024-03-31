from django.shortcuts import render
from django.views.generic import TemplateView, ListView
# Create your views here.


class IndexView(TemplateView):
    template_name = 'index.html'


class EncounterView(ListView):
    template_name = "user_encounters.html"
