from webbrowser import get
from django.shortcuts import render, redirect
from .models import UserData

def main(request):
    
    lst = UserData.objects.all()
    context = {
        'names': lst
    }
    return render(request, 'pages/main.html', context=context)

def create(request):
    if request.method == 'POST':
        data = request.POST
        print('data', data)
        user = UserData(name=data.get('name'))
        user.save()
        return redirect('main')
    else:
        return render(request, 'pages/create.html')

def edit(request, id):
    if request.method == 'POST':
        user = UserData.objects.get(id=id).delete()
        print(user)
        return redirect('main')
    return render(request, 'pages/edit.html')