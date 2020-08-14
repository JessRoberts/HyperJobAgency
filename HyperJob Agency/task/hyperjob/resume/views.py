from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from .models import Resume
# Create your views here.

class ResumeListView(View):
    def get(self, request):
        context = {}
        posts = Resume.objects.all()
        context["posts"] = posts
        return render(request, 'resume/resume_list.html', context)

class CreateResume(View):
    def post(self, request):
        username = request.user
        description = request.POST.get("description")
        if request.user.is_authenticated:
            post = Resume(author=username, description=description)
            post.save()
            return HttpResponseRedirect("/")
        return HttpResponseForbidden()
