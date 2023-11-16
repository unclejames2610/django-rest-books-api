from django.contrib import admin
from django.urls import path

# from books_api.views import book_list, book_create, book
from books_api.views import BookCreate, BookList, BookDetail

urlpatterns = [
    # path('list/', book_list),
    # path('', book_create),
    # path('<int:pk>', book)
    path('list/', BookList.as_view()),
    path('', BookCreate.as_view()),
    path('<int:pk>', BookDetail.as_view())
]