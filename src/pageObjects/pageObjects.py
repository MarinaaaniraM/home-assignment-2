# coding=utf-8
import os
import urlparse
from selenium.webdriver import DesiredCapabilities, Remote, ActionChains
from selenium.webdriver.support.wait import WebDriverWait

__author__ = 'My'

PASSWORD = 'Pa$$w0rD-17'  # TODO

class PageObject():
    def __init__(self):
        browser = os.environ.get('TTHA2BROWSER', 'CHROME')

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
        short_text_element = '//*[@id="content"]/div/div[1]/form/div/div[3]/div[6]/div[1]/div/div/div/div[3]/pre'
        main_text_element = '//*[@id="content"]/div/div[1]/form/div/div[6]/div[6]/div[1]/div/div/div/div[3]/pre'
        create_button_element = '//button[contains(text(),"Создать")]'

        self.driver.find_element_by_class_name('chzn-single').click()
        self.driver.find_element_by_xpath(option_blog_select_element.format(blog_name)).click()
        self.driver.find_element_by_xpath(title_element).send_keys(title)
        self.driver.find_element_by_xpath(short_text_element).click()
        ActionChains(self.driver).send_keys(short_text).perform()
        self.driver.find_element_by_xpath(main_text_element).click()
        ActionChains(self.driver).send_keys(main_text).perform()
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

    def message_error(self):
        error = self.driver.find_element_by_class_name('system-message-error')
        return error.is_displayed()



