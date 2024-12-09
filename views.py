from django.shortcuts import render,redirect
"""from django.contrib.auth.forms import UserCreationForm"""
from django.contrib.auth import authenticate
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from myapp.models import contractor
from math import ceil

def homepage(request):
    return render (request,"home.html")

@login_required(login_url='login')
def categorypage(request):
    allProds = []
    catprods = contractor.objects.values('category','id')
    print(catprods)
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod= contractor.objects.filter(category=cat)
        n=len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    params= {'allProds':allProds}
    return render(request,"category.html",params)

def userregisterationpage(request):
    form=UserRegistrationForm()
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render (request,"userregisteration.html",{'form':form})

def userloginpage(request):
    if request.method == "POST":
        uname=request.POST['uname']
        pwd=request.POST['pwd']
        email=request.POST['email']
        user=authenticate(request,username=uname,password=pwd,email=email)
        if user is not None:
            login(request,user)
            return redirect('category')
    return render(request,'userlogin.html')

def userlogoutpage(request):
     logout(request)
     return redirect('login')

def contractorsearch(request):
    search_obj=request.GET.get('search')
    result=product.object.filter(category__contains=search_obj)
    if result:
        results=result
    else:
        results=False
    return render(request,'category.html',{'contractor':results})