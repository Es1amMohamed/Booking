import datetime
from unit.models import UnitBook


def check_availability(unit,date_from,date_to):
    avail = []
    unit_list = UnitBook.objects.get(unit=unit)
    #for book in book_list:
    if unit_list.date_from > date_to or unit_list.date_to < date_from:
        avail.append(True)
    else:
        avail.append(False)
    return all(avail)