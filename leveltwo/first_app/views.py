from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_dict = {'text_inject': 'WASSUP FUCKERS'}
    return render(request, 'first_app/index.html', context=my_dict)
