from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('education/', views.education, name='education'),
    path('projects/', views.projects, name='projects'),
    path('experience/', views.experience, name='experience'),
    path('extra/', views.extra, name='extra'),
    path('teachers/', views.teachers, name='teachers'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.my_blog, name='blog'),
    path('blog_list/', views.blog_list, name='blog_list'),
    path('blog_body/', views.blog_body, name='blog_body'),
    path('blog_detail', views.blog_detail, name='blog_detail'),

    path('searchbar/', views.searchbar, name='searchbar'),
]