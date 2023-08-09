from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(request):
    return HttpResponse ('''
                         
                         <h1> This is Contact Page </h1>
                        <br> <a href = '/first_app/about/'> About </a>
                        <br> <a href = '/second_app/courses/'> courses </a>
                        <br> <a href = '/second_app/feedback/'> Feedback </a>
                        <br> <a href ='/'> Home </a> 
                         ''')

def about(request):
    return HttpResponse ('''
                         
                         <h1> This is about Page </h1>
                        <br> <a href = '/first_app/contact/'> Contact </a>
                        <br> <a href = '/second_app/courses/'> courses </a>
                        <br> <a href = '/second_app/feedback/'> Feedback </a>
                        <br> <a href ='/'> Home </a>
                         ''')