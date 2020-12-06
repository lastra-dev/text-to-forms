from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

def find_question_box():
    driver.find_element_by_xpath("//*[@id='SchemaEditor']/div/div[2]/div/div[2]/div[3]/div/div/div/div[1]/div[2]/div["
                                 "2]/div[2]/div[1]/div[1]/span/div/div/div[1]/div[2]/textarea")
