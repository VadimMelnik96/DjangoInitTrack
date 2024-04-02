from django.urls import path, include

from .views import IndexView, EncounterListView, EncounterDetailView, EncounterCreateView

app_name = "inittracker"

urlpatterns = [
    path('', IndexView.as_view(), name="main"),
    path('encounters/', EncounterListView.as_view(), name='user_encounters'),
    path('encounters/<int:pk>', EncounterDetailView.as_view(), name='encounter_detail'),
    path('create_encounter/', EncounterCreateView.as_view(), name="create_encounter")
]
