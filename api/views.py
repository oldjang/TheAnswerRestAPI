import time
from django.http import JsonResponse
from rest_framework import viewsets, generics
from rest_framework.views import APIView

from api import models
from api.auth import UserAuth, IsSuperUser, IsGet
from api.models import User, Question, Answer
from api.serializers import QuestionSerializers, AnswerSerializers


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        # 设置一个默认的返回参数
        ret = {'code': 1000, 'msg': None}
        print("OK")
        username = request.data.get('username')
        password = request.data.get('password')
        obj = models.User.objects.filter(u_name=username, u_password=password).first()
        if not obj:
            ret['code'] = '1001'
            ret['msg'] = '用户名或者密码错误'
            return JsonResponse(ret)

        token = str(time.time()) + username
        models.UserToken.objects.update_or_create(u_name=username, defaults={'u_token': token})
        ret['msg'] = '登录成功'
        ret['token'] = token
        return JsonResponse(ret)


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        # 设置一个默认的返回参数
        ret = {'code': 1000, 'msg': None}
        username = request.data.get('username')
        password = request.data.get('password')
        obj = models.User.objects.filter(u_name=username).first()
        if obj:
            ret['code'] = '1001'
            ret['msg'] = '用户名已被注册'
            return JsonResponse(ret)

        user = User(u_name=username, u_password=password)
        user.save()
        token = str(time.time()) + username
        models.UserToken.objects.update_or_create(u_name=username, defaults={'u_token': token})
        ret['msg'] = '注册成功'
        ret['token'] = token
        return JsonResponse(ret)


class QuestionViewSet(viewsets.ModelViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (IsSuperUser,)
    queryset = Question.objects.all().order_by('-pk')
    serializer_class = QuestionSerializers


class AnswerSetViewSet(generics.ListAPIView):
    authentication_classes = (UserAuth,)
    permission_classes = (IsSuperUser, IsGet,)
    serializer_class = AnswerSerializers

    def get_queryset(self):
        qid = self.kwargs['pk']
        return Answer.objects.filter(qid=qid)


class AnswerViewSet(viewsets.ModelViewSet):
    authentication_classes = (UserAuth,)
    permission_classes = (IsSuperUser,)
    queryset = Answer.objects.all().order_by('-pk')
    serializer_class = AnswerSerializers
