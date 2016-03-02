.. image:: https://img.shields.io/travis/sibson/psihook-plugin-debug.svg   :target: https://travis-ci.org/sibson/psihook-plugin-debug/

PsiHook Debug
===============

PsiHook Debug is a simple `PsiHook <https://github.com/sibson/psihook>`_ plugin that can either be used as a template for new plugins or to debug other webhooks. 

Quick start
-----------

1. Add "psihook_debug" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'psihook_debug',
    ]

2. Include the debughook URLconf in your project urls.py like this::

    url(r'^debug/', include('psihook_debug.urls')),

3. Start the development server and trigger a call to visit http://127.0.0.1:8000/debug/
