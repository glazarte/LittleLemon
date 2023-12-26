from django.db import models

# Create your models here.

# class Menu(models.Model):
#     id = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     inventory = models.IntegerField()

#     def __str__(self):
#         return self.title

# class Booking(models.Model):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=255)
#     no_of_guests = models.IntegerField()
#     booking_date = models.DateTimeField()

#     def __str__(self):
#         return f"Booking #{self.id} - {self.name}"

# class MenuItem(models.Model):
#     # Your MenuItem model fields go here
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=8, decimal_places=2)

#     def __str__(self):
#         return self.name

# class Booking(models.Model):
#     first_name = models.CharField(max_length=200)
#     reservation_date = models.DateField()
#     reservation_slot = models.SmallIntegerField(default=10)

#     def __str__(self): 
#         return self.first_name

# class Menu(models.Model):
#    name = models.CharField(max_length=200) 
#    price = models.IntegerField(null=False) 
#    menu_item_description = models.TextField(max_length=1000, default='') 

#    def __str__(self):
#         return self.name
    
# class MenuItem(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.SmallIntegerField()

#     def get_item(self):
#         return f'{self.title} : {str(self.price)}'

from django.db import models

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=True, default=None)
    no_of_guests = models.IntegerField(default=0)
    bookingdate = models.DateTimeField()

    class Meta:
        db_table = "booking"

class Menu(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
    
    class Meta:
        db_table = "menu"
