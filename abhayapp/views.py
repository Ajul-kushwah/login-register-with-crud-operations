from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Account,TribalYouth,Company
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    account = Account.objects.all()
    context={'accounts':account}
    return render(request,'abhayapp/index.html',context)

def about(request):
    return render(request,'abhayapp/about.html')

def add(request):
    account=Account.objects.all()
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        address=request.POST['address']

        add_data=Account(firstname=firstname,lastname=lastname,address=address)
        add_data.save()
        return redirect('/')

def edit(request,pk):
    account_by_id=Account.objects.get(id=pk)
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        add=request.POST['address']

        account_by_id.firstname=fname
        account_by_id.lastname=lname
        account_by_id.address=add

        account_by_id.save()
        return redirect('/')
    else:
        account_by_id = Account.objects.get(id=pk)
        context={'accounts':account_by_id}
        return render(request,'abhayapp/edit.html',context)

def delete(request,pk):
    account_by_id=Account.objects.get(id=pk)
    account_by_id.delete()
    return redirect('/')





def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user =auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('profile')
        else:
            messages.error(request,'Invalid username and password')
           # messages.info(request,'Invalid username and password')
            return redirect('login')
    else:
        return render(request,'abhayapp/login.html')



def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        category = request.POST['category']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken ..')
                print('username already exist ..')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email already exist..')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email)
                user.save()
                print('user created ')
                if category == 'youth-user':
                    youth = TribalYouth(user=user,username=username, email=email, category=category)
                    youth.save()
                    return redirect('login')
                else:
                    company = Company(user=user,company_username=username, company_email=email,
                                      category=category)
                    company.save()
                    return redirect('login')
        else:
            print('password not matching...')
            return redirect('register')

    else:
        return render(request,'abhayapp/signup.html')



@login_required
def profile(request):
    #user=User.objects.get(user=request.user)

    youth=TribalYouth.objects.get(user=request.user)
    context1={'account':youth}
    #
    # company = Company.objects.get(user=request.user)
    # context = {'account': company}
    #
    # if youth.category=='youth-user':
    #     return render(request,'abhayapp/userprofile.html',context1)
    # else:
    #     return render(request, 'abhayapp/companyprofile.html', context)

    return render(request, 'abhayapp/userprofile.html', context1)