from django.urls import path
from . import views

urlpatterns = [
    path('', views.siteindex),
    path('blog/', views.blogindex, name='blogurl'),
    path('blog/<post_slug>', views.blogposts, name='blogposts')
]
