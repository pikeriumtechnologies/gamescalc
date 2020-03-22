import aiohttp
from yarl import URL

from .http import HTTPClient

class Base:
    API = URL.build(scheme="https", host="placeholder.com")

    def __init__(self, api_key):
        self._api_key = api_key

        self._session = None
        self._http = None

    async def init(self, *, session=None):
        if session is None:
            self._session = aiohttp.ClientSession()

        self._http = HTTPClient(self._session, self.API)
