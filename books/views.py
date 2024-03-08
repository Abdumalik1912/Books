from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BookSerializer, RequestSerializer
from .models import Book, Request
from rest_framework import permissions
from rest_framework import parsers


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.available_books.all()
    serializer_class = BookSerializer
    parser_classes = (parsers.MultiPartParser, parsers.FormParser)
    permission_classes = (permissions.IsAuthenticated, )


class RequestViewSet(viewsets.ModelViewSet):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    permission_classes = (permissions.IsAuthenticated, )


