from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.hashers import check_password
from django.contrib import messages
from .models import *
from .cgpa import gpa_calculator
from django.db.models import Sum
# Create your views here.
def homepage(request):
    return render(request, "main/homepage.html", {})

def main(request):
    if request.method == "POST":
        is_username_valid = check_password(request.POST.get("username"),"pbkdf2_sha256$320000$lbdPKNBNhahP8djLxDR3eQ$hASC23bxRRzvyN+o+78YuLJ2v11GUPf1Sm68Y1+a4SA=")
        is_password_valid = check_password(request.POST.get("password"),"pbkdf2_sha256$320000$Wjv7CzD7B0DYOYaCeX0gjA$9YcYztHU2wMxcLcd3s8RjwOg26QRt9ETYodOD8PK6EE=")
        if is_username_valid and is_password_valid:
            return render(request, "main/index.html", {})
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        messages.error(request, "You don't have access to this page, Please login.")
    return redirect("home")

def material_view(request):
    return render(request, "main/material.html",{"materials":Material.objects.all()})

def create_course(request):
    print(request)
    if request.method == "POST":
        print(request.POST)
        department = Department.objects.get(pk=int(request.POST.get("department")))
        course = Course.objects.create(name=request.POST.get("course-name"),semester=request.POST.get("semester"),department=department)
        return HttpResponse(f'''
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Successful!</strong> {course.name} Course has been created.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        ''')

    return render(request, "main/create-course.html", {"departments": Department.objects.all()})

def create_student(request):
    if request.method == "POST":
        print(request.POST)
        department = Department.objects.get(pk=int(request.POST.get("department")))
        student = Student(name=request.POST.get("name"),admission_no=request.POST.get("admission-no"),department=department)
        student.full_clean()
        student.save()
        return HttpResponse(f'''
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Successful!</strong> {student.name} Student has been created.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        ''')
    return render(request, "main/create-student.html", {"departments": Department.objects.all()})

def manage_result(request):
    if request.method == "POST":
        if request.POST.get("type") == "delete":
            print(request.POST)
            Result.objects.get(pk=request.POST.get("result-pk")).delete()
            return HttpResponse("Deleted")
        print(request.POST)
        course = Course.objects.get(pk=int(request.POST.get("course")))
        student = Student.objects.get(pk=int(request.POST.get("student")))
        test_score = request.POST.get("test-score")
        exam_score = request.POST.get("exam-score")
        result = Result.objects.create(student=student, course=course, test_score = test_score, exam_score= exam_score)
        return HttpResponse(f'''
        <div class="alert alert-success alert-dismissible fade show" role="alert">
            <strong>Successful!</strong> Result for {student.name} in {course.name} with total score {result.total_score} and  has been created.
            <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
        </div>
        ''')

    return render(request, "main/manage-result.html", {"courses": Course.objects.all(), "students": Student.objects.all(), "results": Result.objects.order_by("course__name","student__name") })

def manage_department(request):
    if request.method == "POST":
        Department.objects.create(name=request.POST.get("department"))

    return render(request, "main/manage-department.html", {"departments": Department.objects.all()})

def manage_student(request):
    if request.method == "POST":
        Student.objects.get(pk=request.POST.get("student-pk")).delete()
        return HttpResponse("Deleted")
    return render(request, "main/manage-student.html", {"students": Student.objects.all()})

def manage_course(request):
    if request.method == "POST":
        Course.objects.get(pk=request.POST.get("course-pk")).delete()
        return HttpResponse("Deleted")
    return render(request, "main/manage-course.html", {"courses": Course.objects.all()})

def manage_materials(request):
    if request.method == "POST":
        data = request.POST
        file = request.FILES
        print(data)
        if data.get("delete") == "true":
            Material.objects.get(pk=data.get("material-pk")).delete()
            return HttpResponse("Deleted")

        material = Material.objects.create(title=data.get("material-title"),description=data.get("material-desc"),file=file.get("material-file"))
        return HttpResponse(f'''
            <div class="alert alert-success alert-dismissible fade show" role="alert">
                <strong>Successful!</strong> Material has been uploaded.
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        ''')
    print(Material.objects.all())
    return render(request, "main/manage-materials.html", {"materials": Material.objects.all()})


def show_results(request):
    try:
        student = Student.objects.get(admission_no = request.GET.get("admission_no"))
        results = student.result_set.order_by("course__name","course__semester")
        return render(request, "main/showResult.html",{"student":student,"results":results})
    except Student.DoesNotExist:
        messages.warning(request, "Invalid Admission Number")
        return redirect("home")
    except:
        messages.warning(request, "An error occured")
        return redirect("home")
