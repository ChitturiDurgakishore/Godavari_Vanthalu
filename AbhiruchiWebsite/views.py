from django.shortcuts import render
from .models import Contacts
# Create your views here.
def Home(req):
    return render(req,'AbhiruchiWebsite/home.html')

def DBI(req):
    contacts=Contacts.objects.all
    return render(req,'AbhiruchiWebsite/DB.html',{'contacts':contacts})