from django.db import models

# Create your models here.

class Company(models.Model):
    code = models.CharField(max_length=20, primary_key=True)        # 기업코드
    company = models.CharField(max_length=40)                       # 기업명
    last_update = models.DateField()                                # 데이터 업데이트 날짜
    
    # 관리자 화면에서 기업명이 보여지도록 출력하는 함수
    def __str__(self):
        return self.company