from django.db import models
from students.models import Student
from courses.models import Course

class Exam(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='exams')
    name = models.CharField(max_length=100)   # e.g. "Midterm", "Final"
    date = models.DateField()
    total_marks = models.PositiveIntegerField(default=100)

    def __str__(self):
        return f"{self.name} - {self.course.name}"

class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name='results')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='results')
    marks_obtained = models.PositiveIntegerField()

    class Meta:
        unique_together = ('exam', 'student')

    def percentage(self):
        return round((self.marks_obtained / self.exam.total_marks) * 100, 2)

    def grade(self):
        p = self.percentage()
        if p >= 90: return 'A+'
        elif p >= 80: return 'A'
        elif p >= 70: return 'B'
        elif p >= 60: return 'C'
        elif p >= 50: return 'D'
        else: return 'F'

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.marks_obtained}"