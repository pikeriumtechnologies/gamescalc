# gamescalc [Work In Progress]

This is a nifty little library that allows you to get the games a user owns and lets you know the price.

Currently supported platforms:
- Steam

## Requirements

- `aiohttp` (and `yarl`)

## Example

```py
>>> from gamescalc.steam.steam import Steam
>>> s = Steam(api_key='...')
>>> await s.init()
>>> await s.find_user("NCPlayz")
>>> await _.fetch_owned_games()
>>> for game in _:
...     print(game.name, game.price)
```
