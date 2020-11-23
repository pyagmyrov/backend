from rest_framework import serializers
from core import models

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserProfile
        
        fields = ('id','email','name','password','is_staff', 'phone_Num','Welayat','Shaher')
        extra_kwargs = {
            'password':{
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }
        
    def create(self,validated_data):
        user = models.UserProfile.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password'],
            is_staff = validated_data['is_staff'],
        )

        return user

class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Tasks
        fields = ('id','user_profile','Yuk_Ulaglar','Yorute_Tehnikalar','niredenWelayat','niredenShaher','niraWelayat','niraShaher','hachan','created_on')
        extra_kwargs = {
            'user_profile': {
                'read_only':True 
            }
        }

class AddCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Car
        fields = ('id','user_profile','created_on','car_type', 'Yuk_Ulaglar', 'Yorute_Tehnikalar')
        extra_kwargs = {
            'user_profile': {
                'read_only':True 
            }
        }



