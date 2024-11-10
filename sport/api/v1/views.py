from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status , permissions ,generics
from rest_framework.pagination import PageNumberPagination
from ...models import Course , Action , Diet , Plan
from django.db.models import Q
from .serializers import CourseSerializer , ActionSerializer , DietSerializer , CreateDietSerializer , UpdateDietSerializer
from .serializers import PlanSerializer , CreatePlanSerializer , UpdatePlanSerializer
from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend

from .filters import PlanFilter, DietFilter 
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
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = DietFilter

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
    
    
class UpdateDietAPIView(generics.GenericAPIView):
    serializer_class = UpdateDietSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    def get_queryset(self):
        queryset = Diet.objects.filter(course__teacher= self.request.user)
        return queryset
    
    def put(self,request,id):
        diet = self.get_object()
        serializer = self.get_serializer(instance=diet,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Diet updated successfully!'})
    
    
class PlanAPIView(generics.ListAPIView):
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = ListPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PlanFilter
    
    def get_queryset(self):
        query= Q(course__teacher= self.request.user.id) | Q(course__student = self.request.user.id)
        queryset = Plan.objects.filter(query)
        return queryset
    
    
    def post(self,request):
        serializer = CreatePlanSerializer(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'new Exercise created successfully!'})
    
    
class UpdatePlanAPIView(generics.GenericAPIView):
    serializer_class = UpdatePlanSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'id'
    def get_queryset(self):
        queryset = Plan.objects.filter(course__teacher= self.request.user)
        return queryset
    
    def put(self,request,id):
        plan = self.get_object()
        serializer = self.get_serializer(instance=plan,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message':'Exercise plan updated successfully!'})
