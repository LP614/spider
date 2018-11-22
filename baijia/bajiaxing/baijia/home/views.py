from django.shortcuts import render
from home.models import Name
from django.core.paginator import Paginator
from baijia.settings import PAGE_NUMBER


def index(request):
    if request.method == 'GET':
        try:
            page_number = int(request.GET.get('page', 1))
        except:
            page_number = 1
        #获取所有信息
        data_names = Name.objects.all()
        paginator = Paginator(data_names, PAGE_NUMBER)
        page = paginator.page(page_number)
        return render(request, 'index.html',
                      {'page': page})
