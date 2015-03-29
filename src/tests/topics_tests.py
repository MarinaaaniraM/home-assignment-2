# coding=utf-8

import unittest
from pageObjects.pageObjects import PageObject

__author__ = 'My'

BASE_URL = 'http://ftest.stud.tech-mail.ru/'

LOGIN = 'ftest17@tech-mail.ru'
USER_NAME = u'Господин Прокурор'

BLOG = 'Флудилка'
TITLE = u'Title'
SHORT_TEXT = u'ShortText'
MAIN_TEXT = u'MainText'


class TopicTest(unittest.TestCase):

    def setUp(self):
        self.page_obj = PageObject()
        self.page_obj.open_page(BASE_URL, '')
        self.assertEqual(self.page_obj.authorization(LOGIN), USER_NAME)

        self.page_obj.open_page(BASE_URL, '/blog/topic/create/')

    def tearDown(self):
        self.page_obj.close_driver()

    def testCreateSimpleTopic(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, SHORT_TEXT, MAIN_TEXT)

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), MAIN_TEXT)

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), SHORT_TEXT)

        self.page_obj.delete_topic()

    def testCreateTopicWithoutTitle(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.assertTrue(self.page_obj.message_error())

    def testCreateTopicWithoutShortText(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.assertTrue(self.page_obj.message_error())

    def testCreateTopicWithoutMainText(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.assertTrue(self.page_obj.message_error())


