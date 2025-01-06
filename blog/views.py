from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView
from .models import Post, Category, Tag
from django.db.models import Q

class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    paginate_by = 10

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset=queryset)
        post.increase_views()
        return post

class ArchiveView(ListView):
    model = Post
    template_name = 'blog/archive.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        posts_by_year = {}
        for post in context['posts']:
            year = post.created_time.year
            if year not in posts_by_year:
                posts_by_year[year] = []
            posts_by_year[year].append(post)
        context['posts_by_year'] = posts_by_year
        return context

class CategoryListView(ListView):
    model = Category
    template_name = 'blog/category_list.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for category in context['categories']:
            category.post_count = category.post_set.count()
        return context

class TagListView(ListView):
    model = Tag
    template_name = 'blog/tag_list.html'
    context_object_name = 'tags'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for tag in context['tags']:
            tag.post_count = tag.post_set.count()
        return context

class FriendsView(TemplateView):
    template_name = 'blog/friends.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['friends'] = [
            {
                'name': '示例博客',
                'url': 'https://example.com',
                'description': '一个示例博客'
            },
        ]
        return context

class AboutView(TemplateView):
    template_name = 'blog/about.html'

def search(request):
    q = request.GET.get('q')
    if q:
        posts = Post.objects.filter(
            Q(title__icontains=q) |
            Q(content__icontains=q)
        )
    else:
        posts = Post.objects.all()
    
    return render(request, 'blog/search.html', {
        'posts': posts,
        'query': q
    })
