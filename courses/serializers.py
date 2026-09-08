from rest_framework import serializers
from .models import Course

class CourseSerializer(serializers.ModelSerializer):
    """Serializer for Course model"""

    class Meta:
        model = Course
        fields = [ 'code', 'credits', 'department', 'semester', 'status']
        read_only_fields = ['course_duration', 'course_description']


    def validate_email(self, value):
        if Course.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
