from rest_framework import serializers ,exceptions 
from .models import Conversation , ConversationMessage
import difflib
from django.utils.translation import gettext as _


class ConversationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Conversation
        fields = '__all__'