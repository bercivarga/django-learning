from django.views.generic import DetailView, ListView

from blog.models import Blog

class BlogListView(ListView):
    model = Blog


class BlogDetailView(DetailView):
    model = Blog 

