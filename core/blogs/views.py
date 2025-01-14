from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.blogs.models import Blog, Category


class BlogListView(ListView):
	model = Blog
	template_name = 'blogs/list_blogs.html'
	context_object_name = 'blogs'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['categories'] = Category.objects.all()
		return context


class DetailBlogView(DetailView):
	model = Blog
	template_name = 'blogs/detail_blog.html'
	context_object_name = 'blog'


# def list_blog_view(request):
# 	blogs = Blog.objects.all()
# 	categories = Category.objects.all()
# 	return render(request, 'blogs/list_blogs.html', {'blogs': blogs, 'categories': categories})


# def detail_blog_view(request, slug):
# 	blog = Blog.objects.get(slug=slug)
# 	return render(request, 'blogs/detail_blog.html', {'blog': blog})
