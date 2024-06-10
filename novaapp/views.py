from django.shortcuts import render


def index_view(request):
    return render(request, "novaapp/index.html")

def example_view(request):
    return render(request, "example.html")

def conclusion_view(request):
    return render(request, "conclusion.html")