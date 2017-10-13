from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post

from .models import Comment
from .forms import CommentForm

def post_comment(request,post_pk):
    # 先获取被评论的文章，因为后面需要把评论和被评论的文章关联起来
    # 这里使用Django停工的快捷函数 get_list_or_404获取文章
    post = get_object_or_404(Post,pk=post_pk)

    # HTTP请求有get和post两种，一般用户通过表单提交数据都是用post
    if request.method == 'POST':
        # 用户提交的数据存在request.POST中,利用数据构造CommentForm的实例
        form = CommentForm(request.POST)

        # 当调用from.is_valid()方法时,Django自动帮我们检查表单的数据是否符合格式要求
        if form.is_valid():
            # 检查数据是否合法,调用表单的save方法保存数据到数据库
            # commit=False的作用是仅仅利用表单的数据生成Comment模型的实例,但不保存评论到数据库
            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来
            comment.post = post

            # 最终将评论数据保存进数据库
            comment.save()

            # 重定向到post的详情页,实际上当redirect函数接收一个模型的实例时,他会调用这个模型实例的get_absolute_url方法,然后重定向到返回的URL
            return redirect(post)
        else:
            # 检查到数据不合法,重新渲染详情页,并且渲染表单的错误,因此我们传了三个模板变量给detial.html
            # 一个是文章Post,一个是评论列表,一个是表单form
            # 注意这里我们用到了post.comment_set.all()方法,类似于Post.object.all()获取post下的全部评论
            # 因为Post和Comment是ForeignKey关联,所以使用post.comment_set.all()方向查询全部评论
            comment_list = post.comment_set.all()
            context = {'Post':post,
                    'form':form,
                    'comment_list':comment_list
                    }
            return render(request,'blog/detial.html',context=context)
        # 不是post请求,说明用户没有提交数据,重定向到文章详情页
        return redirect(post)
