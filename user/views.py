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
        serialized_data = UserSignupSerializer(data=request.data)
        
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        
        # 아래와 같이 errors를 프론트에 보여주는 것은 좋지 않은 방식이다. 현재는 내가 못하기 때문에 어디가 문제인지 바로 알 수 있어 좋지만
        # 나중에 개발이 끝나고 나서는 그냥 '회원가입 실패'와 같은 메세지를 프론트로 보내주는 것이 더 좋을 것이다!
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # 회원정보 수정
    def put(self, request):
        return Response({'msg' : 'put success!!'})
    
    # 회원탈퇴
    def delete(self, request):
        return Response({'msg' : 'delete success!!'})