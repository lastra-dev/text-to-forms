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
    for i in range(0, len(lines), 5):
        add_question()
        send_info(xpath.QUESTION_BOX, -1, lines[i])
        send_info(xpath.ANSWER_BOX, -2, lines[i+1])
        send_info(xpath.ANSWER_BOX, -1, lines[i+2])
        send_info(xpath.ANSWER_BOX, -1, lines[i+3])
        send_info(xpath.ANSWER_BOX, -1, lines[i+4])


lines = []
with open("questions.txt", "r", encoding="utf8") as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])  # avoids return
        else:
            lines.append(line)
