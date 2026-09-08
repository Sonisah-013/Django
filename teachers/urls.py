from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('', views.teacher_display, name='teacher_display'),
    path('teachers/', views.teachers, name='teachers'),
    path('teacher-details/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('index/', views.index, name='index'),
    path('add-teacher/', views.add_teacher, name='add_teacher'),
    path('details/<int:teacher_id>/', views.teacher_detail, name='teacher_detail'),
    path('edit/<int:teacher_id>/', views.edit_teacher, name='edit_teacher'),
    path('delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('teacher-lists/', views.teacher_lists, name='teacher_lists'),
]