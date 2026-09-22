
from django.shortcuts import render, redirect
from courses.models import Course
from students.models import Student
from .models import Exam, Result

def exam_list(request):
    exams = Exam.objects.all().order_by('-date')
    return render(request, 'exams/exam_list.html', {'exams': exams})

def add_marks(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    students = Student.objects.filter(
        department=exam.course.department,
        semester=exam.course.semester
    )

    if request.method == 'POST':
        for student in students:
            marks = request.POST.get(f'marks_{student.id}')
            if marks:
                Result.objects.update_or_create(
                    exam=exam, student=student,
                    defaults={'marks_obtained': marks}
                )
        return redirect('exams:report', exam_id=exam.id)

    return render(request, 'exams/add_marks.html', {'exam': exam, 'students': students})

def exam_report(request, exam_id):
    exam = Exam.objects.get(id=exam_id)
    results = Result.objects.filter(exam=exam).order_by('-marks_obtained')
    return render(request, 'exams/report.html', {'exam': exam, 'results': results})

def student_report_card(request, student_id):
    student = Student.objects.get(id=student_id)
    results = Result.objects.filter(student=student).order_by('-exam__date')
    return render(request, 'exams/student_report_card.html', {'student': student, 'results': results})

from django.utils import timezone

def exam_schedule(request):
    exams = Exam.objects.all().order_by('date')
    today = timezone.now().date()
    return render(request, 'exams/exam_schedule.html', {
        'exams': exams,
        'today': today
    })