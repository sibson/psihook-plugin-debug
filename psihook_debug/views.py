from __future__ import absolute_import

import json

from django.http import HttpResponse


from .signals import psihook_debug, DebugSender


SCRUBS = 'HTTP_AUTHENTICATION', 'HTTP_AUTHORIZATION', 'HTTP_COOKIE'


def default(request):
    headers = {k: request.META[k] if k not in SCRUBS else '***' for k in request.META if k.startswith('HTTP')}

    kwargs = {
        'path': request.path,
        'method': request.method,
        'headers': headers,
    }
    if not request.body:
        kwargs['payload'] = None
    elif request.META.get('CONTENT_TYPE') == 'text/json':
        try:
            kwargs['payload'] = json.loads(request.body)
        except ValueError:
            return HttpResponse(status=400)
    else:
        kwargs['payload'] = request.POST or request.GET

    psihook_debug.send_robust(DebugSender, **kwargs)

    return HttpResponse()
