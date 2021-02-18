from django.contrib import admin
from .models import Contact, about_me_data, blog, Post, projects_data, experience_data, education_data, home_data, extra_data

# Register your models here.
@admin.register(Contact)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'fname', 'lname', 'mobile')

@admin.register(blog)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'created_on', 'user_name')
  list_filter = ("title", "user_name")
  search_fields = ['title', 'content']

@admin.register(Post)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'created_on', 'author', 'status')
  search_fields = ['title', 'content']

  class Media:
    js = ('tiny.js',)

@admin.register(projects_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'pro_name', 'start_date')
  ordering = ('start_date',)

@admin.register(experience_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'organisation', 'start_date')
  ordering = ('start_date',)

  class Media:
    js = ('tiny.js',)

@admin.register(education_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'edu_name', 'passing', 'marks')
  ordering = ('passing',)

  class Media:
    js = ('tiny.js',)


@admin.register(home_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'tag')

  class Media:
    js = ('tiny.js',)

@admin.register(about_me_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id',)

  class Media:
    js = ('tiny.js',)

@admin.register(extra_data)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id',)