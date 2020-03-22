from requests import Session


class HTTPClient:
    def __init__(self, session, url):
        self._session = session
        self.url = url

    async def request(self, verb, endpoint, *, url=None, **parameters):
        url = (url or self.url).with_path(endpoint).with_query(parameters)
        
        async with self._session.request(verb, url) as r:
            data = await r.json()

        return data
