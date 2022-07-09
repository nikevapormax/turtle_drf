from django.contrib import admin
from .models import User as UserModel
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'fullname', 'email') # admin 페이지의 Users에 나오는 목록
    list_display_links = ('username', )                     # username에 링크가 걸려 누르면 해당 user의 상세정보를 볼 수 있음
    list_filter = ('username', )                           # filter에 username을 보여줌
    search_fields = ('username', 'email', )                # 검색에 사용할 요소 선택
    
    # user의 상세 정보에 나타낼 필드를 설정
    fieldsets = (
        ('info', {'fields' : ('username', 'password', 'email', 'fullname', 'join_date', )}),
        ('permissions', {'fields': ('is_admin', 'is_active', )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('username', 'fullname', 'password1', 'password2',)} # password1과 password2가 있어야 비밀번호를 해싱해주는 칸이 나옴
         ),
    )
    
    filter_horizontal = []
    
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ('username', 'join_date', )
        else:
            return ('join_date', )    
    
    
admin.site.register(UserModel, UserAdmin)
