from django.urls import path
from . import views

app_name = 'attendance'

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('mark/<int:course_id>/', views.mark_attendance, name='mark'),
    path('report/<int:course_id>/', views.absence_report, name='report'),
    path('student/<int:student_id>/', views.student_report, name='student_report'),
]