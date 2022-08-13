from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Comment
from .serializers import CommentSerializer

class CommentView(APIView):

    def get(self, request):
        comments = Comment.objects.all()
        print(comments)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


class CommentSingleView(APIView):

    def patch(self, request, id):
        comment = Comment.objects.filter(id=id).first()
        if comment is None:
            return Response({'error': 'Bad request'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = CommentSerializer(comment, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        place = get_object_or_404(Comment, id=id)
        place.delete()

        return Response('Comentatio eliminado', status=status.HTTP_204_NO_CONTENT)