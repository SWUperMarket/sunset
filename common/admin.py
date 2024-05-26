from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .forms import UserChangeForm, UserCreationForm
from .models import User

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm          # 관리자 화면의 사용자 변경 폼
    add_form = UserCreationForm    # 관리자 화면의 사용자 추가 폼

    list_display = ('username', 'name', 'phone', 'email', 'flag', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('name', 'phone', 'email', 'flag',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('')}
        ),
    )
    
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)