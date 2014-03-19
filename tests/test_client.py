# -*- coding: utf-8 -*-
#
# Copyright 2008,2009 Benoit Chesneau <benoitc@e-engura.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at#
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import unittest2 as unittest
import tempfile
import os
from shutil import rmtree

import json
import unittest2 as unittest
from testconfig import config

from couchapp.client import Database
from couchapp.errors import ResourceNotFound

try:
    url = config['host']['url']
except KeyError:
    url = 'http://localhost:5984/'


class ClientTests(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDatabaseSetup(self):
        # couchapp-test db should not be created yet
        db = Database('%scouchapp-test' % url, create=False)
        self.assertRaises(ResourceNotFound, db.info)
        # create couchapp-test db using default create status
        db = Database('%scouchapp-test' % url)
        db_info = db.info()
        self.assertIsInstance(db_info, dict)


if __name__ == '__main__':
    unittest.main()
