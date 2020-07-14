from django.http import HttpResponse
from datetime import datetime
import json

"""Funcion hello world"""
def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Oh, Hi Current server time is {now}'.format(now=str(now)))

def sort_integers(request):
    """Return a JSON response with sorted integers"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')] 
    sorted_integer = sorted(numbers)
    data = {
        'status': 'True',
        'numbers': sorted_integer,
        'message': 'Integer sorted success'
    }
    """import pdb; pdb.set_trace()"""
    return HttpResponse(json.dumps(data, indent=5), 
            content_type='application/json')

def say_hi(request, name, age):
    """Return a no se que"""

    if age < 12:
        message = 'Sorry {},you are not allowed here.'.format(name)
    else:
        message = 'Hello, {}! Welcome to platzigram'.format(name)
    return HttpResponse(message)

