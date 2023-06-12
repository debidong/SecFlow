from django.urls import path
from .views import *

urlpatterns = [
    path('info', TokenView.as_view()),
    path('reminder', ReminderView.as_view()),
    path('reminder/add', AddReminderView.as_view()),
    path('reminder/delete', DelReminderView.as_view()),
    path('userList', ListUsersView.as_view())
]