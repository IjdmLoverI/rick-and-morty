import requests
from django.conf import settings

from characters.models import Character


def scrape_rick_and_morty() -> list[Character]:
    next_url_to_scrape = settings.RICK_AND_MORTY_API_URL

    characters = []
    while next_url_to_scrape is not None:
        characters_response = requests.get(next_url_to_scrape).json()

        for character in characters_response["results"]:
            characters.append(
                Character(
                    api_id=character["id"],
                    name=character["name"],
                    status=character["status"],
                    species=character["species"],
                    gender=character["gender"],
                    image=character["image"]
                )
            )
        next_url_to_scrape = characters_response["info"]["next"]

    return characters


def save_characters(characters: list[Character]) -> None:
    for character in characters:
        character.save()


def sync_characters_with_api() -> None:
    characters = scrape_rick_and_morty()
    save_characters(characters)
