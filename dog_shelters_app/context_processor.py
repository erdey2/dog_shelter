import datetime as dt

def current_year(request):
    return {'current_year': dt.date.today().year}