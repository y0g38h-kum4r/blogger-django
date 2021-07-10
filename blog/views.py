from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #classBasedview
from .models import Post
# Create your views here.
def home(request):
	return render(request, 'blog/home.html', {'posts' : Post.objects.all()}) #similar to the query in the python shell
#this function is going to handle the traffic from the home page of blog
#what the user needs to see when sent to this route
#this is where the logic goes for how we want to handle certain routes(here, blog home page)


class PostListView(ListView):
	#what model to query, in order to create the list
	#class based views looks for templates with a certain naming pattern <app>/<model>_<viewtype>.html
	model = Post
	template_name = 'blog/home.html'
	#While this view is executing, self.object_list will contain the list of objects (usually, but not necessarily a queryset) that the view is operating upon.
	#letting the class know that the variable to be called is posts instead of object_list
	context_object_name = 'posts'
	ordering = ['-date_posted']
	#no need to create Paginator class and do stuff, all that is required is
	paginate_by = 5

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/users_posts.html'
	context_object_name = 'posts'
	paginate_by = 5
	#we have to modify the queryset the list view returns by overriding a method get_queryset
	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username')) #kwargs the query parameters and get username from url, if it exists capture in variable
		return Post.objects.filter(author=user).order_by('-date_posted')



class PostDetailView(DetailView):
	model = Post

class PostCreateView(LoginRequiredMixin, CreateView): #a view with a form where we create a new post, fields to be in form has to be mentioned, date-filled automatically, however this does not know that the author is the current logged in user, way to do is to override
	#formvalid method of createview, allow us to add author before form is submitted
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class PostUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView): #a view with a form where we create a new post, fields to be in form has to be mentioned, date-filled automatically, however this does not know that the author is the current logged in user, way to do is to override
	#formvalid method of createview, allow us to add author before form is submitted
	model = Post
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
	model = Post
	success_url = '/'
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})

#when looking at a indivudual post, this is a detail_view
#to find url of model object, is to create get_absolute_url method that returns path to specific instance
