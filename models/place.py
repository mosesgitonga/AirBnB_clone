#!/usr/bin/python3
""" place class"""

class Place(BaseModel):
    """city initialization"""

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_of_rooms = 0
    number_of_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
