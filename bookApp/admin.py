from django.contrib import admin
from bookApp.models import Author, Book, Comment
# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Comment)
