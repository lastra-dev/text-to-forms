from selenium import webdriver
import xpath
import time


driver = webdriver.Chrome()


def add_question():
    add_question_button = driver.find_element_by_xpath(xpath.ADD_QUESTION_BUTTON)
    add_question_button.click()


def send_info(location, element, info):
    elements = driver.find_elements_by_xpath(location)
    if element == -2:  # if first answer
        elements[element].click()  # click needed to clear answer box, clear() function not working in this line
    elements[element].send_keys(info)
    time.sleep(0.5)  # necessary time for google forms to finish entering the text


def main_loop():
    add_question()
    new_question = True
    first_answer = False

    for info in lines:
        if not info:
            add_question()
            new_question = True
        elif new_question:
            send_info(xpath.QUESTION_BOX, -1, info)
            new_question = False
            first_answer = True
        elif first_answer:
            send_info(xpath.ANSWER_BOX, -2, info)
            first_answer = False
        else:
            send_info(xpath.ANSWER_BOX, -1, info)


lines = []
with open("questions.txt", "r", encoding="utf8") as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])  # avoids return
        else:
            lines.append(line)
