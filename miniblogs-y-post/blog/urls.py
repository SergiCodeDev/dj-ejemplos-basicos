from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path('', views.post, name='post'),
    path('<int:post_id>', views.postid, name='postid'),
]