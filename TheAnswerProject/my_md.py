from django.utils.deprecation import MiddlewareMixin


class CORSMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response['Access-Control-Allow-Origin'] = '*'
        # 如果是简单请求这样即可，但是我们一般方送json格式的数据，还有可能会有其他method,所有还要进一步判断
        if request.method == 'OPTIONS':
            # 复杂请求会先发预检
            response["Access-Control-Allow-Headers"] = "Content-Type,token"
            response["Access-Control-Allow-Methods"] = "PUT,PATCH,DELETE,POST"
        return response
