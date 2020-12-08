from selenium import webdriver
import time

driver = webdriver.Chrome()


def add_question():
    add_question_button = driver.find_element_by_xpath("//*[@id='SchemaEditor']/div/div[1]/div/div/div[1]/div/span")
    add_question_button.click()


def send_info(xpath, i, text):
    elements = driver.find_elements_by_xpath(xpath)
    if i == -2:  # if first answer
        elements[i].click()  # click needed to clear answer box, clear() function not working in this line
    elements[i].send_keys(text)
    time.sleep(0.5)  # necessary time for google forms to finish entering the text


def main_loop():
    for i in range(0, len(lines), 5):
        add_question()
        send_info("//textarea[@class='appsMaterialWizTextinputTextareaInput exportTextarea']", -1, lines[i])
        send_info("//input[@class='quantumWizTextinputSimpleinputInput exportInput']", -2, lines[i+1])
        send_info("//input[@class='quantumWizTextinputSimpleinputInput exportInput']", -1, lines[i+2])
        send_info("//input[@class='quantumWizTextinputSimpleinputInput exportInput']", -1, lines[i+3])
        send_info("//input[@class='quantumWizTextinputSimpleinputInput exportInput']", -1, lines[i+4])


lines = []
with open("questions.txt", "r", encoding="utf8") as file:
    for line in file:
        if '\n' in line:
            lines.append(line[:-1])  # avoids enter
        else:
            lines.append(line)
