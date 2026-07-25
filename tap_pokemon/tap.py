# Copyright (c) 2026 Edgar-Ramírez Mondragón

"""Pokemon tap class."""

from __future__ import annotations

import typing as t

from requests_cache import install_cache
from singer_sdk import Stream, Tap
from singer_sdk import typing as th

from tap_pokemon.streams import PokemonSpecies

if t.TYPE_CHECKING:
    from singer_sdk.streams import RESTStream

STREAM_TYPES: list[type[RESTStream]] = [
    PokemonSpecies,
]


class TapPokemon(Tap):
    """Singer tap for Pokémon."""

    name = "tap-pokemon"

    config_jsonschema = th.PropertiesList(
        th.Property(
            "base_url",
            th.StringType,
            description="The base URL of the Pokémon API.",
            default="https://pokeapi.co",
        ),
    ).to_dict()

    def __init__(self, *args: t.Any, **kwargs: t.Any) -> None:
        """Initialize the tap.

        Args:
            *args: Positional arguments.
            **kwargs: Keyword arguments.
        """
        super().__init__(*args, **kwargs)
        install_cache()

    def discover_streams(self) -> list[Stream]:
        """Return a list of discovered streams.

        Returns:
            A list of Pokemon streams.
        """
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
