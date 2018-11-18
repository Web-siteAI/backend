from django.shortcuts import render


def register(request):
    return render(request, "EntryApp/entry.html")

# Create your views here.
