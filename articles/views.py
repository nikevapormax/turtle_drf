from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import Article as ArticleModel
from .serializers import ArticleSerializer


class ArticleView(APIView):
    
    def get(self, request):
        articles = ArticleModel.objects.all()
        serialized_data = ArticleSerializer(articles, many=True)
        
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        if not request.user.is_authenticated:
            return Response({'msg': '로그인해주세요'}, 401)
        
        user = request.user
        request = request.data.dict()
        request["user"] = user.id
        
        serialized_data = ArticleSerializer(data=request)
        
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_200_OK)
        
        return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)