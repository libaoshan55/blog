#����
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #ָ������Ҫ��ʾ���ֶ�
        fields=['name','email','url','text']
