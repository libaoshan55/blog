from django.shortcuts import render, get_object_or_404
import markdown
from comments.forms import CommentForm
from .models import Post, Category

"""
请使用下方的模板引擎方式。
def index(request):
    return HttpResponse("欢迎访问我的博客首页！")
"""

"""
请使用下方真正的首页视图函数
def index(request):
    return render(request, 'blog/index.html', context={
        'title': '我的博客首页',
        'welcome': '欢迎访问我的博客首页'
    })
"""


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})

def detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    # post.body = markdown.markdown(post.body,
    #                               extensions=[
    #                                   'markdown.extensions.extra'
    #                                   'markdown.extensions.codehilite'
    #                                   'markdown.extensions.toc'
    #                               ])
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',
                                      'markdown.extensions.codehilite',
                                      'markdown.extensions.toc',
                                  ])
    form=CommentForm()
    #获取这篇post下的所有评论
    comment_list=post.comment_set.all()
    # 将文章、表单、以及文章下的评论列表作为模板变量传给 detail.html 模板，以便渲染相应数据。
    context={'post':post,
             'form':form,
             'comment_list':comment_list
             }
    return render(request,'blog/detail.html',context=context)

#从数据库调用文章列表，筛选文章创建时间的年月
def archives(request,year,month):
    post_list=Post.objects.filter(
        created_time__year=year,
        created_time__month=month
    )
    # post_list = Post.objects.filter(
    #     created_time__year=year,
    #     created_time__month=month
    # ).order_by("-created_time")
    return render(request,'blog/index.html',context={'post_list':post_list})

def category(request,pk):
    #如果用户访问的分类不存在，则返回一个 404 错误页面以提示用户访问的资源不存在。
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'blog/index.html', context={'post_list': post_list})