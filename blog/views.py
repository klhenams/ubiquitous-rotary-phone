from django.shortcuts import redirect
from django.shortcuts import render
from .forms import PostForm

def post_list(request):
    return render(request, 'blog/post_list.html', {})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
       else:
        form = PostForm(instance=post)

    return render(request, 'blog/post_edit.html', {'form': form})

