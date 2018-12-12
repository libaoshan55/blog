from django.shortcuts import render,get_object_or_404,redirect
from blog.models import  Post

#from .models import Comment
from .models import Comment
from .forms import CommentForm

# Create your views here.

def post_comment(request,post_pk):
    # �Ȼ�ȡ�����۵����£���Ϊ������Ҫ�����ۺͱ����۵����¹���������
    # ��������ʹ���� Django �ṩ��һ����ݺ��� get_object_or_404��
    # ��������������ǵ���ȡ�����£�Post������ʱ�����ȡ�����򷵻� 404 ҳ����û���
    #����POST��post_pk�����ﴫ�����ģ�
    post=get_object_or_404(Post,pk=post_pk)
    # �û��ύ�����ݴ��� request.POST �У�����һ�����ֵ����
    # ����������Щ���ݹ����� CommentForm ��ʵ�������� Django �ı��������ˡ�
    #request��������ķ�ʽ����������ݣ�request.POST���������������
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # ������ form.is_valid() ����ʱ��Django �Զ������Ǽ����������Ƿ���ϸ�ʽҪ��
        if form.is_valid():
            # ��鵽�����ǺϷ��ģ����ñ��� save �����������ݵ����ݿ⣬
            # commit=False �������ǽ������ñ����������� Comment ģ�����ʵ���������������������ݵ����ݿ⡣
            comment= form.save(commit=False)

            # �����ۺͱ����۵����¹���������
            comment.post=post

            # ���ս��������ݱ�������ݿ⣬����ģ��ʵ���� save ����
            comment.save()

            # �ض��� post ������ҳ��ʵ���ϵ� redirect ��������һ��ģ�͵�ʵ��ʱ������������ģ��ʵ���� get_absolute_url ������
            # Ȼ���ض��� get_absolute_url �������ص� URL��
            return redirect(post)
        else:
            # ��鵽���ݲ��Ϸ���������Ⱦ����ҳ��������Ⱦ���Ĵ���
            # ������Ǵ�������ģ������� detail.html��
            # һ�������£�Post����һ���������б�һ���Ǳ� form
            # ע�����������õ��� post.comment_set.all() ������
            # ����÷��е������� Post.objects.all()
            # �������ǻ�ȡ��ƪ post �µĵ�ȫ�����ۣ�
            # ��Ϊ Post �� Comment �� ForeignKey �����ģ�
            # ���ʹ�� post.comment_set.all() �����ѯȫ�����ۡ�
            # �����뿴����Ľ��⡣
            #post.comment_set.all()�ȼ���comment.objects.filter(post=post)
            comment_list=post.comment_set.all()
            context={'post':post,
                     'form':form,
                     'comment_list':comment_list
            }
    # ���� post ����˵���û�û���ύ���ݣ��ض�����������ҳ��
    return redirect(post)
