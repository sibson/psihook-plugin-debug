from django.http import HttpResponse

import structlog

LOGGER = structlog.get_logger()

SCRUBS = 'AUTHENTICATION', 'AUTHORIZATION', 'COOKIE'


def debug(request):
    headers = {k: request.META[k] for k in request.META if k.startswith('HTTP') and k not in SCRUBS}
    LOGGER.debug('request', method=request.method, path=request.path, headers=headers)

    return HttpResponse()
