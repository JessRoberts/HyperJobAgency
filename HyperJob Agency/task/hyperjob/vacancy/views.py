from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render
from django.views import View

from .models import Vacancy
# Create your views here.

class VacancyListView(View):
    def get(self, request):
        context = {}
        posts = Vacancy.objects.all()
        context["posts"] = posts
        return render(request, 'vacancy/vacancy_list.html', context)

class CreateVacancy(View):
    def post(self, request):
        username = request.user
        description = request.POST.get("description")
        if request.user.is_staff:
            post = Vacancy(author=username, description=description)
            post.save()
            return HttpResponseRedirect("/")
        return HttpResponseForbidden()
