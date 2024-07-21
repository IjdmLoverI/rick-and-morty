from django.urls import path

from characters.views import get_random_characters_view

urlpatterns = [
    path("characters/random/", get_random_characters_view, name="character-random")
]

app_name = "characters"
