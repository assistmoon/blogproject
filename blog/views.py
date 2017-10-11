from django.http import HttpResponse
from django.shortcuts import render
from .models import Post

def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={
            'title':'Black &amp; White',
            'welcome':'欢迎访问我的博客首页，啊哈哈！',
            'post_list':post_list
        })
