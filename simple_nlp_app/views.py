from rest_framework import viewsets, permissions, mixins
from rest_framework.response import Response
from rest_framework import status
from .serializers import QuestionsSerializers
from .models import Questions
from .task import generate_questions


class SimpleViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """and get replay """

    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializers
    permission_classes = [permissions.AllowAny, ]

    def create(self, request, *args, **kwargs):
        data = request.data
        context = generate_questions(data['types'], data['questions'])
        return Response(context, status=status.HTTP_201_CREATED, )