from django.urls import path
from .views import RegisterView, ProfileView, FollowUserView, UnfollowUserView, APILoginView, APILogoutView
from rest_framework_simplejwt.views import TokenRefreshView
#view to obtain token
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('login/', APILoginView.as_view(), name='login'),
    path('logout/', APILogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow_user'),
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),  
    ]