
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(response):
    return HttpResponse ('''
                         
                         <h1> This is courses Page </h1>
                        <br> <a href = '/first_app/about/'> About </a>
                        <br> <a href = '/first_app/contact/'> Contact </a>
                        <br> <a href = '/second_app/feedback/'> Feedback </a>
                        <br> <a href ='/'> Home </a>
                         
                         ''')

def feedback(response):
    return HttpResponse ('''
                         
                         <h1> This is courses Page </h1>
                        <br> <a href = '/first_app/about/'> About </a>
                        <br> <a href = '/first_app/contact/'> Contact </a>
                        <br> <a href = '/second_app/courses/'> courses </a>
                        <br> <a href ='/'> Home </a>
                         ''')