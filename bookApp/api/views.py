from bookApp.api.serializers import AuthorSerializer, BookSerializer, CommentSerializer
from bookApp.models import Author, Book, Comment
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.generics import get_object_or_404


class BookListCreateAPIView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        book = get_object_or_404(Book, pk=self.kwargs.get("book_pk"))
        serializer.save(book=book)


class AuthorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class AuthorListCreateAPIView(APIView):
#     def get(self, request):
#         writers = Author.objects.all()
#         serializer = AuthorSerializer(
#             writers, many=True, context={'request': request})
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class BookListCreateAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         seralizer = BookSerializer(data=request.data)
#         if seralizer.is_valid():
#             seralizer.save()
#             return Response(seralizer.data, status=status.HTTP_201_CREATED)
#         return Response(seralizer.errors, status=status.HTTP_400_BAD_REQUEST)
