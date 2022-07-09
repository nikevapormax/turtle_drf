from rest_framework import serializers
from .models import User as UserModel

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields  = ['username','password','email','fullname','join_date',]
        
    def create(self, *args, **kwargs):
        user = super().create(*args, **kwargs) # 상속받은 값
        
        password = user.password
        user.set_password(password)    
        
        user.save()
        
        return user
    
    def update(self, *args, **kwargs):
        user = super().create(*args, **kwargs) # 상속받은 값
        
        password = user.password
        user.set_password(password)    
        
        user.save()
        
        return user
        
        
