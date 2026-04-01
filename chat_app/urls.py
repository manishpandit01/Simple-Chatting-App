from django.urls import path

from chat_app import views


urlpatterns = [
    path("",views.chat_list,name="chat-list"),
    path('delete/<int:id>/',views.chat_delete,name="chat-delete"),
    path("create/",views.chat_create,name="chat-create"),
]