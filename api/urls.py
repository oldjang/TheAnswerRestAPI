from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from api import views
from api.views import LoginView, RegisterView, QuestionViewSet

route = routers.DefaultRouter()

# 注册新的路由地址
route.register(r'question', views.QuestionViewSet)
route.register(r'answer', views.AnswerViewSet)

urlpatterns = [
    url(r'^login/$', LoginView.as_view()),
    url(r'^register/$', RegisterView.as_view()),
    url(r'^answerset/(?P<pk>.+)/$', views.AnswerSetViewSet.as_view()),
    url('', include(route.urls)),
]
