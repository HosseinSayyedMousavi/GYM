from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinLengthValidator , MaxLengthValidator
User = get_user_model()

# Create your models here.
class Conversation(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversation_sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='conversation_receiver')
    title = models.CharField(max_length=50, validators=[MinLengthValidator(10)])
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self, ):
        return str(self.id) + " " + self.title


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True , blank=True)
    message = models.TextField(validators=[MaxLengthValidator(1000)])
    viewed = models.BooleanField(default=False)
    
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return ""