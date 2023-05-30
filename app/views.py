from django.shortcuts import render


# Create your views here.
def wish(request):
    d={'name':'khushboo'}
    return render(request,'wish.html',context=d)
