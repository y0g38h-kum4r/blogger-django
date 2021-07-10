from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views #because going to use views functions
urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'), #name is to do reverse lookup
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), #id is the part of the route, pk is the primary key of the post we want to view, allows us to grab value from url and use in view function, detailview expects pk in order to go and fetch that particular object
    path('about/', views.about, name = 'blog-about'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name = 'user-posts'),
]

#say,one has to view the page for blog1, then that url post/1 , id should be the part of route
#The CreateView page displayed to a GET request uses a template_name_suffix of '_form'. post_form is what django expects!!
