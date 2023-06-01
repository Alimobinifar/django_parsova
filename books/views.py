from django.shortcuts import render
from books.models import *
from django.views import View


class Books(View):
    def get(self, request):
        qs = Book.objects.all()
        return render(request, "home.html/", context={"books":qs})