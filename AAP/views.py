from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm

from AAP.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'body','title']

def post_list(request, template_name='books_fbv/post_list.html'):
    post = Post.objects.all()
    data = {}
    data['object_list'] = post
    return render(request, template_name, data)

def post_create(request, template_name='books_fbv/post_form.html'):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('books_fbv:post_list')
    return render(request, template_name, {'form':form})

def post_update(request, pk, template_name='books_fbv/post_form.html'):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        return redirect('books_fbv:post_list')
    return render(request, template_name, {'form':form})

def post_delete(request, pk, template_name='books_fbv/post_confirm_delete.html'):
    post = get_object_or_404(Post, pk=pk)    
    if request.method=='POST':
        post.delete()
        return redirect('books_fbv:post_list')
    return render(request, template_name, {'object':post})
# Create your views here.
