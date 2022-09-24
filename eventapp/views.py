from multiprocessing import context
import os
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_home(request):
    return render(request,'user/userhome.html')

def load_user_signup(request):
    return render(request,'user/signup.html')

def load_user_login(request):
    return render(request,'user/login.html')

def load_admin_home(request):
    return render(request,'admin/adminhome.html')

def load_add_product(request):
    return render(request,'admin/addpdct.html')

def load_product_page(request):
    product=productmodel.objects.all()
    context={'product':product} #fisrt name= htmlpagename and variablename
    return render(request,'user/product.html',context)

def load_service_page(request):
    service=servicemodel.objects.all()
    context={'service':service} #fisrt name= htmlpagename and variablename
    return render(request,'user/service.html',context)

def load_view_product(request):
    product=productmodel.objects.all()
    context={'prdct':product}
    return render(request,'admin/viewproduct.html',context)

def load_add_service(request):
    return render(request,'admin/addservice.html')

def load_view_service(request):
    service=servicemodel.objects.all()
    context={'service':service}
    return render(request,'admin/viewservice.html',context)

def load_view_user(request):
    users=usermodel.objects.all()
    context={'users':users}
    return render(request,'admin/viewuser.html',context)

def load_profile_page(request):
    users=usermodel.objects.get(user=request.user)
    context={'users':users}
    return render(request,'user/profile.html',context)

def load_profile_edit(request):
    users=usermodel.objects.get(user=request.user)
    context={'users':users}
    return render(request,'user/useredit.html',context)

def load_view_book(request):
    products=bookmodel.objects.all()
    context={'products':products}
    return render(request,'admin/viewbook.html',context)

def load_add_book(request):
    return render(request,'user/book.html')

def user_signup(request):
    if request.method=='POST':
        fname=request.POST['firstname']
        lname=request.POST['lastname']
        uname=request.POST['username']
        address=request.POST['address']
        mail=request.POST['email']
        num=request.POST['number']
        password=request.POST['password']
        confmpassword=request.POST['confirmpassword']

        #photo

        photo=request.FILES.get('photo')

        if password==confmpassword:
            if User.objects.filter(username=uname).exists():
                messages.info(request,'This User Name Is Already Exist')
                return render('load_user_signup')
            
            elif User.objects.filter(email=mail).exists():
                messages.info(request,'This Email Is Alreay Exist')
                return redirect('load_user_signup')
            else:
                user=User.objects.create_user(first_name=fname,last_name=lname,username=uname,email=mail,password=password)
                user.save()
                messages.success(request,'Successfully Registred')
                print("success")

                data=User.objects.get(id=user.id)
                user_data=usermodel(user_address=address,user_number=num,user_Photo=photo,user=data)
                user_data.save()
                messages.success(request,'successfully ragistred')
                print("successed")
                return redirect('load_user_login')

        else:
            #message info
            print("Password Is Not Matching")
            return redirect('load_user_signup')
        return redirect('load_user_login')
    else:
        return render(request,'user/signup.html')


def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password) #variavlename and html name

        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('load_admin_home')
            else:
                login(request,user)
                auth.login(request,user)
                return redirect('user_home')
        else:
            return redirect('user_login')
    else:
        return redirect('user/login.html')

def user_logout(request):
    auth.logout(request)
    return redirect('user_home')

def userdelete(request,pk):
    user=usermodel.objects.get(id=pk)
    user.delete()
    return redirect('load_view_user')

# to edit user profile
def edit_user(request):
    if request.method == 'POST':
        member=usermodel.objects.get(user=request.user)
        member.user.first_name=request.POST['firstname']
        member.user.last_name=request.POST['lastname']
        member.user_address=request.POST['address']
        member.user_number=request.POST['number']
        # member.image=request.FILES['file']
        # if request .FILES.get('file') is not None:
            # if not member.image == "/static/images/blank-profile-picture-973460_640.png":
            #     os.remove(member.image.path)
            #     member.image="/static/images/blank-profile-picture-973460_640.png"
        member.save()
        member.user.save()
        return redirect('load_profile_page')
        
def addproduct(request):
    if request.method=='POST':
        pname=request.POST['productname']
        pprice=request.POST['productprice']
        photo=request.FILES.get('photo')
        

        pdata=productmodel(product_name=pname,product_price=pprice,product_photo=photo)
        pdata.save()
        return redirect('load_add_product')

def deleteproduct(request,pk):
    prdct=productmodel.objects.get(id=pk)
    prdct.delete()
    return redirect('load_view_product')

def editproduct(request,pk):
    if request.method=='POST':
        products=productmodel.objects.get(id=pk)
        products.product_name=request.POST['pname']
        products.product_price=request.POST['pprice']
        # products.product_photo=request.FILES['file']
        products.save()
        return redirect('load_view_product')
    products=productmodel.objects.get(id=pk)
    return render(request,'admin/productedit.html',{'products':products})

def addservice(request):
    if request.method=='POST':
        sname=request.POST['servicename']
        sprice=request.POST['serviceprice']
        sphoto=request.FILES.get('photo')

        sdata=servicemodel(Ser_Name=sname,Ser_Price=sprice,Ser_Photo=sphoto)
        sdata.save()
        return redirect('load_add_service')

def deleteservice(request,pk):
    service=servicemodel.objects.get(id=pk)
    service.delete()
    return redirect('load_view_service')

def editservice(request,pk):
    if request.method=='POST':
        service = servicemodel.objects.get(id=pk)
        service.Ser_Name = request.POST['pname']
        service.Ser_Price = request.POST['price']
        # products.image=request.FILES['file']
        service.save()
        return redirect('load_view_service')
    service=servicemodel.objects.get(id=pk)
    return render(request,'admin/serviceedit.html',{'service':service})
       
def addbook(request,pk):
    product = productmodel.objects.get(id=pk)
    user = usermodel.objects.get(user=request.user)
    data = bookmodel(prdct=product,user=request.user)
    data.save()
    return redirect('load_product_page')

def addbook(requset,pk):
    service=servicemodel.objects.get(id=pk)
    data = bookmodel(ser=service,user=requset.user)
    data.save()
    return redirect('load_service_page')

# to show product page
def showbook(request):
    products=bookmodel.objects.filter(user=request.user)
    context={'products':products}
    return render(request,'user/show.html',context)