from rest_framework import serializers
from ...models import Course , Action , Diet , Plan
from account.api.v1.serializers import UserAPIViewSerializer

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserAPIViewSerializer()
    student = UserAPIViewSerializer()
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
        

class CreateDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        exclude = ['created_date','update_date']
        
    def validate(self,attrs):
        course = attrs.get('course')
        if course.teacher != self.context['request'].user:
            raise serializers.ValidationError({"detail" : "You are not the teacher of this course."})
        
        return super().validate(attrs)
        

class UpdateDietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = ['start_date','end_date','description']
        
    def validate(self,attrs):
        if self.instance.course.teacher != self.context['request'].user:
            raise serializers.ValidationError({"detail" : "You are not the teacher of course of this diet."})
        
        return super().validate(attrs)

class PlanSerializer(serializers.ModelSerializer):
    course = CourseSerializer()
    class Meta:
        model = Plan
        fields = '__all__'

class CreatePlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan  
        exclude = ['created_date','update_date']

        def validate(self,attrs):
            course = attrs.get('course')
            if course.teacher != self.context['request'].user:
                raise serializers.ValidationError({"detail" : "You are not the teacher of this course."})
        
            return super().validate(attrs)
