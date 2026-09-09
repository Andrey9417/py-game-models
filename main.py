import json

import init_django_orm  # noqa: F401

from db.models import Race, Skill, Player, Guild


def main() -> None:
    players_dict = {}
    with open("players.json") as file_data:
        players_dict = json.load(file_data)

    for key, value in players_dict.items():
        guild = None
        if value["guild"]:
            guild, _ = Guild.objects.get_or_create(
                name=value["guild"]["name"],
                defaults=dict(description=value["guild"].get("description"))
            )
        race, _ = Race.objects.get_or_create(
            name=value["race"]["name"],
            defaults=dict(description=value["race"]["description"])
        )
        for skill in value["race"]["skills"]:
            Skill.objects.get_or_create(
                name=skill["name"],
                defaults=dict(bonus=skill["bonus"], race=race)
            )
        Player.objects.get_or_create(
            nickname=key,
            defaults=dict(
                email=value["email"],
                bio=value["bio"],
                race=race,
                guild=guild
            )
        )


if __name__ == "__main__":
    main()
