from django.contrib import admin
from django.urls import path
from .views import MainView, SignupView, MyLoginView
from resume.views import ResumeListView, CreateResume
from vacancy.views import VacancyListView, CreateVacancy
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('vacancies', VacancyListView.as_view(), name="vacancy_list"),
    path('resumes', ResumeListView.as_view(), name="resume_list"),
    path('', MainView.as_view(), name="main"),
    path('admin/', admin.site.urls),
    path('home', MainView.as_view(), name="main"),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', MyLoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('resume/new', CreateResume.as_view(), name='new_resume'),
    path('vacancy/new', CreateVacancy.as_view(), name='new_vacancy'),
    path('createResume', CreateResume.as_view()),
    path('createVacancy', CreateVacancy.as_view()),

]
