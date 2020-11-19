from rest_framework import serializers
from .models import Question, Answer


class QuestionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Question  # 指定的模型类
        fields = ('pk', 'title', 'u_name', 'context')


class AnswerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Answer  # 指定的模型类
        fields = ('pk', 'qid', 'u_name', 'context')
