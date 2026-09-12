# Copyright (c) 2026 Edgar-Ramírez Mondragón

"""Pokemon tap class."""

from __future__ import annotations

from typing import Any, override

from requests_cache import install_cache
from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_pokemon.streams import PokemonSpecies


class TapPokemon(Tap):
    """Singer tap for Pokémon."""

    name = "tap-pokemon"
    config_jsonschema = th.PropertiesList().to_dict()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the tap.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        install_cache()

    @override
    def discover_streams(self) -> list[Stream]:
        return [
            PokemonSpecies(tap=self),
        ]
