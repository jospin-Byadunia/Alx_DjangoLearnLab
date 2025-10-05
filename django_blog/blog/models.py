from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your models here.
class Post(models.Model):
    title= models.CharField(max_length=200)
    content= models.TextField()
    published_date= models.DateTimeField(auto_now_add=True)
    author= models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

@login_required
def profile(request):
    if request.method == "POST":
        # Allow user to update email and first/last name
        request.user.email = request.POST.get("email")
        request.user.first_name = request.POST.get("first_name")
        request.user.last_name = request.POST.get("last_name")
        request.user.save()
        return redirect("profile")

    return render(request, "blog/profile.html", {"user": request.user})