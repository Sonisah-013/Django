from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    """Serializer for Student model"""

    class Meta:
        model = Student
        fields = ['student_id','date_of_birth', 'first_name', 'last_name', 'email', 'program', 'department','semester']
        


    def validate_email(self, value):
        if Student.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value
