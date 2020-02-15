from datetime import datetime


venue_list = [
    {
    "type": "venue",
    "name": "Madison Square Garden",
    "genre": ["Rock",
              "Pop",
              "Hip-Hop"],
    "start": [datetime(2020, 2, 8, 19, 30),
              datetime(2020, 2, 9, 17, 0),
              datetime(2020, 2, 10, 18, 0)],
    "end": [datetime(2020, 2, 8, 22, 30),
            datetime(2020, 2, 9, 19, 0),
            datetime(2020, 2, 11, 0, 0)],
    "description": "World's most famous venue."
     },

    {
    "type": "venue Center",
    "name": "Moda",
    "genre": ["Folk",
              "Pop",
              "Country"],
    "start": [datetime(2020, 2, 8, 18, 30),
              datetime(2020, 2, 9, 16, 0),
              datetime(2020, 2, 12, 17, 0)],
    "end":   [datetime(2020, 2, 8, 21, 30),
              datetime(2020, 2, 9, 17, 0),
              datetime(2020, 2, 12, 22, 0)],
    "description": "Home of the trail Blazers."
    },

    {
    "type": "venue",
    "name": "Staples",
    "genre": ["Metal",
              "Rock",
              "Pop",
              "Hip-Hop"],
    "start": [datetime(2020, 2, 8, 18, 30),
              datetime(2020, 2, 10, 16, 30),
              datetime(2020, 2, 11, 17, 30)],
    "end":   [datetime(2020, 2, 9, 21, 30),
              datetime(2020, 2, 10, 18, 30),
              datetime(2020, 2, 11, 19, 30)],
    "description": "RIP Kobe."
    }
]
