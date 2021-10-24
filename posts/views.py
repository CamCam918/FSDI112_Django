from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,)
from posts.models import Post
# Create your views here.

class HomePageView(TemplateView):
    template_name = "home.html"

class PostListView(ListView):
    model = Post
    template_name = "post_list.html"

class PostDetailView(DetailView):
    model = Post
    template_name= "post_detail.html"