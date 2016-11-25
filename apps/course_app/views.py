from django.shortcuts import render, redirect
from .models import Course 

# Create your views here.
def index(request):
    courses = Course.objects.all()
    # print "courses:", courses

    # print ("query:", 50*"*")
    # print courses.query
    # print ("object:",50*"*")
    # print courses
    # print (50*"*")
    # for course in courses:
    #     print course.name, course.description

    context = {
        'courses': courses
    }
    return render(request, 'course_app/index.html', context)


def add_course(request):
    if request.method == "POST":
        print "Got add post" 
        course_name = request.POST['name']
        course_description = request.POST['description']
        print course_name   
        print course_description
        Course.objects.create(name=course_name, description=course_description)
    return redirect (index)


def delete_course(request, id):
    print "Got delete request" 
    courses = Course.objects.filter(id=id)
    
    print ("query:", 50*"*")
    print courses.query
    print ("object:",50*"*")
    print courses
    print (50*"*")
    for course in courses:
        print course.name, course.description

    context = {
        'courses': courses
    }

    return render(request, 'course_app/verify.html', context)

       
def delete(request, id, verification):
    print "Got delete command"
    print verification 
    if verification == "confirm":
        Course.objects.filter(id=id).delete()
    return redirect (index)
