from django.shortcuts import render
from .models import article
from django.db.models import Q
# Create your views here.


def index(request):
    data = article.objects.all()
    
    if request.method == 'POST':
         search = request.POST.get('search')
         
        #  data = article.objects.filter(name__icontains=search)
         data = article.objects.filter(Q(title__icontains = search)|Q(desc__icontains = search))
         print(search)
    context={
        'res' : data
    }
    return render(request,'index.html',context)

def display(request,pk):
     data1 = article.objects.get(id=pk)
     context = {
         'data1' : data1
     }   
     return render(request,'singledetails.html',context)

def about(request):
    return render(request,'about.html')