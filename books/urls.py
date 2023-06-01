from django.urls import path
from books.views import Books


urlpatterns=[
    path('home/',Books.as_view())
]