from django.urls import path
from .views import posts, post_detail

urlpatterns = [
    path('', posts, name='posts'),
    path('<int:id>', post_detail)
]
