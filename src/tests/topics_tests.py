# coding=utf-8

import unittest
from src.pageObjects.pageObjects import PageObject

__author__ = 'My'

BASE_URL = 'http://ftest.stud.tech-mail.ru/'

LOGIN = 'ftest17@tech-mail.ru'
USER_NAME = u'Господин Прокурор'

BLOG = 'Флудилка'
TITLE = u'Title'
SHORT_TEXT = u'ShortText'
MAIN_TEXT = u'MainText'
UNORDERED_LIST = '* test\ntest'
ORDERED_LIST = '1. test\ntest'
IMAGE_FROM_NET = '![](http://megafun.name/images/articles/sereznye-koshki-6-foto_1.jpg)'
YANDEX_LINK = '[testing_link](http://ya.ru)'
USER_PROFILE_LINK = u'[Господин Губернатор](/profile/g.gubernator/)'

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
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), MAIN_TEXT)

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), SHORT_TEXT)

        self.page_obj.delete_topic()

    def testCreateTopicWithoutTitle(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.page_obj.save_new_topic()
        self.assertTrue(self.page_obj.is_message_error())

    def testCreateTopicWithoutShortText(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.page_obj.save_new_topic()
        self.assertTrue(self.page_obj.is_message_error())

    def testCreateTopicWithoutMainText(self):
        self.page_obj.create_simple_topic(BLOG, '', SHORT_TEXT, MAIN_TEXT)
        self.page_obj.save_new_topic()
        self.assertTrue(self.page_obj.is_message_error())

    def testShortTextBoldMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_text_bold()
        self.assertEqual(self.page_obj.read_short_message(), '****')
    #
    def testMainTextBoldMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_text_bold()
        self.assertEqual(self.page_obj.read_main_message(), '****')

    def testShortTextItalicMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_text_italic()
        self.assertEqual(self.page_obj.read_short_message(), '**')

    def testMainTextItalicMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_text_italic()
        self.assertEqual(self.page_obj.read_main_message(), '**')

    def testShortTextUnorderedListMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_text_unordered_list()
        self.assertEqual(self.page_obj.read_short_message(), '* test\n* ')

    def testMainTextUnorderedListMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_text_unordered_list()
        self.assertEqual(self.page_obj.read_main_message(), '* test\n* ')

    def testShortTextOrderedListMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_text_ordered_list()
        self.assertEqual(self.page_obj.read_short_message(), '1. test\n2. ')

    def testMainTextOrderedListMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_text_ordered_list()
        self.assertEqual(self.page_obj.read_main_message(), '1. test\n2. ')

    def testShortTextLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_text_link()
        self.assertEqual(self.page_obj.read_short_message(), '[](http://web-site.ru)')

    def testMainTextLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_text_link()
        self.assertEqual(self.page_obj.read_main_message(), '[](http://web-site.ru)')

    def testShortImageLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_image_link()
        self.assertEqual(self.page_obj.read_short_message(), '![](http://image.jpg)')

    def testMainImageLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_image_link()
        self.assertEqual(self.page_obj.read_main_message(), '![](http://image.jpg)')

    def testShortImageUploadMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_image_upload()
        self.assertIn('.jpg', self.page_obj.read_short_message())
    #
    def testMainImageUploadMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_image_upload()
        self.assertIn('.jpg', self.page_obj.read_main_message())

    def testShortUserLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_short_user_link(u'Губернатор')
        self.assertEqual(self.page_obj.read_short_message(), USER_PROFILE_LINK)

    def testMainUserLinkMarkdown(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '', '')
        self.page_obj.make_main_user_link(u'Губернатор')
        self.assertEqual(self.page_obj.read_main_message(), USER_PROFILE_LINK)

    def testCreateTopicWithoutComment(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, SHORT_TEXT, MAIN_TEXT)
        self.page_obj.make_comment_forbidden()
        self.page_obj.save_new_topic()

        self.assertTrue(not self.page_obj.is_comment_available())
        self.page_obj.delete_topic()

    def testCreateTopicWithoutPublishing(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, SHORT_TEXT, MAIN_TEXT)
        self.page_obj.make_not_publish()
        self.page_obj.save_new_topic()

        self.page_obj.open_blog_page()
        self.assertNotEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertNotEqual(self.page_obj.get_topic_text(), SHORT_TEXT)

        self.page_obj.open_page(BASE_URL, '/blog/topics/draft/')
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), SHORT_TEXT)
        self.page_obj.delete_topic()

    def testCreateTopicWithBoldText(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '**' + SHORT_TEXT + '**', '**' + MAIN_TEXT + '**')
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), MAIN_TEXT)
        self.assertTrue(self.page_obj.is_bold_main_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), SHORT_TEXT)
        self.assertTrue(self.page_obj.is_bold_short_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithItalicText(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, '*' + SHORT_TEXT + '*', '*' + MAIN_TEXT + '*')
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), MAIN_TEXT)
        self.assertTrue(self.page_obj.is_italic_main_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertEqual(self.page_obj.get_topic_text(), SHORT_TEXT)
        self.assertTrue(self.page_obj.is_italic_short_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithUnorderedList(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, UNORDERED_LIST, UNORDERED_LIST)
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_unordered_list_main_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_unordered_list_short_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithOrderedList(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, ORDERED_LIST, ORDERED_LIST)
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_ordered_list_main_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_ordered_list_short_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithLink(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, YANDEX_LINK, YANDEX_LINK)
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_link_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_link_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithImage(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, IMAGE_FROM_NET, IMAGE_FROM_NET)
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_image_main_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_image_short_text())

        self.page_obj.delete_topic()

    def testCreateTopicWithUserLink(self):
        self.page_obj.create_simple_topic(BLOG, TITLE, USER_PROFILE_LINK, USER_PROFILE_LINK)
        self.page_obj.save_new_topic()

        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_user_link_text())

        self.page_obj.open_blog_page()
        self.assertEqual(self.page_obj.get_topic_title(), TITLE)
        self.assertTrue(self.page_obj.is_user_link_text())

        self.page_obj.delete_topic()



