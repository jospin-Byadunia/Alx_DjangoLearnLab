from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import user_passes_test

def is_member(user):
    return hasattr(user, "userprofile") and user.userprofile.role == "member"

@user_passes_test(is_member, login_url="/login/")
def member_view(request):
    return render(request, "relationship_app/member_view.html")