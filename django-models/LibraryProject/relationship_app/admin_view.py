from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "admin"

@user_passes_test(is_admin, login_url="/login/")
def admin_view(request):
    return render(request, "relationship_app/admin_view.html")
