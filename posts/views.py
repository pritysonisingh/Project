from django.shortcuts import render,redirect
from .forms import PostForm
from posts.models import Post
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

def post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return redirect('posts:post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})


class PostListView(ListView):
    model= Post

class PostDetailView(DetailView):
    model=Post

# def like(request,pk):
#     feed = get_object_or_404(Feed,pk=pk)
#     user= request.user
#     if request.method=='POST':
#         if feed.user_like.filter(id=user.id).exists():
#             feed.user_like.remove(user)
#             return render(request, 'index.html', {'form':form})
#         else:
#             feed.user_like.add(user)
#             return render(request, 'index.html', {'form':form})