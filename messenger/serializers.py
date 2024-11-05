from rest_framework import serializers ,exceptions 
from .models import Conversation , ConversationMessage
import difflib
from django.utils.translation import gettext as _
from django.core.validators import MaxLengthValidator


class CreateConversationSerializer(serializers.ModelSerializer):
    message = serializers.CharField(required=True,validators=[MaxLengthValidator(1000)])
    class Meta:
        model = Conversation
        fields = ("sender","receiver","title","message")


class ConversationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Conversation
        fields = '__all__'