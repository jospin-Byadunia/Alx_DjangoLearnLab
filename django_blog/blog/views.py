from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm
from .models import Comment
from django.urls import reverse



def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Django's login function
            return redirect("profile")  # Make sure you have a 'profile' URL name
    else:
        form = AuthenticationForm()
    return render(request, "blog/login.html", {"form": form})

def logout_view(request):
    logout(request)  # Django’s logout
    return render(request, "blog/logout.html")

class registerView(CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('/login/')

# profile view to handle post and update user info

@login_required
def profile_view(request):
    if request.method == "POST":
        # update user profile info
        request.user.first_name = request.POST.get("first_name", request.user.first_name)
        request.user.last_name = request.POST.get("last_name", request.user.last_name)
        request.user.email = request.POST.get("email", request.user.email)
        request.user.save() 

        return redirect("profile")  # refresh page after saving

    return render(request, "blog/profile.html", {"user": request.user})


# Implement CRUD Operations for Blog Posts
# Create, Read, Update, Delete views can be added here as needed.

#classe based views
#list view


class PostListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']
    paginate_by = 5

class PostDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'


class PostCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
class PostUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_form.html'
    form_class = PostForm
    success_url = reverse_lazy('blog:post_list')

class PostDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')
    
    
#comment views

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/comment_form.html'

    def form_valid(self, form):
        # Attach the comment to the correct post
        form.instance.post_id = self.kwargs['pk']
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        from .models import Post
        context['post'] = Post.objects.get(pk=self.kwargs['pk'])  # pass post to template
        return context

    def get_success_url(self):
        return reverse('blog:post_detail', kwargs={'pk': self.kwargs['pk']})


class CommentUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_form.html'
    form_class = CommentForm
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # fetch the comment first, then its post
        comment = self.get_object()
        context['post'] = comment.post
        return context

    def get_success_url(self):
        comment = self.get_object()
        return reverse('blog:post_detail', kwargs={'pk': comment.post.pk})
class CommentDeleteView(DeleteView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'
    success_url = reverse_lazy('blog:post_list')

#a view to list all comments for a post

class CommentListView(ListView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_list.html'
    context_object_name = 'comments'
    ordering = ['-created_date']
    paginate_by = 5

class CommentDetailView(DetailView, LoginRequiredMixin, UserPassesTestMixin):
    model = Comment
    template_name = 'blog/comment_detail.html'
    context_object_name = 'comment'