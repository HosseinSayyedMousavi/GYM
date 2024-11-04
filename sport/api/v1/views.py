from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status , permissions ,generics
from rest_framework.pagination import PageNumberPagination
from ...models import Course , Action
from django.db.models import Q
from .serializers import CourseSerializer , ActionSerializer


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

