from rest_framework import serializers
from .models import Questions


class QuestionsSerializers(serializers.ModelSerializer):
    """
    Serializer class to get questions
    """

    class Meta:
        model = Questions
        fields = [
            'types',
            'questions',
        ]
