from rest_framework import serializers
from .models import Article as ArticleModel


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleModel
        fields = ['title', 'content', 'image', 'created_at', 'updated_at',]
 

