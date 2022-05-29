
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from bookshelf.models import User
from .forms import UserRegistrationForm
from bookshelf.forms import UserRegistrationForm

@login_required
def index(request):
    return render(request, 'bookshelf/home.html')


def book_detail(request):
    return render(request, 'bookshelf/book.html')

# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # user = form.save()
#             # user.refresh_from_db()
#             # user.save()
#             # username = form.cleaned_data.get('username')
#             # raw_password = form.cleaned_data.get('password1')
#             # user = authenticate(username=username, password=raw_password)
#             # login(request, user)
#             # return redirect('home')
#             messages.success(request, f'Your account has been created. You can log in now!')
#             return redirect('login')
#     else:
#         form = UserRegistrationForm()
        
#     context = { 'form': form }
#     return render(request, 'bookshelf/register.html', context)




def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            messages.success(request, f'Your account has been created. You can log in now!')
            # login(request, User)
            return redirect('login')  
            #return redirect('login')
    else:
        form = UserRegistrationForm()

    context = {'form': form}
    return render(request, 'bookshelf/register.html', context)