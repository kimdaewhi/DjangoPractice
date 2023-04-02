from django.contrib import admin
#edit
from .models import Company     # 모델 추가

# Register your models here.

# 검색 기능 추가
class CompanyAdmin(admin.ModelAdmin):
    search_fields = ['company']
    
admin.site.register(Company, CompanyAdmin)    # 관리자모드에서 관리할 모델 추가해줌. 배열로 기능 추가 가능함