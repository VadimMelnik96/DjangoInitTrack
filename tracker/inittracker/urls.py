from django.urls import path, include

from .views import IndexView, EncounterListView, EncounterDetailView

app_name = "inittracker"

urlpatterns = [
    path('', IndexView.as_view(), name="main"),
    path('encounters/', EncounterListView.as_view(), name='user_encounters'),
    path('encounters/<int:pk>', EncounterDetailView.as_view(), name='encounter_detail'),
]
