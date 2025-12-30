from django.shortcuts import render, get_object_or_404
from .models import Account

def index(request,id):
    data = get_object_or_404(Account, id=id)
    context = {
        'information': data,
    }
    return render(request,'account/index.html',context)