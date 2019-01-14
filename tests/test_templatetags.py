# -*- coding: utf-8 -*-
import six
from django.test import TestCase
from django.template import engines

from django_extensions.templatetags.widont import widont, widont_html

try:
    from unittest.mock import Mock, MagicMock, patch
except ImportError:
    from mock import patch


# TODO: these tests are far from having decent test coverage
class TemplateTagsTests(TestCase):
    def test_widont(self):
        self.assertEqual(widont('Test Value'), 'Test&nbsp;Value')
        self.assertEqual(widont(six.u('Test Value')), six.u('Test&nbsp;Value'))

    def test_widont_html(self):
        self.assertEqual(widont_html('Test Value'), 'Test&nbsp;Value')
        self.assertEqual(widont_html(six.u('Test Value')), six.u('Test&nbsp;Value'))


class DebuggerTagsTests(TestCase):

    """Test class for DebuggerTags."""

    def setUp(self):  # noqa
        self.engine = engines['django']

    def test_pdb_filter(self):
        import pdb
        pdb.set_trace = MagicMock(return_value=None)
        template = self.engine.from_string(
            '''
            {% load debugger_tags %}

            {{ test_object|pdb }}
            '''
        )
        template.render({'test_object': Mock()})
        self.assertTrue(pdb.set_trace.called)
