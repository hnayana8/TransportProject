from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
# from django.contrib import messages
from .models import newuser,driver,Booking,cargo,City,Course
# from .forms import CompanyForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')
def login(request):
        if request.method== 'POST':
            try:
                Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
                print("Username=",Userdetailes)
                request.session['Username']=Userdetailes.Username
                messages.success(request,"successfully login")
                return redirect('user_home')
            except newuser.DoesNotExist as e:   
                messages.error(request,"Username/ Password Invalied...!")
        return render(request, 'login.html')
   
   
    
    

def registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(Username=Username).exists():
            messages.warning(request,'Username is already exists')
            return redirect('registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('login')
    else:
        return render(request, 'registration.html')   

    # return render(request, 'registration.html')
def user_home(request):
    form=driver.objects.all()
    return render(request,'user_home.html',{'forms':form})


def user_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('index')

def about(request):
    return render(request,'about.html')

def pricing(request):
    return render(request,'pricing.html')

def driver_login(request):
        if request.method== 'POST':
            try:
                Userdetailes=driver.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
                print("Username=",Userdetailes)
                request.session['Username']=Userdetailes.Username
                messages.success(request,"successfully login")
                return redirect('driver_home')
            except newuser.DoesNotExist as e:   
                messages.error(request,"Username/ Password Invalied...!")
        return render(request, 'driver_login.html')


def driver_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']   
        dfname=request.POST['dfname']
        lname=request.POST['lname']
        address=request.POST['address']
        dcontact=request.POST['dcontact']
        lno=request.POST['lno']
        vno=request.POST['vno']
        email=request.POST['email']
        image=request.FILES['image']
        pday=request.POST['pday']
        phours=request.POST['phours']
        pmonth=request.POST['pmonth']       
        pass1=request.POST['pass1']
        # gender=request.POST['gender']   , gender=gender
        if driver.objects.filter(Username=Username).exists():
            messages.warning(request,'username is already exists')
            return redirect('registration')
        else:
        
            driver(Username=Username,dfname=dfname, lname=lname, address=address,dcontact=dcontact,lno=lno,vno=vno,email=email,image=image,pday=pday,phours=phours,pmonth=pmonth, pass1=pass1).save()
            messages.success(request, 'The new user '+request.POST['dfname']+ " IS saved successfully..!")
            return redirect('driver_login')
    else:
        return render(request,'driver_registration.html')

def driver_home(request):
    return render(request,'driver_home.html')

def driver_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('index')

def admin_login(request):
        if request.method== 'POST':
            try:
                Userdetailes=newuser.objects.get(Username=request.POST['Username'], pass1=request.POST['pass1'])
                print("Username=",Userdetailes)
                request.session['Username']=Userdetailes.Username
                messages.success(request,"successfully login")
                return redirect('admin_home')
            except newuser.DoesNotExist as e:   
                messages.error(request,"Username/ Password Invalied...!")
        return render(request,'admin_login.html')
    

def admin_registration(request):
    if request.method == 'POST':
        Username=request.POST['Username']
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if newuser.objects.filter(email=email).exists():
            messages.warning(request,'email is already exists')
            return redirect('registration')
        else:
            newuser(Username=Username, fname=fname, lname=lname, email=email, pass1=pass1, pass2=pass2).save()
            messages.success(request, 'The new user '+request.POST['Username']+ " IS saved successfully..!")
            return redirect('login')
    else:
        # return render(request, 'registration.html')  
        return render(request,'admin_registration.html')


def admin_logout(request):
    # logout(request)
    messages.success(request,"successfully logout..!")
    return redirect('index')

def admin_home(request):
    return render(request,'admin_home.html')

def views_user(request):
    form=newuser.objects.all()
    return render(request, 'views_user.html', {'forms':form})

def views_drivers(request):
    form=driver.objects.all()
    return render(request, 'views_drivers.html', {'forms':form})


def book_car(request):
    city=City.objects.all()
    if request.method == 'POST':
        ufname=request.POST['ufname']
        ulname=request.POST['ulname']
        uaddress=request.POST['uaddress']
        uphone=request.POST['uphone']
        weightSelect=request.POST['weightSelect']
        priceSelect=request.POST['priceSelect']
        # gender=request.POST['gender']    ,gender=gender
        Booking(ufname=ufname, ulname=ulname, uaddress=uaddress,uphone=uphone,weightSelect=weightSelect,priceSelect=priceSelect).save()
        messages.success(request,"successfully booking")
        return redirect('user_home')
    else:  
        context={
            'citys':'citys',
            
          
        }
    return render (request,'booking_car.html',context)
    
    
   
     
        
        
       

    

def search(request):
    query_name=request.GET['query']
    form=driver.objects.filter(address__icontains=query_name)
    return render (request, 'search.html',{'forms':form})

   

def views_bookings(request):
    hops=Booking.objects.all()
    return render(request, 'view_bookings.html', {'hop':hops})



def delete_data(request, id):
    pi= Booking.objects.get(pk=id)
    pi.delete()
    return redirect('views_bookings')
    





def order(request):
    return render(request, 'order.html')


def cargo_details(request):
    if request.method == 'POST':
        weight=request.POST['weight']
        price=request.POST['price']
        cargo(weight=weight,price=price).save()
    return render(request,'cargo_details.html')


def demo(request):
    citys = City.objects.all()
    d = {'citys': citys}
    return render(request,'demo.html',d)

def load_courses(request):
    city_id = request.GET.get('city')
    courses = Course.objects.filter(city_id=city_id).order_by('name')
    return render(request, 'courses_dropdown_list_options.html', {'courses': courses})