from django.urls import path , include
from . import views
app_name="account-api-v1"

urlpatterns = [
        # registration 
        path("registration/",views.RegistrationApiView.as_view(),name = 'registration'),
        # user update
        path("user_info/",views.UserAPIView.as_view() , name = "user-info"),
    ]