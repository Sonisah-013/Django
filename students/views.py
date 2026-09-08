from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Student





@login_required
def students_home(request):
    return render(request, 'home.html')




@login_required
def students_about(request):
    return render(request, 'about.html')



students = [
    {
        "student_id": 1,
        "name": "Kaushal Karn",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    },
    {
        "student_id": 2,
        "name": "John Doe",
        "age": 22,
        "grade": "B",
        "course": "Mathematics"
    },
    {
        "student_id": 3,
        "name": "Harry Potter",
        "age": 20,
        "grade": "A",
        "course": "Computer Science"
    },
    {
        "student_id": 4,
        "name": "Jane Smith",
        "age": 19,
        "grade": "B",
        "course": "Physics"
    }
]



@login_required
def student_display(request):
    return JsonResponse(students, safe=False)




@login_required
def student_details(request, student_id):

    for student in students:

        if student["student_id"] == student_id:
            return JsonResponse(student)

    return HttpResponse("Student not found.")




@login_required
def student_list(request):

    students_list = Student.objects.all()

    context = {
        "students": students_list
    }

    return render(
        request,
        'students/student_list.html',
        context
    )



@login_required
def index(request):

    return render(
        request,
        'students/index.html'
    )



@login_required
def student_detail(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    return render(
        request,
        'students/student_details.html',
        {
            "student": student
        }
    )




@login_required
def add_students(request):

    if request.method == "POST":

        Student.objects.create(
            student_id=request.POST.get("student_id"),
            first_name=request.POST.get("first_name"),
            last_name=request.POST.get("last_name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            date_of_birth=request.POST.get("date_of_birth"),
            department=request.POST.get("department"),
            program=request.POST.get("program"),
            semester=request.POST.get("semester"),
            status=request.POST.get("status"),
            address=request.POST.get("address"),
            notes=request.POST.get("notes"),
        )
        messages.success(request, "Student  registered successfully!")
        return redirect("students:student_list")

    return render(
        request,
        "students/add_student.html"
    )




@login_required
def edit_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    if request.method == "POST":

        student.student_id = request.POST.get("student_id")
        student.first_name = request.POST.get("first_name")
        student.last_name = request.POST.get("last_name")
        student.email = request.POST.get("email")
        student.phone = request.POST.get("phone")
        student.date_of_birth = request.POST.get("date_of_birth")
        student.department = request.POST.get("department")
        student.program = request.POST.get("program")
        student.semester = request.POST.get("semester")
        student.status = request.POST.get("status")
        student.address = request.POST.get("address")
        student.notes = request.POST.get("notes")

        student.save()

        return redirect("students:student_list")

    return render(
        request,
        "students/edit_student.html",
        {
            "student": student
        }
    )




@login_required
def delete_student(request, student_id):

    student = get_object_or_404(
        Student,
        id=student_id
    )

    student.delete()

    return redirect("students:student_list")


from django.views.generic import ListView,CreateView
from .models import Student
from django.urls import reverse_lazy


class StudentListView(ListView):
      model = Student
      template_name = 'students/student_list_cbv.html'
      context_object_name = 'students'
      ordering = ['first_name']
      paginate_by = 10


class StudentCreateView(CreateView):
      model = Student
      fields=[
          'student_id',
          'first_name',
          'last_name',
          'email',
          'phone',
          'date_of_birth',
          'department',
          'program',
          'semester',
          'status',
          'address',
          'notes'
      ]
      template_name = 'students/form.html'
      success_url = reverse_lazy('students:student_list')
      
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from .serializers import StudentSerializer

@api_view(['GET', 'POST'])
def student_lists(request):
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)