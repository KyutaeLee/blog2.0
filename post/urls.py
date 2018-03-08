from django.urls import path

from post.models import Post
from . import views
from django.views.generic.detail import DetailView

app_name = 'post'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('upload', views.UploadView.as_view(), name='post_create'),
    path('single/<int:pk>', DetailView.as_view(model=Post, template_name='post/detail.html'), name='post_detail'),
    path('update', views.PostUpdateView.as_view(), name='post_update'),
    path('delete', views.PostDeleteView.as_view(), name='post_delete'),

]

