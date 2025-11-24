from django.db import models

# Create your models here.


class login(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    usertype = models.CharField(max_length=100)

class fuel_provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login,on_delete=models.CASCADE)

class mechanic(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    certificate = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

class user(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=100)
    gender = models.CharField(max_length=100)
    place  = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)

class rating(models.Model):
    Rating = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class complaint(models.Model):
    date = models.CharField(max_length=100)
    reply  = models.CharField(max_length=100)
    reply_date = models.CharField(max_length=100)
    complaint = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class feedback(models.Model):
    date = models.CharField(max_length=100)
    feedback = models.CharField(max_length=100)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class fuel_price(models.Model):
    Fuel_Price = models.CharField(max_length=100)
    Fuel_Density = models.CharField(max_length=100)
    Fuel_type = models.CharField(max_length=100)
    FUEL_PROVIDER = models.ForeignKey(fuel_provider, on_delete=models.CASCADE)


class fuel_provider_request(models.Model):
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    Payment_Date = models.CharField(max_length=100)
    Payment_Status = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    FUEL_PRICE= models.ForeignKey(fuel_price, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class mechanic_request(models.Model):
    status = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    Payment_Date = models.CharField(max_length=100)
    longitude = models.CharField(max_length=100)
    latitude = models.CharField(max_length=100)
    Payment_Status = models.CharField(max_length=100)
    MECHANIC = models.ForeignKey(mechanic, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class chat(models.Model):
    chat = models.CharField(max_length=100)
    Date = models.CharField(max_length=100)
    Type = models.CharField(max_length=100)
    LOGIN = models.ForeignKey(login, on_delete=models.CASCADE)
    USER = models.ForeignKey(user, on_delete=models.CASCADE)

class service_amount(models.Model):
    Service_Details = models.CharField(max_length=100)
    amount=models.CharField(max_length=100)
    MECHANIC = models.ForeignKey(mechanic, on_delete=models.CASCADE)
