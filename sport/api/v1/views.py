from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status , permissions ,generics

from ...models import Course
from django.db.models import Q
from .serializers import CourseSerializer

class CourseAPIView(generics.GenericAPIView):
    
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        query = Q(teacher= request.user.id) | Q(student= request.user.id)
        queryset = Course.objects.filter(query)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)