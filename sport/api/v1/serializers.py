from rest_framework import serializers
from ...models import Course
from account.api.v1.serializers import UserAPIViewSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserAPIViewSerializer()
    user = UserAPIViewSerializer()
    class Meta:
        model = Course
        fields = '__all__'