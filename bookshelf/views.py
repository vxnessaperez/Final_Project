from django.shortcuts import render

def index(request):
    return render(request, 'bookshelf/home.html')


def book_detail(request):
    return render(request, 'bookshelf/book.html')