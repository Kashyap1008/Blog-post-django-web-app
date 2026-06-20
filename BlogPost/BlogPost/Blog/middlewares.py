import logging

logger = logging.getLogger(__name__)


class RequestLoggingMiddleware :
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        logger.info(f"{request.user} | {request.method} | {request.path}")

        response = self.get_response(request)

        return response
    

class VisitorIPMiddleware:
    def __init__(self,get_response):
        self.get_response = get_response

    def __call__(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')

        if x_forwarded_for :
            ip = x_forwarded_for.split(',')[0].strip()

        else:
            ip =request.META.get('REMOTE_ADDR')        

        request.ip_address = ip

        return self.get_response(request)