from selenium import webdriver
import xpath
import time

driver = webdriver.Chrome()


def add_question():
    """Locates and clicks on add question button in browser"""

    add_question_button = driver.find_element_by_xpath(xpath.ADD_QUESTION_BUTTON)
    add_question_button.click()


def send_info(location, element, info):
    """Locates element in browser and sends information

    Gets a list of elements passed by an xpath location in the browser.
    It then sends information to the n-element of that list.
    If the element is the first answer option in google forms it gets
    clicked in order to get cleared, this is because
    elements[element].clear() is not working here.
    """

    elements = driver.find_elements_by_xpath(location)
    # if first answer
    if element == -2:
        # click needed to clear answer box
        elements[element].click()
    elements[element].send_keys(info)
    # necessary time for google forms to finish entering the text
    time.sleep(0.5)


def fill_list():
    """Fills list in which questions are taken to fill Google form"""

    with open("questions.txt", "r", encoding="utf8") as file:
        for line in file:
            if '\n' in line:
                # avoids return
                questions.append(line[:-1])
            else:
                questions.append(line)


def main_loop():
    add_question()
    new_question = True
    first_answer = False
    n_questions = 0

    for info in questions:
        if not info:
            add_question()
            new_question = True
            n_questions += 1
            print(str(n_questions) + " questions added")
        elif new_question:
            send_info(xpath.QUESTION_BOX, -1, info)
            new_question = False
            first_answer = True
        elif first_answer:
            send_info(xpath.ANSWER_BOX, -2, info)
            first_answer = False
        else:
            send_info(xpath.ANSWER_BOX, -1, info)

    print(str(n_questions + 1) + " questions added\n")


########################################################################


print("--------------------------------------------\n"
      "            SELENIUM EXAM FILLER\n"
      "--------------------------------------------\n"
      "More info: https://github.com/oscaragl13/selenium-exam-filler\n")


questions = []
fill_list()

print(str(questions.count('') + 1) + " questions to add.")
input("Hit Enter when you get to your Google form...\n")
main_loop()
input("Process finished, press Enter to exit...")
