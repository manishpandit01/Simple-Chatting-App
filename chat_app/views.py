from django.http import HttpResponseRedirect
from django.shortcuts import  get_object_or_404, redirect 
from chat_app.models import Message

from django.shortcuts import render

# Create your views here.
def chat_list(request):
    chats=Message.objects.all()
    return render(
        request,
        "chat_list.html",
        {"chats":chats}
    )

def chat_delete(request,id):
    chat=get_object_or_404(Message,id=id)
    chat.delete()
    return redirect('chat-list')

def chat_create(request):
    if request.method=="POST":
        sender="Manish"
        message_text=request.POST.get("message")
        
        if message_text:
            Message.objects.create(sender=sender,message=message_text)
    return redirect('chat-list')

def chat_update(request,id):
    chat=get_object_or_404(Message,id=id)
    if request.method=="POST":
        message_text=request.POST.get("message")
        
        if message_text:
            chat.message=message_text
            chat.save()
    return redirect('chat-list')
    