from django.urls import path
from .views import login_view, logout_view, registerView, profile_view



urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', registerView.as_view(), name='register'),
    path('profile/', profile_view, name='profile'),
]
