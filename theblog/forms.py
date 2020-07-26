from django import forms
from .models import Post, Category, Comment

#choices = [('Coding', 'Coding'), ('Sports', 'Sports'), ('Comedy', 'Comedy')]
choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body', 'snippet', 'header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Put Your Title Here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Put Your Title-Tag Here'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'elder', 'type':'hidden'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'Put Your Post Here'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put Your Snippet For Your Article'}),

        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body', 'snippet','header_image')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Hellow'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'snippet': forms.TextInput(attrs={'class': 'form-control'}),

        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','value':'', 'id':'holder', 'type':'hidden'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
           }