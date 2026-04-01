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