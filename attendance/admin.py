from django.contrib import admin
from .models import AttendanceRecord

@admin.register(AttendanceRecord)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course', 'date', 'status')
    list_filter = ('course', 'date', 'status')
    search_fields = ('student__name',)