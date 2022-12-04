import json
from typing import Callable
import logging
from rest_framework.response import Response

class LoggingMiddleware:
    
    def __init__(self, get_response: Callable):
        self.get_response = get_response
        self.request_logger = logging.getLogger('middleware.request')
        self.response_logger = logging.getLogger('middleware.response')

    def __call__(self, request):
        self.request_logger.info('request received', extra={
            'user' : json.dumps({
                'id': request.user.id,
                'username': request.user.username,
                }),
            'path': request.path,
            'body': json.dumps(request.POST),
        })
        
        response: Response = self.get_response(request)
        
        if response.status_code > 299:
            self.response_logger.info('response received', extra={
                'user' : json.dumps({
                    'id': request.user.id,
                    'username': request.user.username,
                    }),
                'path': request.path,
                'status': response.status_code,
                'body': json.dumps(response.__dict__.get('data', {})),
            })
        
        return response