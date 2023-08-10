from django.shortcuts import render

# Create your views here.

def contact(request):
    return render(request, './first_app/index.html',{"name": "I am Rahim",
    "marks": 86, "lst": [24,3,10,5], "blog" : "Lorem ipsum dolar"})