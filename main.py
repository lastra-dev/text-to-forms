from platform import system
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

import constants


def add_question():
    """Locates and clicks on add question button in browser"""

    add_question_button = driver.find_element_by_xpath(constants.ADD_QUESTION_BUTTON)
    add_question_button.click()


def send_info(a_location, index_in_location, info_to_send):
    """Locates element in browser and sends information

    Gets element from list of elements and send information to that element

    Parameters
    ----------
    a_location : str
        Xpath location of the elements
    index_in_location : int
        Index of element in the location
    info_to_send : str
        Information to send to the element in the location
    """

    elements = driver.find_elements_by_xpath(a_location)
    # if first answer
    if index_in_location == -2:
        # click needed to clear answer box, .clear() not working...
        elements[index_in_location].click()
    elements[index_in_location].send_keys(info_to_send)
    # necessary time for google forms to finish entering the text
    sleep(0.5)


def make_list_with(a_file) -> list:
    """Fills list in which questions are taken to fill Google form

    :param string a_file: should be a file with questions separated with blank lines
    """

    result = []
    with open(a_file, "r", encoding="utf8") as text:
        for line in text:
            if '\n' in line:
                # avoids return
                result.append(line[:-1])
            else:
                result.append(line)
    return result


def chromedriver_path_of(system_name) -> str:
    """Gets system name and returns a string path

    :param string system_name: should be "Windows", "Linux" or "Darwin".
    System name can be obtained from "platform" module and "system" function
    """

    if system_name == 'Windows':
        return "./chromedriver.exe"
    else:
        return "./chromedriver"


########################################################################


def main_loop():
    print("Adding questions...\n")
    add_question()
    # necessary booleans to change input location
    new_question = True
    first_answer = False
    # questions counter to print while process is running
    questions_count = 0

    for info in questions:
        if not info:
            # adds a new question when blank line found
            add_question()
            new_question = True
            questions_count += 1
            print(str(questions_count) + " questions added")
        elif new_question:
            # adds info in question box
            send_info(constants.QUESTION_BOX, -1, info)
            new_question = False
            first_answer = True
        elif first_answer:
            # adds info in first answer box
            send_info(constants.ANSWER_BOX, -2, info)
            first_answer = False
        else:
            # adds info in the rest of the answer boxes
            send_info(constants.ANSWER_BOX, -1, info)

    print(str(questions_count + 1) + " questions added\n")


if __name__ == "__main__":
    print(constants.MENU)
    try:
        driver = webdriver.Chrome(executable_path=chromedriver_path_of(system()))
        driver.get("https://docs.google.com/forms/")
        questions = make_list_with("questions.txt")
    except WebDriverException:
        print("ERROR: Make sure to have chromedriver inside the root of the project, Chrome installed,\n"
              "both programs on the same version, and do not close the browser window.\n")
    except FileNotFoundError:
        print("ERROR: Make sure to have questions.txt inside the root of the project and add questions to it.\n")
    else:
        print(str(questions.count('') + 1) + " questions to add.")
        input("Hit Enter when you get to your Google form...\n")
        try:
            main_loop()
        except WebDriverException:
            print("ERROR: Try running the program again.\n")
    input("Process finished, press Enter to exit...")
