from django.urls import path
from . import views 
app_name = "support"
urlpatterns = [
    path('conversations/', views.ConversationAPIView.as_view(),name='conversations'),
]