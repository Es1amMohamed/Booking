from django.shortcuts import render
from .amadues_api import *

def all_hotels_view(request):
    city_code = request.GET.get('city_code', 'LON')
    search_query = request.GET.get('query', '')
    hotels = get_all_hotels(city_code, search_query) 
    return render(request, 'hotels/all_hotels.html', {'hotels': hotels, 'query': search_query})



def hotel_detail_view(request, hotelId):
  
    city_code = request.GET.get('city_code', 'LON')  
    hotels = get_all_hotels(city_code)

    hotel = next((hotel for hotel in hotels if hotel["hotelId"] == hotelId), None)

    if hotel:
        return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})
    else:
        return render(request, 'hotels/hotel_detail.html', {'error': 'Hotel not found.'})
