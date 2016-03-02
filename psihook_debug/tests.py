from __future__ import absolute_import

import json
from unittest import TestCase
from mock import patch

from django.test import RequestFactory
from django.http import QueryDict

from . import views, signals


class DefaultViewTestCase(TestCase):
    def setUp(self):
        super(DefaultViewTestCase, self).setUp()
        self.factory = RequestFactory(HTTP_AUTHORIZATION='secret')
        self.params = {
            'app': 'testapp',
            'user': 'testuser@example.com',
            'url': 'https://testapp.example.com',
            'head': '12345',
            'head_long': '1234567890abcdef',
            'git_log': 'test changes',
            'release': '11',
        }
        self.headers = {
            'HTTP_COOKIE': '***',
            'HTTP_AUTHORIZATION': '***',
        }

    @patch('psihook_debug.signals.psihook_debug.send_robust')
    def test_sends_signal(self, signal):
        req = self.factory.post('/debug/webhook', self.params)

        resp = views.default(req)
        self.assertEqual(resp.status_code, 200)

        expected = QueryDict(mutable=True)
        expected.update(self.params)

        signal.assert_called_once_with(signals.DebugSender, path='/debug/webhook', method='POST', headers=self.headers, payload=expected)

    @patch('psihook_debug.signals.psihook_debug.send_robust')
    def test_sends_signal_json(self, signal):
        req = self.factory.post('/debug/webhook', json.dumps(self.params), content_type='text/json')
        resp = views.default(req)
        self.assertEqual(resp.status_code, 200)

        signal.assert_called_once_with(signals.DebugSender, path='/debug/webhook', method='POST', headers=self.headers, payload=self.params)

    @patch('psihook_debug.signals.psihook_debug.send_robust')
    def test_scrubs_headers(self, signal):
        req = self.factory.post('/debug/webhook', self.params)

        resp = views.default(req)
        self.assertEqual(resp.status_code, 200)

        args, kwargs = signal.call_args
        self.assertNotEqual(kwargs['headers']['HTTP_AUTHORIZATION'], 'secret')
