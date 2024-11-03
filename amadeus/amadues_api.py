import requests
from django.conf import settings



def get_access_token():
    url = "https://test.api.amadeus.com/v1/security/oauth2/token"
    data = {
        "grant_type": "client_credentials",
        "client_id": settings.AMADEUS_CLIENT_ID,
        "client_secret": settings.AMADEUS_CLIENT_SECRET
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        raise Exception("Could not retrieve access token: " + response.text)
    


def get_all_hotels(city_code, query=None):
    access_token = get_access_token()
    url = "https://test.api.amadeus.com/v1/reference-data/locations/hotels/by-city"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "cityCode": city_code
    }
    response = requests.get(url, headers=headers, params=params)
    hotels = response.json().get("data", [])
    if query:
        hotels = [hotel for hotel in hotels if query.lower() in hotel.get("name", "").lower()]

    return hotels


