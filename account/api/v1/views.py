
from rest_framework.response import Response
from copy import copy
from rest_framework import status ,generics
from .serializers import RegistrationSerializer

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = copy(serializer.data)
        data.pop("password",None)
        return Response(data , status = status.HTTP_201_CREATED)

