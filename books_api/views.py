# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from rest_framework import status
# from books_api.models import Book
# from books_api.serializer import BookSerializer

# # Create your views here.
# @api_view(['GET'])
# def book_list(request):
#     books = Book.objects.all() # complex data
#     # books_python = list(books.values()) #python ds
#     # return JsonResponse({
#     #     'books': books_python
#     # })
#     serializer = BookSerializer(books, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def book_create(request):
#     serializer = BookSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         return Response(serializer.errors)
    
# @api_view(['GET', 'PUT', 'DELETE'])
# def book(request, pk):
#     try:
#         book = Book.objects.get(pk=pk)
#     except:
#         return Response({
#             'error': 'Does not exist'
#         }, status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
    
#     if request.method == "PUT":
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == "DELETE":
#         book.delete()
#         return Response({
#             'delete': True
#         })


from rest_framework.views import APIView
from books_api.models import Book
from books_api.serializer import BookSerializer
from rest_framework.response import Response
from rest_framework import status


class BookList(APIView):
    def get(self, request):
        books = Book.objects.all() # complex data
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)
    

class BookCreate(APIView):
    def post(self, request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class BookDetail(APIView):
    def get_book_by_pk(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except:
            return Response({
                'error': 'Does not exist'
            }, status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    
    def put(self, request, pk):
        book = self.get_book_by_pk(pk)
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        book = self.get_book_by_pk(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)