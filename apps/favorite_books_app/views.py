from django.shortcuts import render, redirect
from apps.login_app.models import User
from django.contrib import messages
from .models import *

# Create your views here.
def books(request):
    one_user = User.objects.get(id=request.session['userid'])
    context = {
        "this_user": one_user,
        "all_books":Book.objects.all()
    }
    return render(request,'books.html', context)

    #add a book
#favorite book
#unfavorite book
#edit book
#delete book

def create_book(request):
    if request.method=="POST":
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect("/books")
        else:
            one_user = User.objects.get(id=request.session['userid'])
            title = request.POST.get('title')
            description= request.POST.get('description')
            uploaded_by = one_user
            new_book = Book.objects.create(title=title,description=description,uploaded_by=uploaded_by)
            new_book.save()
            one_user.liked_books.add(new_book.id)

            return redirect(f"/books/{new_book.id}")

def view_book(request, book_id):
    one_book = Book.objects.get(id=book_id)
    one_user = User.objects.get(id=request.session['userid'])
    context = {
        'this_book': one_book,
        'fav_users': one_book.users_who_like.all(),
        'this_user': one_user
    }
    if one_book.uploaded_by_id == one_user.id:
        return render(request,'admin_view_book.html', context)
    else:
        return render(request,'view_book.html', context)

def update_book(request, book_id):
    if request.method=="POST":
        errors = Book.objects.basic_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f"/books/{book_id}")
    else:
            #specify book
            book_to_update = Book.objects.get(id=book_id)
            #update book attirbutes
            book_to_update.title = request.POST.get('title')
            book_to_update.description= request.POST.get('description')
            #save book
            book_to_update.save()
    return redirect(f"/books/{book_id}")

def favorite_book(request, book_id):
    #specify book
    one_user = User.objects.get(id=request.session['userid'])
    one_user.liked_books.add (book_id)
    return redirect(f"/books/{book_id}")

def unfavorite_book(request, book_id):
    one_user = User.objects.get(id=request.session['userid'])
    one_user.liked_books.remove (book_id)
    return redirect(f"/books/{book_id}")

def delete_book(request, book_id):
    """ if request.method=="POST": """
    book_to_delete = Book.objects.get(id=book_id)
    book_to_delete.delete()
    return redirect("/books")

#favorite and unfavorite book functions