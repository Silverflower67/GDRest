# Level API
___
GDRest offers an API for getting level data. You can get data about levels,
commenting, etc.
## Reading routes
This routes always start by the base url (by default http://localhost:4700)
 ## GET routes
`/level/<id>`  
Returns a level's info. `id` is the level's ID. For example, 
`/level/72941895` returns this:  
```json
{
    "name": "APEX",
    "id": 72941895,
    "description": "Amoung (epilepsy warning)",
    "author": {
        "name": "StarkyTheSalad",
        "id": 21161314
    },
    "difficulty": "Extreme Demon",
    "downloads": 205789,
    "length": "LONG",
    "stars": 10,
    "rated": true,
    "featured": true,
    "epic": true,
    "objects": 88179,
    "overload": true,
    "song": {
        "name": "High in Flight",
        "author": "WaterLemonMusic",
        "id": 927398,
        "scope": "custom",
        "link": "https://www.newgrounds.com/audio/listen/927398",
        "download_link": "https://audio.ngfiles.com/927000/927398_High-in-Flight.mp3?f1587220865"
    }
}
```  
`/level/<id>/author`  
Returns the level's author info. Redirects to `/user/<username>`, where
`username` is the author's username. See [User API](users.md) for more info about the return value
