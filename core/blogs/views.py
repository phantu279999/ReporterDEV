from django.shortcuts import render
from django.views.generic import ListView, DetailView

from core.blogs.models import Blog, Category, BlogInCate


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


class BlogCategoryView(ListView):
	# model = Category
	template_name = 'blogs/blog_category.html'
	context_object_name = 'blogs'

	def get_queryset(self):
		self.category = Category.objects.get(url=self.kwargs['url'])
		return [blog.blog for blog in BlogInCate.objects.filter(category=self.category).select_related('blog')]

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['category'] = self.category
		return context


# def list_blog_view(request):
# 	blogs = Blog.objects.all()
# 	categories = Category.objects.all()
# 	return render(request, 'blogs/list_blogs.html', {'blogs': blogs, 'categories': categories})


# def detail_blog_view(request, slug):
# 	blog = Blog.objects.get(slug=slug)
# 	return render(request, 'blogs/detail_blog.html', {'blog': blog})


# def blog_in_category_view(request, url):
# 	category = Category.objects.get(url=url)
# 	blogs = [blog.blog for blog in BlogInCate.objects.filter(category=category).select_related('blog')]
# 	return render(request, 'blogs/blog_category.html', {'category': category, 'blogs': blogs})
