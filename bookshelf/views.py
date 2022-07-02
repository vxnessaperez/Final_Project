from django.contrib import messages
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from django.forms import forms
from bookshelf.models import Review
# from django.contrib.auth import login, authenticate
from bookshelf.forms import ReviewForm, UserRegistrationForm

@login_required
def index(request): 
    return render(request, 'bookshelf/home.html')

def book_detail(request):
    return render(request, 'bookshelf/book.html')
    
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

def detail(request, id):
    post = get_object_or_404(Review, pk=id)
    return render(request, "bookshelf/detail.html", {"post": post })

@login_required()
def new(request):
    reviews = Review.objects.all()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form = form.save()
            return redirect("new")
    else:
        form = ReviewForm()
    return render(request, 'bookshelf/new.html', {'form': form ,'reviews': reviews})

def edit_review(request, pk):
    selected_review = get_object_or_404(Review, pk=pk)
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            selected_review = form.save()
            return redirect("home")
    else:
        form = ReviewForm(instance=selected_review)
    return render(request, 'bookshelf/edit_review.html', {'form': form, 'selected_review': selected_review})
    
def delete_review(request, pk):
    if request.method == "GET":
        form = ReviewForm()
        return render(request, 'bookshelf/delete_review.html', {'Reviews': Review})

