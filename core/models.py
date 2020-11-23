from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings
import uuid
import os

# Create your models here.

 

class UserProfileManager(BaseUserManager):
    def create_user(self, email, name, is_staff ,password = None, ):
        if not email:
            raise ValueError("Email hokman gerek")
        
        email = self.normalize_email(email)
        user = self.model(email=email, name=name, is_staff = is_staff)

        user.set_password(password)


        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,name, password):
        is_staff = True
        user = self.create_user(email,name, is_staff, password,)
        user.is_superuser = True
        user.save(using=self._db)
        
        return user
    
class City(models.Model):
    Welayatlar = [
       ('1', 'Balkan'),
       ('2', 'Ahal'),
       ('3', 'Mary'),
       ('4', 'Lebap'),
       ('5', 'Dashoguz'),
    ]
    Welayatlarr = ['Balkan','Ahal','Mary','Lebap','Dashoguz']
 
    Welayat = models.CharField(max_length=1, choices = Welayatlar)
    Etrap = models.CharField(max_length = 100)



    def __str__(self):
        return '%s | %s' % (self.Welayatlarr[ord(self.Welayat)-49], self.Etrap)

     
class Welayat(models.Model):
    welayat = models.CharField(max_length = 60)

    def __str__(self):
        return self.welayat


class UserProfile(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique = True)
    name = models.CharField(max_length=254)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)
    is_superuser = models.BooleanField(default = False)
    phone_Num = models.IntegerField(blank = True, null = True)
    fields = (('email', 'name', 'is_staff', 'is_superuser'),)
    created_on = models.DateTimeField(auto_now_add = True)

    Welayat = models.ManyToManyField(
        Welayat,
        blank=True
       )

    Shaher = models.ManyToManyField(
        City,
        blank=True
       )

    
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']
    
    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name
    
    def __str__(self):
        return self.email



class YukUlaglar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class TehnikiUlaglar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
   



class Tasks(models.Model):

    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
       )
    
    Yuk_Ulaglar= models.ForeignKey(
            YukUlaglar,
            on_delete = models.CASCADE
        )
    Yorute_Tehnikalar = models.ForeignKey(
            TehnikiUlaglar,
            on_delete = models.CASCADE
        )

    niredenWelayat = models.ForeignKey(
        Welayat,
        on_delete = models.CASCADE,
        related_name = 'nireden_Velayat',
        default=None
       )

    niredenShaher = models.ForeignKey(
        City,
        on_delete = models.CASCADE,
        related_name = 'nireden_Shaher',
        default=None
       )

    niraWelayat = models.ForeignKey(
        Welayat,
        on_delete = models.CASCADE,
        related_name = 'nira_Welayat',
        default=None
       )

    niraShaher = models.ForeignKey(
        City,
        on_delete = models.CASCADE,
        related_name = 'nira_Shaher',
        default=None,
       )

    hachan = models.DateTimeField(auto_now_add = False)

    created_on = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nireden


class Car(models.Model):
    user_profile = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete = models.CASCADE
       )

    car_types = [
       ('1','Yuk Ulaglar'),
       ('2','Yorute Tehnikalar'),
    ]
    created_on = models.DateTimeField(auto_now_add = True)
    car_type = models.CharField(max_length=1, choices = car_types)
    

    
    Yuk_Ulaglar= models.ForeignKey(
            YukUlaglar,
            on_delete = models.CASCADE
        )
    Yorute_Tehnikalar = models.ForeignKey(
            TehnikiUlaglar,
            on_delete = models.CASCADE
        )

    def __str__(self):
        return self.user_profile
    




