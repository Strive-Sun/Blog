from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostListView.as_view(), name='index'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('category/<int:pk>/', views.CategoryPostView.as_view(), name='category_posts'),
    path('tag/<int:pk>/', views.TagPostView.as_view(), name='tag_posts'),
    path('archive/', views.ArchiveView.as_view(), name='archive'),
    path('categories/', views.CategoryListView.as_view(), name='categories'),
    path('tags/', views.TagListView.as_view(), name='tags'),
    path('friends/', views.FriendsView.as_view(), name='friends'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('search/', views.search, name='search'),
] 