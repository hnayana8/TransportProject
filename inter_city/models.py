from django.db import models

# Create your models here.

class newuser(models.Model):
    Username=models.CharField(max_length=80)
    fname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    email=models.EmailField(max_length=90)
    pass1=models.CharField(max_length=90)
    pass2=models.CharField(max_length=90)
    

class driver(models.Model):
    boolChoice = (
        ("M","Male"),("F","Female")
        )
    Username=models.CharField(max_length=80,default=0)
    dfname=models.CharField(max_length=89)
    lname=models.CharField(max_length=88)
    address= models.CharField(max_length=540)
    dcontact=models.CharField(max_length=120)
    lno=models.CharField(max_length=120)
    vno=models.CharField(max_length=120)
    email=models.EmailField(max_length=90)
    image = models.ImageField(upload_to='images',default="")  
    pday=models.CharField(max_length=120)
    phours=models.CharField(max_length=120)
    pmonth=models.CharField(max_length=120)
    pass1=models.CharField(max_length=90)
    gender = models.CharField(max_length = 1,choices=boolChoice)
 
class Booking(models.Model):
    # driver_name = models.ForeignKey(driver, on_delete=models.CASCADE,default="")
    boolChoice = (
        ("M","Male"),("F","Female")
        )
    
    SEMESTER_CHOICES = (
        ("1", "per day"),
        ("2", "per hours"),
        ("3", "per month"),
        # ("4", "Patient Transport Vehicle"),
        # ("5", "Air Ambulance"),
     
        )
    ufname=models.CharField(max_length=89)
    ulname=models.CharField(max_length=88)
    uaddress= models.CharField(max_length=540)
    uphone=models.CharField(max_length=120)
    weightSelect=models.CharField(max_length=12,null='True',default=0)
    priceSelect=models.CharField(max_length=12,default=0)
    # city = models.ForeignKey(driver, on_delete=models.CASCADE,default="")
    # course=models.ForeignKey(driver, on_delete=models.CASCADE,default="")  
    gender = models.CharField(max_length = 1,choices=boolChoice) 


class cargo(models.Model):
    weight=models.CharField(max_length=120)
    price=models.CharField(max_length=20)

class City(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Course(models.Model):
    city = models.ForeignKey(City,on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name