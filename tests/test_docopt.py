#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2009 Benoit Chesneau <benoitc@e-engura.org>
#
# This software is licensed as described in the file LICENSE, which
# you should have received as part of this distribution.

import os
import tempfile
import shutil
import sys
import unittest

from docopt import docopt

from couchapp.errors import ResourceNotFound
from couchapp.client import Database
import couchapp.commands as commands

couchapp_dir = os.path.join(os.path.dirname(__file__), '../')
couchapp_cli = os.path.join(os.path.dirname(__file__), '../bin/couchapp')

class CliTestCase(unittest.TestCase):

    def setUp(self):
        self.startdir = os.getcwd()

    def tearDown(self):
        os.chdir(self.startdir)

    def testUsageHelp(self):
        print commands.usage()
    
    def testDocoptOutput(self):
        parsed = docopt(commands.usage_doc,
                ["push"])
        print parsed
