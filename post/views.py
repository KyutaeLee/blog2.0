from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post/list.html', {'posts':posts})

class UploadView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['photo', 'text']
    template_name = 'post/upload.html'

    def form_valid(self, form):
        form.instance.author_id = self.request.user.id
        if form.is_valid():
            form.instance.save()
            return redirect('/')
        else :
            return self.render_to_response({'form':form})


class PostUpdateView(UpdateView):
    model = Post
    fields = ['photo', 'text']
    template_name = 'post/upload.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


