from django.urls import path
from .views import login_view, logout_view, registerView, profile_view, PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

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
]
