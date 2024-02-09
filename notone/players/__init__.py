from importlib import import_module as add
from random import choice

from notone.types import Player

"""Update the list below to change which players will play the game."""


def load() -> list[Player]:
    default_players = [
        add("notone.players.aggro_aiden"),
        add("notone.players.cautious_carter"),
    ]
    challenger_players = [
        add("notone.players.nadire_beatrycze"),
    ]

    return [
        choice(default_players),
        choice(challenger_players),
    ]
