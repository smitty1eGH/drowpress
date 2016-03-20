# -*- coding: utf-8 -*-

import os
import sys
sys.path.append('/home/smitty/proj/drowpress/app')

import unittest
from   flask    import request
from   app      import app

class AppTest(unittest.TestCase):
    """Does the thing work?
    
    """
    def setUp(self):
        self.app = app.test_client()

    def test_homepage_works(self):
        response = sefl.app.get("/")
        self.assertEqual(response.status_code, 200)
        
if __name__ == '__main__':
    unittest.main()
        
