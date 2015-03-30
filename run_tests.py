#!/usr/bin/env python2

import sys
import unittest
from src.tests.topics_tests import TopicTest


if __name__ == '__main__':
    suite = unittest.TestSuite((
        unittest.makeSuite(TopicTest),
    ))
    result = unittest.TextTestRunner().run(suite)
    sys.exit(not result.wasSuccessful())
