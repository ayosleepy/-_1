from django.urls import path, re_path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    re_path(r'^Author/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail'),
]