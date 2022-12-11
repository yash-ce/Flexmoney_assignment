from django.db import models

class Application_form(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    phone=models.CharField(max_length=150)
    birth_date=models.DateField()
    geder=models.CharField(max_length=150,)
    payment_month=models.CharField(max_length=150)
    payment_year=models.CharField(max_length=150)
    batch_time=models.CharField(max_length=150)
    Otp=models.CharField(max_length=150)

    def __str__(self) -> str:
        return ( self.email)

class Alredy_registered_user(models.Model):
    email=models.EmailField(max_length=254)
    payment_month=models.CharField(max_length=150)
    payment_year=models.CharField(max_length=150)
    batch_time=models.CharField(max_length=150)
    Otp=models.CharField(max_length=150,null=True)

    def __str__(self) -> str:
        return ( self.email)

class Payment(models.Model):
    Upi_id = models.CharField(max_length=50)
    payment_Img = models.ImageField(upload_to='images/')
    Otp = models.CharField(max_length=50)

    def __str__(self) -> str:
        return (self.Upi_id)

