from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, './first_app/home.html', {"name": "I am Rahim", "marks" : 86, "courses" : [
        {
            "id" : 1,
            "couses" : "C",
            "teacher" : "Rahim"
        },
        {
            "id" : 2,
            "couses" : "C++",
            "teacher" : "kahim"
        },
        {
            "id" : 3,
            "courses" : "python",
            "teacher" : "Fahim"
        },
    ]})

def about(request):
    return render(request, './first_app/about.html', {'author': 'galen maxwell'})
    
    
