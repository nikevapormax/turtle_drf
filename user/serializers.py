from rest_framework import serializers
from .models import User as UserModel

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields  = ['username','password','email','fullname','join_date',]
        
        extra_kwargs = {
            # 쓰기 전용(write_only)으로 설정된 필드는 직렬화된 데이터에서 보여지지 않는다.
            'password': {'write_only': True},
        }
        
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
        
        
