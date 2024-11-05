from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status , permissions ,generics
from rest_framework.pagination import PageNumberPagination
from ...models import Course , Action , Diet
from django.db.models import Q
from .serializers import CourseSerializer , ActionSerializer , DietSerializer , CreateDietSerializer 
from django.contrib.auth import get_user_model

User = get_user_model()

class ListPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100


class CourseAPIView(generics.GenericAPIView):
    
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        query = Q(teacher= request.user.id) | Q(student= request.user.id)
        queryset = Course.objects.filter(query)
        serializer = self.serializer_class(queryset,many=True)
        return Response(serializer.data)


class ActionListAPIView(generics.ListAPIView):
    serializer_class = ActionSerializer
    pagination_class = ListPagination
    queryset = Action.objects.all()


class DietAPIView(generics.GenericAPIView):
    serializer_class = CreateDietSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        query = Q(course__teacher= request.user.id) | Q(course__student= request.user.id)
        queryset = Diet.objects.filter(query)
        serializer = DietSerializer(queryset,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Diet created successfully!'})