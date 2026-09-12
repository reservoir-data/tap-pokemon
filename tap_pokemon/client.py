# Copyright (c) 2026 Edgar-Ramírez Mondragón

"""REST client handling, including PokemonStream base class."""

from __future__ import annotations

from typing import TYPE_CHECKING, override
from urllib.parse import parse_qs, urlparse

from requests_cache import CachedSession
from singer_sdk import RESTStream

if TYPE_CHECKING:
    import requests
    from singer_sdk.streams.rest import HTTPRequest, PageContext


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
    def get_http_request(self, *, page: PageContext[str]) -> HTTPRequest:
        req = super().get_http_request(page=page)
        req.params["limit"] = 100
        if next_url := page.next_page_token:
            parsed = urlparse(next_url)
            query = parse_qs(parsed.query)
            req.params["offset"] = query.get("offset", [""])[0]
            req.params["limit"] = query.get("limit", [""])[0]
        return req
