from . import views
from django.urls import path

urlpatterns = [
    path('all/', views.read_post, name = 'readAll'),
    path('getPost/<int:idx>', views.read_one_post, name = 'readOnePost'),
    path('create/', views.create_blog, name = 'createPost'),
    path('update/<int:idx>', views.update_blog, name = 'updateBlog'),
    path('delete/<int:idx>', views.delete_blog, name = 'deleteBlog')
]