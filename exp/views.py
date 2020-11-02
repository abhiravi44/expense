from django.shortcuts import render,redirect
from . models import *
from . forms import *
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')


def register1(request):
    if request.method=='POST':
        f=StaffForm(request.POST)
        print(f)
        if f.is_valid():
            print(f)
            f.save()
            return redirect('/index/')
    else:
        f=StaffForm()
    
    
    return render(request,'register1.html',{'f':f})

def login1(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            form=login(request,user)
            return render(request,'expense.html')
        else:
            form=AuthenticationForm()
            messages.info(request,f' Account does not exists !!!')
        
    else:
        form=AuthenticationForm()
        
    return render(request,'login1.html',{'form':form})    

def logout1(request):
    logout(request)
    return redirect('/index/')

def allrecord(request):
    data=record.objects.all()
    context={'data':data}
    return render(request,'Allrecord.html',context)

def register(request):
    if request.method=='POST':
        form=ListForm(request.POST,request.FILES)
        if form.is_valid():
            print(form)
            user = form.save()
            return redirect('/index/')
    else:
        form=ListForm()
        context={'form':form}
    return render(request,'user_reg.html',context)

def saverec(request):
    if request.method=='POST':
        form=RecordForm(request.POST)
        if form.is_valid():
            db=record()
            now=datetime.now()
            year=now.strftime('%Y')
            month=now.strftime('%m')
            day=now.strftime("%d")
            'time=now.strftime("%H:%M:%S")'
            date_time=now.strftime('%Y-%m-%d')
            db.Date=date_time
            db.Description=form.cleaned_data['Description']
            db.Category=form.cleaned_data['Category']
            db.Amount=form.cleaned_data['Amount']
            db.User=request.user
            db.save()            
            return redirect('/index/')
    else:
        form=RecordForm()
        context={'form':form}
    return render(request,'enterrec.html',context)

def getreportbycategory(request):
    if request.method=='POST':
        category=request.POST['category']
        details=record.objects.filter(Category=category)
        sums=sum([a.Amount for a in details])
        context={'details':details,'sums':sums}
        return render(request,'getreport.html',context)
    else:
        return render(request,'getreport.html')
    return render(request,'getreport.html')

def getreportbydate(request):
    if request.method=='POST':
        date1=request.POST.get('date1')
        date2=request.POST.get('date2')
        print(date1,date2)
        date_data=record.objects.filter(Date__range=[date1,date2])
        print(date_data)
        sums=sum([a.Amount for a in date_data])
        context={'date_data':date_data,'sums':sums}

        return render(request,'daterport.html',context)
    else:
        return render(request,'daterport.html')
    return render(request,'daterport.html')
        
                


def userlogin(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        password=request.POST.get('password')
        if user_model.objects.filter(Username=uname,Password=password).exists():
            data=user_model.objects.filter(Username=uname,Password=password)
            for a in data:
                usertype=a.Category
                if usertype=='Admin':
                    request.session['username']=uname
                    request.session['password']=password
                    return render(request,'expense.html')
                elif usertype=='User':
                    request.session['username']=uname
                    request.session['password']=password
                    return render(request,'expense.html')
        else:
            return HttpResponse('<h4>User not Found!!!</h4>')
    return render(request,'login.html')
                

