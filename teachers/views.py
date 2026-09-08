from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Teacher
from django.contrib.auth.decorators import login_required



@login_required
def teacher_display(request):
    return HttpResponse("This is the teacher display page.")



@login_required
def teachers(request):

    teachers_list = Teacher.objects.all()

    departments = (
        Teacher.objects
        .values_list("department", flat=True)
        .distinct()
        .order_by("department")
    )

    context = {
        "teachers": teachers_list,
        "departments": departments,
    }

    return render(
        request,
        "teachers/teacher_list.html",
        context
    )



@login_required
def teacher_detail(request, teacher_id):

    teacher = get_object_or_404(
        Teacher,
        id=teacher_id
    )

    return render(
        request,
        "teachers/teacher_detail.html",
        {"teacher": teacher}
    )



@login_required 
def edit_teacher(request, teacher_id):

    teacher = get_object_or_404(
        Teacher,
        id=teacher_id
    )

    teachers = Teacher.objects.filter(
        status="active"
    )

    if request.method == "POST":

        teacher.first_name = request.POST.get("first_name")
        teacher.last_name = request.POST.get("last_name")
        teacher.email = request.POST.get("email")
        teacher.phone = request.POST.get("phone")
        teacher.department = request.POST.get("department")
        teacher.position = request.POST.get("position")
        teacher.qualification = request.POST.get("qualification")
        teacher.experience = request.POST.get("experience")
        teacher.joining_date = request.POST.get("joining_date")
        teacher.status = request.POST.get("status")
        teacher.bio = request.POST.get("bio")

        teacher.save()

        return redirect("teachers:teachers")

    context = {
        "teacher": teacher,
        "teachers": teachers,
    }

    return render(
        request,
        "teachers/edit_teacher.html",
        context
    )

@login_required 
def delete_teacher(request, teacher_id):
    teacher = get_object_or_404(Teacher, id=teacher_id)

    teacher.delete()

    return redirect("teachers:teachers")


@login_required
def index(request):

    teachers_list = Teacher.objects.all()

    active_teacher = teachers_list.filter(
        status="active"
    )

    inactive_teacher = teachers_list.filter(
        status="inactive"
    )

    departments = (
        Teacher.objects
        .values_list("department", flat=True)
        .distinct()
        .order_by("department")
    )

    context = {
        "teachers": teachers_list,
        "total_teacher": teachers_list.count(),
        "active_teacher": active_teacher.count(),
        "inactive_teacher": inactive_teacher.count(),
        "departments": len(departments),
    }

    return render(
        request,
        "teachers/index.html",
        context
    )



@login_required
def add_teacher(request):

    if request.method == "POST":

        Teacher.objects.create(
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            department=request.POST.get("department"),
            position=request.POST.get("position"),
            qualification=request.POST.get("qualification"),
            experience=request.POST.get("experience"),
            joining_date=request.POST.get("joining_date"),
            status=request.POST.get("status"),
            bio=request.POST.get("bio"),
        )

        return redirect("teachers:teachers")

    return render(
        request,
        "teachers/add_teacher.html"
    )

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Teacher
from .serializers import TeacherSerializer

@api_view(['GET', 'POST'])
def teacher_lists(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()
        serializer = TeacherSerializer(teachers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)