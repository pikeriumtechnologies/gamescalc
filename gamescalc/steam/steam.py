from yarl import URL

from gamescalc.base import Base
from .objects import SteamUser, SteamGame

class Steam(Base):
    API = URL.build(scheme="https", host="api.steampowered.com")
    STORE_API = URL.build(scheme="https", host="store.steampowered.com")
    CURRENCY = 'GBP'

    async def find_user(self, username):
        data = await self._http.request('GET', "/ISteamUser/ResolveVanityURL/v1/", key=self._api_key, vanityurl=username)

        user = SteamUser(self, data['response'])

        return user

    async def get_owned_games(self, steam_id, *, currency=None):
        currency = currency or self.CURRENCY

        data = await self._http.request('GET', "/IPlayerService/GetOwnedGames/v1/", key=self._api_key, steamid=steam_id, format='json')

        games = []

        for game in data['response']['games']:
            game = SteamGame(self, game, currency)
            await game.fetch_store_details()
            games.append(game)

        return games

    async def fetch_store_details(self, app_id, *, currency=None):
        currency = currency or self.CURRENCY

        data = await self._http.request('GET', '/api/appdetails', url=self.STORE_API, appids=app_id, currency=currency)

        if data[str(app_id)]['success']:
            return data[str(app_id)]['data']
        return {} # not found
