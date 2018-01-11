from selene import browser
from selene.browser import open_url
from selene.support.jquery_style_selectors import s, ss
from selene.support.conditions import have
from selenium import webdriver


class GooglePage(object):
    def open(self):
        open_url("http://google.com/ncr")
        return self

    def search(self, text):
        s("[name='q']").set(text).press_enter()
        return SearchResultsPage()


class SearchResultsPage(object):
    def __init__(self):
        self.results = ss(".srg .g")


def setup_module(module):
    driver = webdriver.Remote(
        command_executor='http://192.168.124.44:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome',
                              'javascriptEnabled': True})
    browser.set_driver(driver)


def teardown_module(module):
    browser.quit()


def test_rambler_search():
    google = GooglePage().open()
    search = google.search("selene")
    search.results[0].should(have.text("In Greek mythology, Selene is the goddess of the moon"))  # :D


def test_rambler_search2():
    google = GooglePage().open()
    search = google.search("selene2")
    search.results[0].should(have.text("In Greek mythology, Selene is the goddess of the moon"))  # :D