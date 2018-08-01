from django.urls import path
from .import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'), #root URL
    path('issues/<int:pk>', views.issue_detail, name='issue_detail'),
    path('comments', views.comment_list, name='comment_list'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
]