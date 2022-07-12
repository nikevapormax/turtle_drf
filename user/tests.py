from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from .models import User

class UserRegistrationTest(APITestCase):
    def test_registration(self):
        # user_view라는 name을 가진 url을 자동으로 가져와 변수에 저장해줌
        url = reverse("user_view")
        user_data = {
            "username" : "user10",
            "fullname" : "user10",
            "email" : "user10@naver.com",
            "password" : "1010"
        }
        
        # client는 APITestCase에서 자동으로 생성해준다.
        # client를 이용해서 post를 보내고, 아래의 url로 user_data를 보내주고 결과를 response에 담아준다.
        response = self.client.post(url, user_data)
        # 우리가 views.py의 회원가입 부분의 Response에 값을 담아놓았기 때문에 프린트를 찍으면 어디서 에러가 났는지 알 수 있음
        # print(response.data)
        
        self.assertEqual(response.status_code, 200)
        
        
class LoginUserTest(APITestCase):
    def setUp(self):
        self.data = {'username': 'user10', 'password': '1010'}
        self.user = User.objects.create_user('user10', '1010')
    
    # 로그인 테스트
    def test_login(self):
        response = self.client.post(reverse('token_obtain_pair'), self.data)
        self.assertEqual(response.status_code, 200 )
    
    # 회원정보 테스트
    def test_get_user_data(self):
        access_token = self.client.post(reverse('token_obtain_pair'), self.data).data['access']
        response = self.client.get(
            reverse('user_view'), 
            HTTP_AUTHORIZATION = f'Bearer {access_token}'
        )
        # self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['username'], self.data['username'])