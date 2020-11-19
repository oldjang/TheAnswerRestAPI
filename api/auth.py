from rest_framework.permissions import BasePermission

from api.models import User, UserToken
from rest_framework.authentication import BaseAuthentication


class UserAuth(BaseAuthentication):
    # 重写认证方法
    def authenticate(self, request):
        # get请求获取数据是才验证权限，post等可能是注册或者登录，应该放开访问权限
        if request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT':
            # request.query_params 这个获取的类型是 django里面的 QueryDict 类型
            token = request.data.get('token')
            print(token)
            try:
                u_name = UserToken.objects.get(u_token=token).u_name
                user = User.objects.get(u_name=u_name)
                print(user)
                return user, token
            except:
                return


class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        # get请求获取数据是才验证权限，post等可能是注册或者登录，应该放开访问权限
        if request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT':
            return isinstance(request.user, User)

        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'DELETE' or request.method == 'PUT':
            return request.user.u_name == obj.u_name or request.user.is_super
        return True


class IsGet(BasePermission):
    def has_permission(self, request, view):
        # get请求获取数据是才验证权限，post等可能是注册或者登录，应该放开访问权限
        if request.method == 'POST' or request.method == 'DELETE' or request.method == 'PUT':
            return False
        return True
