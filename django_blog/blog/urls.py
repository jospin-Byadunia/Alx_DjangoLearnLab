from django.urls import path
from .views import( login_view, logout_view, registerView, profile_view, PostListView, PostDetailView, PostCreateView, 
                   PostUpdateView, 
                   PostDeleteView, CommentCreateView, CommentUpdateView, CommentDeleteView, 
                   CommentListView, CommentDetailView)

app_name = "blog" 

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registerView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
    path('', PostListView.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/comments/new/', CommentCreateView.as_view(), name='comment_create'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('post/<int:pk>/comments/', CommentListView.as_view(), name='comment_list'),
    path('comment/<int:pk>/', CommentDetailView.as_view(), name='comment_detail'),
    ]
