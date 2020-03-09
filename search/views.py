from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'search/home.html')


def search(request):
    return render(request, 'search/search.html')
