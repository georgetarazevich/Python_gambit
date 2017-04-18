# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

success = True
wd = WebDriver()
wd.implicitly_wait(60)

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

try:
    wd.get("https://www.tut.by/")
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//html")).perform()
    wd.find_element_by_xpath("//html").click()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("body")).perform()
    wd.find_element_by_css_selector("button.button.rubric__button").click()
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@class='b-top-c']/div[1]/div")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.header._title")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("Кража денег из сейфа произошла на Революционной, 3. По этому адресу расположен ГУБОПиК МВД Беларуси. 8 января было воскресенье, а значит, скорее всего, войти в это здание мог только штатный сотрудник силовой структуры. Затем подозреваемый уехал в Украину, а потом – в Румынию.")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='title_news_block']/div[3]")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_link_text("Кража денег из сейфа произошла на Революционной, 3. По этому адресу расположен ГУБОПиК МВД Беларуси. 8 января было воскресенье, а значит, скорее всего, войти в это здание мог только штатный сотрудник силовой структуры. Затем подозреваемый уехал в Украину, а потом – в Румынию.")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_xpath("//div[@id='title_news_block']/div[1]")).perform()
    ActionChains(wd).move_to_element(wd.find_element_by_css_selector("span.header._title")).perform()
finally:
    wd.quit()
    if not success:
        raise Exception("Test failed.")
