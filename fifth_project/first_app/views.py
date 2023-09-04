from django.shortcuts import render
from . forms import contactForm

def home(request):
    return render(request, './first_app/home.html')

def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('userName')
        email = request.POST.get('userEmail')
        select = request.POST.get('select')
        return render(request, './first_app/about.html', {'name' : name, 'email' : email, 'select': select })
    else:
        return render(request, './first_app/about.html')

def submit_form(request):
    return render(request, './first_app/form.html')

def DjangoForm(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        
        if form.is_valid():
           file = form.cleaned_data['file']
           with open('./first_app/upload/' + file.name, 'wb+') as destination:
               for chunck in file.chunks():
                   destination.write(chunck)
           print(form.cleaned_data)
        return render(request, './first_app/django_form.html', {'form':form })
    else:
        form = contactForm()
        return render(request, './first_app/django_form.html', {'form':form })
        
# Create your views here.
