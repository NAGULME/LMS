from django.shortcuts import redirect,render
from app.models import Categories,Courses,Level
from django.contrib import messages 
from django.template.loader import render_to_string
from django.http import JsonResponse




def BASE(request):
    return render(request,'base.html')

def HOME(request):
    Category = Categories.objects.all().order_by('id')[0:5]
    course = Course.objects.filter(status='PUBLISH').order_by('id')
    context ={
        'Category': Category,
        'course':course,
    }
    return render(request,'main/home.html',context)

    return render(request,'main/home.html')

def SINGLE_COURSE(request):
     Category = Categories.get_all_category(Categories)
     Level=Level.object.all()
     course = Course.object.all()
     context ={
         'category':Category,
         'Level':Level,
         'course':course,
     }
     return render(request,'main/single_course.html')

def filter_data(request):
    Category=request.GET.getlist('category[]')
    Level= request.GET.getlist('Level[]')
    if Category:
        course =Course.objects.filter(Category__id__in=Category).order_by('-id')

    elif Level:
        course = Course.objects.filter(Level__id__in=Level).order_by('-id')
    else:
        course= Course.objects.all().order_by('-id')


        context ={
            'course':course
        }
    t = render_to_string('ajax/course.html',context)
    
    return JsonResponse({'data':t})

def CONTACT_US(request):
    Category = Categories.get_all_category( Categories )
    context ={
        'category':Category
    }
    
    return render(request,'main/contant_us.html',context )

def ABOUT_US(request):
    Category = Categories.get_all_category( Categories )
    context ={
        'category':Category
    }
    return render(request,'main/about_us.html' )

def SEARCH_COURSE(request):
    Category = Categories.get_all_category( Categories )
    context ={
        'category':Category
    }
    query = request.GET['query']
    course = Course.objects.filter(title__icontains = query)
    context = {
        'course':course,
    }
    return render(request,'search/search.html',context)

def COURSE_DETAILS(request ,slug):

    Category = Categories.get_all_category( Categories )
    time_dyration=Video.objects.filter(course __slug=slug).aggregate(sum('time_duration'))
    course_id=Course.objects.get(slug=slug)
    try:
       check_enroll=UserCourse.objects.get(user=request.user,course=)
    except UserCourse.DoesNotExist:
        check_enroll=None

    course =Course.objects.filter(slug = slug)
    if course.exists():
        course = course.first()
    else:
        return redirect('404')
    context ={
        'course':course,
    }
    return render(request,'course/course_details.html',course)

def PAGE_NOT_FOUND(request):
    Category = Categories.get_all_category( Categories )
    context ={
        'category':Category
    }
    return render (request,'error/404.html')

def CHECKOUT(request,slug):
    course = Course.object.get(slug= slug)
    check_id = Course.objects.get()
    check_enroll =UserCourse.objects.get(user=request.user ,course =)
    if course.price ==0:
        course =UserCourse(
            user = request.user,
            course = course,
            
        )
        course.save()
        messages.success(request,'course are successfully enrolled!')
        return redirect('home')
    return render(request,'Checkout/checkout.html')

def MY_COURSE(request):
    course =UserCourse.objects.filter(user= request.user)
    context={
        'course':course,
    }
    return render(request,'course/my-course.html',context)
