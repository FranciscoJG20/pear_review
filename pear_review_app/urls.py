from django.urls import path
from .import views

urlpatterns = [
    path('', views.issue_list, name='issue_list'), #root URL
    path('issues/<int:pk>', views.issue_detail, name='issue_detail'),
    path('issues/new', views.issue_create, name='issue_create'),
    path('issues/<int:pk>/edit', views.issue_edit, name='issue_edit'),
    path('issues/<int:pk>/delete', views.issue_delete, name='issue_delete'),
    path('comments', views.comment_list, name='comment_list'),
    path('comments/<int:pk>', views.comment_detail, name='comment_detail'),
    path('comments/new', views.comment_create, name='comment_create'),
    path('comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),
    path('comments/<int:pk>/delete', views.comment_delete, name='comment_delete'),
]
