from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from user.serializers import UserSignupSerializer

# Create your views here.
class UserView(APIView):
    
    # 회원정보 조회
    def get(self, request):
        # 현재는 회원가입 시리얼라이저만 있기 때문에 아래와 같이 작성
        return Response(UserSignupSerializer(request.user).data, status=status.HTTP_200_OK)
    
    # 회원가입
    def post(self, request):
        return Response({'msg' : 'post success!!'})
    
    # 회원정보 수정
    def put(self, request):
        return Response({'msg' : 'put success!!'})
    
    # 회원탈퇴
    def delete(self, request):
        return Response({'msg' : 'delete success!!'})