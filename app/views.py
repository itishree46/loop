from django.shortcuts import render

# Create your views here.
def loop(request):
    d={'name':'itishree','l':[10,20,30,49]}
    return render(request,'loop.html',d)
