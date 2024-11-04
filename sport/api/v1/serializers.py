from rest_framework import serializers
from ...models import Course , Action , Diet
from account.api.v1.serializers import UserAPIViewSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserAPIViewSerializer()
    user = UserAPIViewSerializer()
    class Meta:
        model = Course
        fields = '__all__'

class ActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Action
        fields = '__all__'

class DietSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Diet
        fields = '__all__'