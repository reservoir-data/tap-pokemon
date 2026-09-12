# Copyright (c) 2026 Edgar-Ramírez Mondragón

"""REST client handling, including PokemonStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, Any, override
from urllib.parse import parse_qs, urlparse

from requests_cache import CachedSession
from singer_sdk import RESTStream

if TYPE_CHECKING:
    import requests
    from singer_sdk.helpers.types import Context


class PokemonStream(RESTStream):
    """Pokemon stream class."""

    records_jsonpath = "$.results[*]"
    next_page_token_jsonpath = "$.next"  # ruff: ignore[hardcoded-password-string]
    url_base = "https://pokeapi.co"

    @override
    @property
    def requests_session(self) -> requests.Session:
        return CachedSession()

    @override
    def get_url_params(self, context: Context | None, next_page_token: str | None) -> dict[str, Any]:
        params: dict = {}
        next_url = urlparse(next_page_token) if next_page_token else None

        if next_url:
            query = parse_qs(next_url.query)
            params["offset"] = query.get("offset", [""])[0]
            params["limit"] = query.get("limit", [""])[0]
        else:
            params["limit"] = 100

        return params
