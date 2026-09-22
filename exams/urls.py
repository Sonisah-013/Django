from django.urls import path
from . import views

app_name = 'exams'
urlpatterns = [
    path('', views.exam_list, name='exam_list'),
    path('add-marks/<int:exam_id>/', views.add_marks, name='add_marks'),
    path('report/<int:exam_id>/', views.exam_report, name='report'),
    path('student/<int:student_id>/', views.student_report_card, name='student_report_card'),
    path('schedule/', views.exam_schedule, name='exam_schedule'),
]