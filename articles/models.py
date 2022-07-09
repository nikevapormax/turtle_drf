from django.db import models

class Article(models.Model):
    user = models.ForeignKey('user.User', verbose_name="작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=20)
    content = models.TextField("게시글 내용")
    image = models.ImageField("이미지", blank=True)
    created_at = models.DateTimeField("생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간",auto_now=True)
    
    class Meta:
        db_table = 'articles'
        
