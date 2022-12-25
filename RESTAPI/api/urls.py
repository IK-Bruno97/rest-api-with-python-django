from django.urls import path
from . views import Person, PersonUpdate

urlpatterns = [
    path('person-data/', Person.as_view()),
    path('update-person/<int:person_id>', PersonUpdate.as_view()),
]
