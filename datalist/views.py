from django.shortcuts import render, redirect
from .models import Usertask
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required
def main(request):
    name = request.user
    if User.objects.filter(username=name).exists():
        lst = User.objects.get(username=name).usertask_set.all()
        context = {
            'names': lst
        }
        return render(request, 'pages/main.html', context=context)
    else:
        return redirect('create')

def create(request):
    if request.method == 'POST':
        data = request.POST.get('name')
        data = 'empty' if len(data)==0 else data
        user = User.objects.get(username=request.user)
        task = Usertask(user=user, name=data, line='text-decoration-none')
        task.save()
        return redirect('main')
    return render(request, 'pages/create.html')

def done(request, id):
    user = Usertask.objects.get(id=id)
    user.line = 'text-decoration-line-through'
    user.save()
    return redirect('main')


def delete(request, id):
    if request.method == 'POST':
        user = Usertask.objects.get(id=id).delete()
        print(user)
        return redirect('main')
    return render(request, 'pages/edit.html')

def edit(request, id):
    user = Usertask.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        user.name = data.get('name')
        user.save()
        return redirect('main')
    
    return render(request, 'pages/edit.html', {'name': user.name})
# def register(request):
#     if request.method == 'POST':
#         data = request.POST
#         username = data.get('username')
#         password1 = data.get('password1')
#         password2 = data.get('password2')
#         if password1 == password2:
#             user = Username(username=username, password1=password1, password2=password2)
#             user.save()
#         else:
#             return redirect('register')
#         return redirect('main')
#     return render(request, 'pages/register.html')

# def login(request):
#     if request.method == 'POST':
#         data = request.POST
#         username = data.get('username')
#         password1 = data.get('password')
#         if Username.objects.filter(name__exact=username):
#             user = Username.objects.get(name=username)
#             if user.password1 == password1: 
                
    #             return redirect(f'../?name={user.name}')
    # return render(request, 'pages/login.html')