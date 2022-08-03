from multiprocessing import context
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def sign_up(request):
    form = UserCreationForm()
    registrado = False
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registrado = True
    context = {'form':form,'registrado': registrado}
    return render(request, 'app_login/signup.html', context)