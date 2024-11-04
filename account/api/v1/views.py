
from rest_framework.response import Response
from copy import copy
from rest_framework import status , permissions ,generics
from .serializers import RegistrationSerializer ,  UserAPIViewSerializer

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = copy(serializer.data)
        data.pop("password",None)
        return Response(data , status = status.HTTP_201_CREATED)

class UserAPIView(generics.GenericAPIView):
    serializer_class = UserAPIViewSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self,request):
        user = request.user
        serializer = self.serializer_class(user)
        serializer.data['error'] = False
        return Response(serializer.data)
