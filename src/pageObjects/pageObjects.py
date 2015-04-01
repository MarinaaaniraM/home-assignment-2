# coding=utf-8
import os
import urlparse
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

__author__ = 'My'

PASSWORD = os.environ['TTHA2PASSWORD']

dir = os.path.dirname(__file__)
filename = os.path.join(dir, '../../cat.jpg')
LOCAL_PICTURE = os.path.join(dir, '../../cat.jpg')


class PageObject():
    def __init__(self):
        browser = os.environ.get('TTHA2BROWSER', 'FIREFOX')

        self.driver = Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy())

    def close_driver(self):
        self.driver.quit()

    def open_page(self, base_url, path):
        url = urlparse.urljoin(base_url, path)
        self.driver.get(url)
        self.driver.maximize_window()

    def authorization(self, login):
        login_element = '//input[@name="login"]'
        password_element = '//input[@name="password"]'
        submit_element = '//span[text()="Войти"]'
        login_button_element = '//a[text()="Вход для участников"]'
        username_element = '//a[@class="username"]'

        self.driver.find_element_by_xpath(login_button_element).click()
        self.driver.find_element_by_xpath(login_element).send_keys(login)
        self.driver.find_element_by_xpath(password_element).send_keys(PASSWORD)
        self.driver.find_element_by_xpath(submit_element).click()

        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(username_element).text)

    def create_simple_topic(self, blog_name, title, short_text, main_text):
        option_blog_select_element = '//li[text()="{}"]'
        title_element = '//input[@name="title"]'
        short_text_element = '(//div[@class="CodeMirror-code"])[1]'

        main_text_element = '(//div[@class="CodeMirror-code"])[2]'

        self.driver.find_element_by_class_name('chzn-single').click()
        self.driver.find_element_by_xpath(option_blog_select_element.format(blog_name)).click()
        self.driver.find_element_by_xpath(title_element).send_keys(title)
        self.driver.find_element_by_xpath(short_text_element).click()
        ActionChains(self.driver).send_keys(short_text).perform()
        self.driver.find_element_by_xpath(main_text_element).click()
        ActionChains(self.driver).send_keys(main_text).perform()

    def save_new_topic(self):
        create_button_element = '//button[contains(text(),"Создать")]'
        self.driver.find_element_by_xpath(create_button_element).submit()

    def get_topic_title(self):
        title_element = '//*[@class="topic-title"]/a'
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(title_element).text)

    def get_topic_text(self):
        short_text_element = '//*[@class="topic-content text"]/p'
        return WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(short_text_element).text)

    def open_blog_page(self):
        self.driver.find_element_by_class_name('topic-blog').click()

    def delete_topic(self):
        delete_button_confirm_element = '//input[@value="Удалить"]'
        self.driver.find_element_by_class_name('actions-delete').click()
        self.driver.find_element_by_xpath(delete_button_confirm_element).click()

    def is_message_error(self):
        return self.driver.find_element_by_class_name('system-message-error').is_displayed()

    def read_short_message(self):
        short_text_element = '(//div[@class="CodeMirror-code"])[1]'
        return WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, short_text_element))).text

    def read_main_message(self):
        main_text_element = '(//div[@class="CodeMirror-code"])[2]'
        return WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, main_text_element))).text

    def make_short_text_bold(self):
        short_text_bold_element = '(//a[@class="markdown-editor-icon-bold"])[1]'
        self.driver.find_element_by_xpath(short_text_bold_element).click()

    def make_main_text_bold(self):
        main_text_bold_element = '(//a[@class="markdown-editor-icon-bold"])[2]'
        self.driver.find_element_by_xpath(main_text_bold_element).click()

    def make_short_text_italic(self):
        short_text_italic_element = '(//a[@class="markdown-editor-icon-italic"])[1]'
        self.driver.find_element_by_xpath(short_text_italic_element).click()

    def make_main_text_italic(self):
        main_text_italic_element = '(//a[@class="markdown-editor-icon-italic"])[2]'
        self.driver.find_element_by_xpath(main_text_italic_element).click()

    def make_short_text_unordered_list(self):
        short_text_unordered_list_element = '(//a[@class="markdown-editor-icon-unordered-list"])[1]'
        self.driver.find_element_by_xpath(short_text_unordered_list_element).click()
        ActionChains(self.driver).send_keys('test').perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def make_main_text_unordered_list(self):
        main_text_unordered_list_element = '(//a[@class="markdown-editor-icon-unordered-list"])[2]'
        self.driver.find_element_by_xpath(main_text_unordered_list_element).click()
        ActionChains(self.driver).send_keys('test').perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def make_short_text_ordered_list(self):
        short_text_ordered_list_element = '(//a[@class="markdown-editor-icon-ordered-list"])[1]'
        self.driver.find_element_by_xpath(short_text_ordered_list_element).click()
        ActionChains(self.driver).send_keys('test').perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def make_main_text_ordered_list(self):
        main_text_ordered_list_element = '(//a[@class="markdown-editor-icon-ordered-list"])[2]'
        self.driver.find_element_by_xpath(main_text_ordered_list_element).click()
        ActionChains(self.driver).send_keys('test').perform()
        ActionChains(self.driver).send_keys(Keys.ENTER).perform()

    def make_short_text_link(self):
        short_text_link_element = '(//a[@class="markdown-editor-icon-link"])[1]'
        self.driver.find_element_by_xpath(short_text_link_element).click()
        self.driver.switch_to.alert.send_keys('http://web-site.ru')
        self.driver.switch_to.alert.accept()

    def make_main_text_link(self):
        main_text_link_element = '(//a[@class="markdown-editor-icon-link"])[3]'
        self.driver.find_element_by_xpath(main_text_link_element).click()
        self.driver.switch_to.alert.send_keys('http://web-site.ru')
        self.driver.switch_to.alert.accept()

    def make_short_image_link(self):
        short_image_link_element = '(//a[@class="markdown-editor-icon-image"])[1]'
        self.driver.find_element_by_xpath(short_image_link_element).click()
        self.driver.switch_to.alert.send_keys('http://image.jpg')
        self.driver.switch_to.alert.accept()

    def make_main_image_link(self):
        main_image_link_element = '(//a[@class="markdown-editor-icon-image"])[3]'
        self.driver.find_element_by_xpath(main_image_link_element).click()
        self.driver.switch_to.alert.send_keys('http://image.jpg')
        self.driver.switch_to.alert.accept()

    def make_short_image_upload(self):
        self.driver.execute_script('$(".markdown-upload-photo-container").show()')
        short_text_image_upload_element = '(//input[@name="filedata"])[1]'
        short_text_image_upload_contains_text = '//div[@class="CodeMirror-code" and contains(., ".jpg")]'
        self.driver.find_element_by_xpath(short_text_image_upload_element).send_keys(LOCAL_PICTURE)

        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, short_text_image_upload_contains_text)))

    def make_main_image_upload(self):
        self.driver.execute_script('$(".markdown-upload-photo-container").show()')
        main_text_image_upload_element = '(//input[@name="filedata"])[2]'
        main_text_image_upload_contains_text = '//div[@class="CodeMirror-code" and contains(., ".jpg")]'
        self.driver.find_element_by_xpath(main_text_image_upload_element).send_keys(LOCAL_PICTURE)

        WebDriverWait(self.driver, 30, 0.1).until(
            expected_conditions.presence_of_element_located((By.XPATH, main_text_image_upload_contains_text)))

    def make_short_user_link(self, user_name):
        short_user_link_element = '(//a[@class="markdown-editor-icon-link"])[2]'
        self.driver.find_element_by_xpath(short_user_link_element).click()
        find_user_element = '//*[@id="search-user-login-popup"]'
        self.driver.find_element_by_xpath(find_user_element).send_keys(user_name)

        choose_user_element = '//a[text()="Господин Губернатор"]'
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(choose_user_element)).click()

    def make_main_user_link(self, user_name):
        short_user_link_element = '(//a[@class="markdown-editor-icon-link"])[4]'
        self.driver.find_element_by_xpath(short_user_link_element).click()
        find_user_element = '//*[@id="search-user-login-popup"]'
        self.driver.find_element_by_xpath(find_user_element).send_keys(user_name)

        choose_user_element = '//a[text()="Господин Губернатор"]'
        WebDriverWait(self.driver, 30, 0.1).until(
            lambda d: d.find_element_by_xpath(choose_user_element)).click()

    def make_comment_forbidden(self):
        comment_checkbox_element = '//*[@id="id_forbid_comment"]'
        self.driver.find_element_by_xpath(comment_checkbox_element).click()

    def is_comment_available(self):
        try:
            return self.driver.find_element_by_class_name('comment-add-link').is_displayed()
        except NoSuchElementException:
            return False

    def make_not_publish(self):
        comment_checkbox_element = '//*[@id="id_publish"]'
        self.driver.find_element_by_xpath(comment_checkbox_element).click()

    def is_bold_short_text(self):
        short_text_bold_element = '//*[@class="topic-content text"]/p/strong'
        try:
            return self.driver.find_element_by_xpath(short_text_bold_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_bold_main_text(self):
        main_text_bold_element = '//*[@class="topic-content text"]/p/strong'
        try:
            return self.driver.find_element_by_xpath(main_text_bold_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_italic_short_text(self):
        short_text_italic_element = '//*[@class="topic-content text"]/p/em'
        try:
            return self.driver.find_element_by_xpath(short_text_italic_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_italic_main_text(self):
        main_text_italic_element = '//*[@class="topic-content text"]/p/em'
        try:
            return self.driver.find_element_by_xpath(main_text_italic_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_unordered_list_short_text(self):
        short_text_unordered_list_element = '//*[@class="topic-content text"]/ul'
        try:
            return self.driver.find_element_by_xpath(short_text_unordered_list_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_unordered_list_main_text(self):
        main_text_unordered_list_element = '//*[@class="topic-content text"]/ul'
        try:
            return self.driver.find_element_by_xpath(main_text_unordered_list_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_ordered_list_short_text(self):
        short_text_ordered_list_element = '//*[@class="topic-content text"]/ol'
        try:
            return self.driver.find_element_by_xpath(short_text_ordered_list_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_ordered_list_main_text(self):
        main_text_ordered_list_element = '//*[@class="topic-content text"]/ol'
        try:
            return self.driver.find_element_by_xpath(main_text_ordered_list_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_link_text(self):
        try:
            return self.driver.find_element_by_link_text('testing_link').is_displayed()
        except NoSuchElementException:
            return False

    def is_image_short_text(self):
        short_text_image_element = '//*[@class="topic-content text"]/p/img'
        try:
            return self.driver.find_element_by_xpath(short_text_image_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_image_main_text(self):
        main_text_image_element = '//*[@class="topic-content text"]/p/img'
        try:
            return self.driver.find_element_by_xpath(main_text_image_element).is_displayed()
        except NoSuchElementException:
            return False

    def is_user_link_text(self):
        try:
            return self.driver.find_element_by_link_text(u'Господин Губернатор').is_displayed()
        except NoSuchElementException:
            return False








