from django.urls import path , include
from . import views
app_name="sport-api-v1"

urlpatterns = [
    path('course/',views.CourseAPIView.as_view(),name='courses'),
    path('action/',views.ActionListAPIView.as_view(),name='actions'),
    path('diet/',views.DietAPIView.as_view(),name='diets')
    ]