from django.urls import path
from . import views

app_name = 'web'
urlpatterns = [
    path("<int:id>", views.tables, name="tables"),
    path("", views.index, name="home"),
    path("create/", views.create, name="create"),
    path("index/", views.index, name="index"),
    path("HowTo/", views.howto, name="HowTo"),
    path("Impressum/", views.impressum, name="Impressum"),
    path("create/post", views.post_create, name="post_create"),
    path('edit/<int:item_id>/', views.edit, name='edit'),
    path('edit/<int:item_id>/post/', views.post_edit, name='post_edit'),
    path('delete/<int:item_id>', views.post_delete, name='post_delete'),
]
