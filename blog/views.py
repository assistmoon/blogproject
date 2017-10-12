# from django.http import HttpResponse
import markdown
from django.shortcuts import render,get_object_or_404
from .models import Post

def index(request):
    # return HttpResponse("欢迎访问我的博客首页！")
    post_list=Post.objects.all().order_by('-created_time')
    return render(request,'blog/index.html',context={
            'title':'Black &amp; White',
            'welcome':'欢迎访问我的博客首页，啊哈哈！',
            'post_list':post_list
        })

def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)

    #引入markdown
    post.body = markdown.markdown(post.body,
                                extensions=[
                                'markdown.extensions.extra',
                                'markdown.extensions.codehilite',
                                'markdown.extensions.toc',
                                ]
    )

    return render(request,'blog/detail.html',context={'post':post})
