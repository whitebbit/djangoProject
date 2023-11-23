from django.urls import path
from .views import blog_detail

urlpatterns = [
    path("blog/<int:blog_id>/", blog_detail, name="blog_detail"),
]
