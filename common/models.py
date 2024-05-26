from django.db import models
from django.contrib.auth.models import (User, BaseUserManager, AbstractBaseUser)

"""
 * MODEL No. 1
 * MODEL Name : User  ##테이블 이름
"""

# User 생성을 위해 사용되는 헬퍼
class UserManager(BaseUserManager): 
    
    # 회원 생성
    def create_user(self, username, name, phone, email, flag, verifyCode, password=None, **extra_fields):
    
        if not username:      # 모든 요소들은 필수로 입력되어야 함
            raise ValueError('Must have username')
        
        if not name:
            raise ValueError('Must have name')
        
        if not phone:
            raise ValueError('Must have phone number')
        
        if not email:
            raise ValueError('Must have email')
        
        if not flag:
            raise ValueError('Must have flag')
        
        if not verifyCode:
            raise ValueError('Must have verification code')
        
        user = self.model(
            username = username,
            name = name,
            phone = phone,
            email = self.normalize_email(email),
            flag = flag,
            verifyCode = verifyCode,
        )

        user.set_password(password)     # 비밀번호 평문으로 저장하지 않음
        user.save(using=self._db)
        return user

    # 관리자 생성
    def create_superuser(self, username, name, phone, email, flag, verifyCode, password=None, **extra_fields):
        user = self.create_user(
            username = username,
            name = name,
            password = password,
            phone = phone,
            email = self.normalize_email(email),
            flag = flag,
            verifyCode = verifyCode,
        )

        user.is_admin = True
        user.save(using=self._db)
        return user
        

# 회원 기능을 위해 사용할 실제 모델
class User(AbstractBaseUser):   
    username = models.CharField(max_length=30, null=False, unique=True, primary_key=True)
    name = models.CharField(max_length=30, null=False)
    # password = models.CharField(max_length=256, null=False)
    phone = models.CharField(max_length=13, null=True)
    email = models.EmailField(max_length=30, null=False, unique=True)
    flag = models.IntegerField(null=False)
    verifyCode = models.CharField(max_length=30, null=False, default='0')

    # Django User 모델의 필수 필드
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name', 'phone', 'email', 'flag', 'verifyCode']  # 반드시 입력되어야 하는 필드

    def __str__(self):
        return self.username
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
    
    # True 반환 시 관리자 페이지에 로그인 가능
    @property
    def is_staff(self):         
        return self.is_admin

    class Meta:
        # db_table = 'common_user'
        managed = True

        constraints = [     # username과 이메일이 사용자 간 중복될 수 없도록 설정
            models.UniqueConstraint(
                fields=['username', 'email'],
                name='unique_information'
            ),
        ]
