from yarl import URL


class SteamUser:
    def __init__(self, client, data):
        self._client = client
        self.id = int(data.get('steamid', '1'))
        self.games = []

    async def fetch_owned_games(self, *, currency=None):
        self.games = await self._client.get_owned_games(self.id, currency=currency)

        return self.games


class SteamGame:
    API = URL.build(scheme="https", host="store.steampowered.com")

    def __init__(self, client, data, currency):
        self._client = client
        self.currency = currency
        self.id = int(data.get('appid', '-1'))
        self.playtime_forever = int(data.get('playtime_forever', '-1'))

        self.name = ""
        self.price = 0

    async def fetch_store_details(self):
        data = await self._client.fetch_store_details(self.id, currency=self.currency)

        self.name = data.get('name', 'unknown')
        if data.get('price_overview', None): # None == Free To Play
            self.price = int(data['price_overview']['final']) / 100
