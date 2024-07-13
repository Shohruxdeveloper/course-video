from django.urls import path, include

from .views import BlogListCreateView, BlogRetrieveUpdateDestroyView


urlpatterns = [
    path('api/v1/blog', BlogListCreateView.as_view()),
    path('api/v1/blog/<int:pk>', BlogRetrieveUpdateDestroyView.as_view()),

]
