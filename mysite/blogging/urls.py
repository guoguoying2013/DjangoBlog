from django.urls import path
from blogging.views import stub_view
from blogging.views import list_view, detail_view

#first is url path, second is the view function name in the view.py
urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
]