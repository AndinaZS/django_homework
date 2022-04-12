from django.shortcuts import render, redirect

from books.models import Book


def index_view(request):
    return redirect('books')


def books_view(request):
    template = 'books/books_list.html'
    context = {'books': [book for book in Book.objects.all()]}
    return render(request, template, context)


def books_date_view(request, pub_date):
    template = 'books/books_list.html'
    try:
        prev_data = Book.objects.order_by('pub_date').filter(pub_date__lt=pub_date).first().pub_date
    except AttributeError:
        prev_data = None
    try:
        next_data = Book.objects.order_by('pub_date').filter(pub_date__gt=pub_date).first().pub_date
    except AttributeError:
        next_data = None
    context = {'books': [book for book in Book.objects.filter(pub_date=pub_date)],
               'prev_data': prev_data,
               'next_data': next_data
               }
    return render(request, template, context)