from django.shortcuts import render
from django.http import HttpResponse

from .models import Company
# Create your views here.
def index(request):
    # return HttpResponse("안녕하세요. 기본 페이지입니다.")
    company_list = Company.objects.all()        # Company 모델에 있는 정보 모두 로드
    context = {'company_list': company_list}    # company_list의 정보를 context에 담는다
    
    return render(request, 'stock/index.html', context)