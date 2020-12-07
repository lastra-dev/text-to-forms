from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()


def new_question():
    time.sleep(0.5)
    add_question_button = driver.find_element_by_xpath("//*[@id='SchemaEditor']/div/div[1]/div/div/div[1]/div/span")
    add_question_button.click()


def send_tab():
    time.sleep(0.5)
    tab_action = ActionChains(driver)
    tab_action.send_keys(Keys.TAB)
    tab_action.perform()


def send_info(info):
    time.sleep(0.5)
    info_action = ActionChains(driver)
    info_action.send_keys(info)
    info_action.perform()


def add_new_question(question, a, b, c, d):
    new_question()
    send_info(question)
    send_tab()
    send_tab()
    send_tab()
    send_info(a)
    send_info(b)
    send_info(c)
    send_info(d)


def main_loop():
    for i in range(0, len(lines), 5):
        add_new_question(lines[i], lines[i+1], lines[i+2], lines[i+3], lines[i+4])


lines = []
with open("questions.txt", "r", encoding="utf8") as file:
    for line in file:
        lines.append(line)
