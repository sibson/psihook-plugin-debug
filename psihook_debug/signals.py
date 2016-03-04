import django.dispatch


class DebugSender(object):
    """ A placeholder for sender in signals """


psihook_debug = django.dispatch.Signal(providing_args=['method', 'path', 'headers', 'payload'])
