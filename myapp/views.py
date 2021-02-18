from django.shortcuts import render
from myapp.models import Contact
from django.contrib import messages
from .models import blog, Post, projects_data, experience_data, education_data, home_data, about_me_data, extra_data
from django.db.models import Q

# Create your views here.
def home(request):
    context ={
        'home': home_data.objects.all()
    }
    return render(request, 'home.html', context)

def about(request):
    context ={
        'about_me':about_me_data.objects.all()
    }
    return render(request, 'about.html', context)

def education(request):
    context ={
        'educations': education_data.objects.all().order_by('-passing')
    }
    return render(request, 'education.html', context)

def projects(request):
    context ={
        'projects': projects_data.objects.all().order_by('-start_date')
    }
    return render(request, 'projects.html', context)

def experience(request):
    context ={
        'experiences' : experience_data.objects.all().order_by('-start_date')
    }
    return render(request, 'experience.html', context)

def extra(request):
    context ={
        'extras' : extra_data.objects.all().order_by('-id')
    }
    return render(request, 'extra.html', context)

def teachers(request):
    return render(request, 'teachers.html')

def contact(request):
    if request.method == 'POST':
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        msg = request.POST.get('msg')

        contact = Contact(fname=fname, lname = lname, email=email, mobile=mobile, msg=msg)
        contact.save()
        messages.success(request, 'Your message has been sent')
    return render(request, 'contact.html')

def my_blog(request):
    sort_by_start_date = blog.objects.all().order_by('-created_on')
    dest = {
        'ob' : sort_by_start_date
    }
    return render(request, 'blog.html', dest)

def blog_list(request):
    dest = Post.objects.all().order_by('-created_on')
    post_id = []
    blog_id = request.POST.get('blog_id')
    for i in dest:
        if i.blog_name_id == int(blog_id):
            post_id.append(i.id)
    context = {
        'post_id': post_id,
        'posts': dest
    }
    return render(request, 'blog_list.html', context)

def blog_body(request):
    dest = Post.objects.all()
    blog_body_id = int(request.POST.get('post_id'))
    post_id = 0
    for i in dest:
        if i.id == blog_body_id:
            post_id = i.id
            break
    context = {
        'post_id': post_id,
        'posts': dest
    }
    return render(request, 'blog_body.html', context)

def blog_detail(request):
    blog_id = int(request.POST.get('blog_detail_id'))
    dest = blog.objects.all()
    context = {
        'blog_id': blog_id,
        'blog': dest
    }
    return render(request, 'blog_detail.html', context)


def searchbar(request):
    query = None
    results = []
    if request.method == 'POST':
        query = request.POST.get('search')
        results = Post.objects.filter(Q(title__icontains=query) | Q(content__icontains=query))
        return render(request, 'searchbar.html', {'query': query, 'results': results})