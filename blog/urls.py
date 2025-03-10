from django.urls import path

from .views import search, detail, category, delete_comment

urlpatterns = [
    path('search/', search, name='search'),
    path('<slug:category_slug>/<slug:slug>/', detail, name="post_detail"),
    path('<slug:slug>/', category, name="category_detail"),
    path('comment/<int:id>/delete/', delete_comment, name='delete_comment'),
]