from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class TurtleTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # token 가져오기
        token = super().get_token(user)
        
        # 사용자 지정 커스텀 클레임 설정
        token['id'] = user.id
        token['username'] = user.username
        token['email'] = user.email
        
        return token