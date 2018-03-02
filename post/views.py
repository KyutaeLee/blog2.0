from django.shortcuts import render
from .models import Post
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
def index(request):
    return render(request, 'post/index.html')

class UploadView(CreateView):
    model = Post
    fields = ['photo', 'text']
    template_name = 'post/upload.html'

class PostUpdateView(UpdateView):
    model = Post
    fields = ['photo', 'text']
    template_name = 'post/upload.html'

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'


