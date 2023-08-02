import datetime
from unit.models import *

def check_availability(unit,date_to,date_from):
    avail = []
    book_list = UnitBook.objects.filter(unit=unit)
    for book in book_list:
        if book.date_from > date_to or book.date_to < date_from:
            avail.append(True)
        else:
            avail.append(False)
    return all(avail)