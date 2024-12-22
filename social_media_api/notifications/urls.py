# notifications/urls.py
from django.urls import path
from posts.views import NotificationListView, MarkNotificationAsReadView

urlpatterns = [
    path('', NotificationListView.as_view(), name='notification-list'),
    path('read/<int:pk>/', MarkNotificationAsReadView.as_view(), name='mark-notification-read'),
]
