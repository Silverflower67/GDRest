# User API
___
As with levels (see [Level API](levels.md)), GDRest also has an API for users

## Reading routes
All routes start by the base url (by default http://localhost:4700)

## GET Routes
`/user/<name>`  
Returns a user's info. For example, `/user/Ares` returns this:
```json
{
    "name": "Ares",
    "playerID": 5882651,
    "accountID": 489692,
    "rank": 27178,
    "stars": 7536,
    "diamonds": 7682,
    "coins": 149,
    "userCoins": 1346,
    "demons": 140,
    "cp": 19,
    "mod": {
        "isMod": true,
        "elder": true
    },
    "social": {
        "youtube": null,
        "twitter": "https://twitter.com/Naedian",
        "twitch": "https://twitch.tv/naedian"
    }
}
```  
`/user/<name>/levels`
Returns a list of the user's levels. For example, `/user/Mineber/levels` returns this (only the  
first 3 appear here):
```json
{
  "levels": [
  {
    "name": "Fala",
    "id": 73678606,
    "description": "New solo lvl with different style! So simple but i tried something different ^^ 6*? Made in 9h~ with 17k obj",
    "difficulty": "Harder",
    "downloads": 346,
    "length": "LONG",
    "stars": 0,
    "rated": false,
    "featured": false,
    "epic": false,
    "song": {
      "name": "TheFatRat - Fire",
      "author": "ThisIsTheFatRat",
      "id": 1071391,
      "scope": "custom",
      "link": "https://www.newgrounds.com/audio/listen/1071391",
      "download_link": "https://audio.ngfiles.com/1071000/1071391_TheFatRat---Fire.mp3?f1630069831"
    }
  },
  {
    "name": "Raly",
    "id": 73576923,
    "description": "New solo level! Hard 5*? ^^",
    "difficulty": "Hard",
    "downloads": 285993,
    "length": "LONG",
    "stars": 5,
    "rated": true,
    "featured": true,
    "epic": false,
    "song": {
      "name": "Celestine Era / ????????",
      "author": "Kumi-P",
      "id": 1068479,
      "scope": "custom",
      "link": "https://www.newgrounds.com/audio/listen/1068479",
      "download_link": "https://audio.ngfiles.com/1068000/1068479_Celestine-Era--.mp3?f1629351793"
    }
  },
  {
    "name": "Levas polka",
    "id": 73359254,
    "description": "A level that alexins has given me, i did some improvements before upload it. Thanks alexins!",
    "difficulty": "Harder",
    "downloads": 6152,
    "length": "LONG",
    "stars": 6,
    "rated": true,
    "featured": true,
    "epic": false,
    "song": {
      "name": "Levas Polka (Remix)-EuroDance",
      "author": "A-n-d-Y-J",
      "id": 166097,
      "scope": "custom",
      "link": "https://www.newgrounds.com/audio/listen/166097",
      "download_link": "http://audio.ngfiles.com/166000/166097_AndY_J___Leva_s_Polka__Rem.mp3"
    }
  }
]
}
```