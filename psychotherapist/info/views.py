from django.shortcuts import render, redirect
from .models import Airtable

def index(request):
    cur_info = Airtable.objects.all
    context = {'cur_info': cur_info}
    return render(request, 'index.html', context)

def lc(request, rec_id):
    try:
        info = Airtable.objects.get(recid=rec_id)
    except:
        return redirect('/')
    context = {'info': info}
    return render(request, 'lc.html', context)
