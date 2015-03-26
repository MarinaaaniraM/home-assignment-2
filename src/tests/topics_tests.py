# coding=utf-8

import os
import unittest
from pageObjects import pageObjects
from selenium.webdriver import Remote, DesiredCapabilities

__author__ = 'My'


class TopicTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

        USERNAME = u'Господин Прокурор'
        USEREMAIL = 'ftest17@tech-mail.ru'
        PASSWORD = 'Pa$$w0rD-17'

        auth_page = pageObjects.AuthPage(self.driver)
        auth_page.open()

        auth_form = auth_page.form
        auth_form.open_form()
        auth_form.set_login(USEREMAIL)
        auth_form.set_password(PASSWORD)
        auth_form.submit()

        user_name = auth_page.top_menu.get_username()
        self.assertEqual(USERNAME, user_name)


    def tearDown(self):
        self.driver.quit()

    def testCreateSimpleTopic(self):
        BLOG = 'Флудилка'
        TITLE = u'Господин Прокурор написал: Заголовок топика111'
        SHORT_TEXT = u'Господин Прокурор написал: Короткий текст, отображается в блогах!111'
        MAIN_TEXT = u'Господин Прокурор написал: Главный текст, Отображается внутри топика!111'

        create_page = pageObjects.CreatePage(self.driver)
        create_page.open()

        create_form = create_page.form
        create_form.blog_select_open()
        create_form.blog_select_set_option(BLOG)
        create_form.set_title(TITLE)
        create_form.set_short_text(SHORT_TEXT)
        create_form.set_main_text(MAIN_TEXT)
        create_form.submit()

        topic_page = pageObjects.TopicPage(self.driver)
        topic_title = topic_page.topic.get_title()
        topic_text = topic_page.topic.get_text()
        self.assertEqual(TITLE, topic_title)
        self.assertEqual(MAIN_TEXT, topic_text)

        topic_page.topic.open_blog()

        blog_page = pageObjects.BlogPage(self.driver)
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertEqual(TITLE, topic_title)
        self.assertEqual(SHORT_TEXT, topic_text)

        blog_page.topic.delete()
        topic_title = blog_page.topic.get_title()
        topic_text = blog_page.topic.get_text()
        self.assertNotEqual(TITLE, topic_title)
        self.assertNotEqual(SHORT_TEXT, topic_text)