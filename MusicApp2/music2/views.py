from django.shortcuts import render

def index (request):
    return render (request,'music2/index.html')
