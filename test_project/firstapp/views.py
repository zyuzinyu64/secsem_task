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

def admin_data(request):
    admin = Person.objects.filter(login='admin')
    return render(request, 'admin.html', {'admin_data': admin})

def user_data(request, id):
    user_data = Person.objects.filter(id=id)
    return render(request, 'other_users.html', {'user_data':user_data, 'id':id})
