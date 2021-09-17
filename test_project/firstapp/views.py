from django.shortcuts import render
from django.http import HttpResponse
from .models import Person
 
# def index(request):
#     return HttpResponse("<h2>Главная</h2>")

def index(request):
    return render(request, "index.html")

def users(request):
    return render(request, "users.html")

def ActiveUsersView(request):
    active_list = Person.objects.filter(status=1)
    return render(request, 'users.html', {'active_list': active_list})

def UserDataByLogin(request):
    login_ = str(request.GET.get('login'))
    user_data = Person.objects.filter(login=login_)
    return render(request, 'by_login.html', {'user_data': user_data})

def UserDataByID(request):
    id_ = int(request.GET.get('id'))
    user_data = Person.objects.filter(id=id_)
    return render(request, 'by_id.html', {'user_data':user_data})
