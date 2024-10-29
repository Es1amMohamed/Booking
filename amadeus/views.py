from django.shortcuts import render
from django.core.paginator import Paginator
from .amadues_api import *

def all_hotels_view(request):
    
    city_code = request.GET.get('city_code', 'LON')
    search_query = request.GET.get('query', '')
    hotels = get_all_hotels(city_code, search_query) 
    page_number = request.GET.get('page', 1) 
    hotels_per_page = 10  
    paginator = Paginator(hotels, hotels_per_page)
    page_obj = paginator.get_page(page_number)
    return render(request, 'hotels/all_hotels.html',
                {
                'hotels': page_obj,
                'query': search_query,
                })



def hotel_detail_view(request, hotelId):
  
    city_code = request.GET.get('city_code', 'LON')  
    hotels = get_all_hotels(city_code)

    hotel = next((hotel for hotel in hotels if hotel["hotelId"] == hotelId), None)

    if hotel:
        return render(request, 'hotels/hotel_detail.html', {'hotel': hotel})
    else:
        return render(request, 'hotels/hotel_detail.html', {'error': 'Hotel not found.'})
