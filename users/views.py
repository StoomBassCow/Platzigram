"""Users views"""

from django.contrib.auth import authenticate, login
from django.shortcuts import render

def login_view(request):


    #import pdb; pdb.set_trace()
    if request.method == 'POST':

        print('*' * 30)
        username = request.POST['username']
        password = request.POST['password']
        print('User ', username, ':', 'Pass ', password)
        print('*' * 30)        

    return render(request, 'users/login.html') 