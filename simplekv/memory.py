#!/usr/bin/env python
# coding=utf8

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

from . import KeyValueStorage


class DictStore(KeyValueStorage):
    """Store data in a dictionary.

    This store uses a dictionary as the backend for storing, its implementation
    is straightforward. The dictionary containing all data is available as `d`.
    """
    def __init__(self, d=None):
        self.d = d or {}

    def _open(self, key):
        return StringIO(self.d[key])

    def _put_file(self, key, file):
        self.d[key] = file.read()
        return key
