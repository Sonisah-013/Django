from django.urls import path
from . import views

app_name = 'fees'
urlpatterns = [
    path('', views.fee_list, name='fee_list'),
    path('invoice/<int:invoice_id>/', views.invoice_detail, name='invoice_detail'),
    path('student/<int:student_id>/', views.student_fees, name='student_fees'),
]