from django.shortcuts import render, redirect
from django.db.models import Count
from courses.models import Course
from students.models import Student
from .models import AttendanceRecord

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'attendance/course_list.html', {'courses': courses})

def mark_attendance(request, course_id):
    course = Course.objects.get(id=course_id)
    students = Student.objects.filter(
        department=course.department,
        semester=course.semester
    )

    if request.method == 'POST':
        date = request.POST.get('date')
        for student in students:
            status = request.POST.get(f'status_{student.id}')
            AttendanceRecord.objects.update_or_create(
                student=student, course=course, date=date,
                defaults={'status': status}
            )
        return redirect('attendance:report', course_id=course.id)

    return render(request, 'attendance/mark_attendance.html', {
        'course': course, 'students': students
    })

def absence_report(request, course_id):
    course = Course.objects.get(id=course_id)
    records = AttendanceRecord.objects.filter(course=course, status='absent').order_by('date')
    summary = (AttendanceRecord.objects
               .filter(course=course, status='absent')
               .values('student__first_name', 'student__last_name')
               .annotate(absent_count=Count('id')))
    return render(request, 'attendance/report.html', {
        'course': course, 'records': records, 'summary': summary
    })