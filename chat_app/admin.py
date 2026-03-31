from chat_app.models import Message

from django.contrib import admin

# Register your models here.
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display=['sender','message','created_at','updated_at']