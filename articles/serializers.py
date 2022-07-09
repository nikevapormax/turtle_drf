from rest_framework import serializers
from .models import Article as ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    
    def get_username(self, obj):
        return obj.user.username
    class Meta:
        model = ArticleModel
        fields = ['user', 'username', 'title', 'content', 'image', 'created_at', 'updated_at',]
 

