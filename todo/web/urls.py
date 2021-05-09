from django.urls import path

from . import views

app_name = 'web'
urlpatterns = [
    path('', views.index, name='index'),
    path('edit/<int:todo_id>/', views.edit, name='edit'),
    path('edit/<int:todo_id>/post/', views.post_edit, name='post_edit'),
    path('delete/<int:todo_id>', views.post_delete, name='post_delete'),
]