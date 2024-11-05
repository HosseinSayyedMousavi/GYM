
from rest_framework.response import Response
from .models import Conversation, ConversationMessage
from django.contrib.auth import get_user_model
from rest_framework import generics ,permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import  ConversationSerializer
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiExample
from datetime import datetime
from django.db.models import Q
User = get_user_model()


class ListPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'
    max_page_size = 100
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'new_conversations': Conversation.objects.filter(conversationmessage__viewed=False).exclude(conversationmessage__user=self.request.user.id).distinct().count(),
            'results': data,
        })


class ConversationAPIView(generics.ListAPIView):
    permission_classes =[permissions.IsAuthenticated]
    serializer_class = ConversationSerializer
    pagination_class = ListPagination

    def get_queryset(self):
        query = Q(sender= self.request.user.id) | Q(receiver= self.request.user.id)
        queryset = Conversation.objects.filter(query).order_by('-id')
        return queryset
    
    @extend_schema(
        description="Get list of user's conversations",
    )
    def get(self,*args,**kwargs):
        return super().get(*args,**kwargs)
        

