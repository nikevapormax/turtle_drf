from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from user.models import User 

# 이미지 업로드
from django.test.client import MULTIPART_CONTENT, encode_multipart, BOUNDARY
from PIL import Image
import tempfile

def get_temporary_image(temp_file):
    size = (200, 200)
    color = (255, 0, 0, 0)
    image = Image.new('RGBA', size, color)
    image.save(temp_file, 'png')
    
    return temp_file


class ArticleCreateTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user_data = {'username': 'user10', 'password': '1010'}
        cls.article_data = {'title' : 'test title', 'content' : 'test content'}
        cls.user = User.objects.create_user('user10', '1010')
        
    def setUp(self):
        self.access_token = self.client.post(reverse('token_obtain_pair'), self.user_data).data['access']
        
    # 로그인하지 않았을 경우 게시글 작성
    def test_fail_if_not_logged_in(self):
        url = reverse('article_view')
        response = self.client.post(url, self.article_data)
        self.assertEqual(response.status_code, 401)

    # 게시글 작성(이미지 x)
    def test_create_article(self):
        response = self.client.post(
            path=reverse('article_view'),
            data=self.article_data,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
       
        # self.assertEqual(response.data["msg"], '글 작성 완료')
        self.assertEqual(response.status_code, 200)
        
    # 게시글 작성(이미지 o)
    def test_create_article_with_image(self):
        # 임시 이미지파일 생성
        temp_file = tempfile.NamedTemporaryFile()
        temp_file.name = 'image.png'   
        image_file = get_temporary_image(temp_file)
        # 그냥 파일이기 때문에 첫 번째 프레임을 받아옴
        image_file.seek(0)
        self.article_data["image"] = image_file
        
        # 전송
        response = self.client.post(
            path=reverse('article_view'),
            data=encode_multipart(data=self.article_data, boundary=BOUNDARY),
            content_type=MULTIPART_CONTENT,
            HTTP_AUTHORIZATION=f'Bearer {self.access_token}'
        )
        self.assertEqual(response.data["msg"], '글 작성 완료')