from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

urlpatterns = [
    path('', views.UserView.as_view()),
    
    # simplejwt 에서 제공하는 기본 JWT 인증 / 로그인 대체
    path('api/token/', views.TurtleTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]