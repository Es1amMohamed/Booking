import datetime
from unit.models import Unit , UnitBook



def check_availability(unit,date_from,date_to):
    avail = []
    unit_list = UnitBook.objects.filter(unit=unit)
    for book in unit_list:
        if book.date_from > date_to or book.date_to < date_from:
            avail.append(True)
        else:
            avail.append(False)
    return all(avail)