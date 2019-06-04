from django.shortcuts import render

def index (request):
    return render (request,'music2/index.html')

def contact(request):

    return render(request, 'mysic2/basic.html', {'values':['jgkfjgkfjgfjkgf','456787654']})
