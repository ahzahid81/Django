from django.http import HttpResponse

def home(request):
    return HttpResponse('''
                        
                         <a href = '/first_app/contact/'> Contact </a>
                         <br><a href = '/first_app/about/'> About </a>
                         <br><a href = '/second_app/courses/'> courses </a>
                         <br><a href = '/second_app/feedback/'> Feedback </a>
                        
                        ''')