from django.urls import path
from bookApp.api import views
# from bookApp.api import views as api_views

urlpatterns = [
    path("authors", views.AuthorListCreateAPIView.as_view(), name="authors"),
    path("books", views.BookListCreateAPIView.as_view(), name="books")
]
