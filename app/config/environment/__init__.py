#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import importlib

env = os.environ.get('DECANTER_ENV', 'devel')

try:
    import_string = "from %s import *" % env
    exec import_string
except ImportError as error:
    print "Settings file not found for %s environment." % env
    exit(1)
