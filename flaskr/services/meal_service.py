import time
from selenium import webdriver
from flaskr.models.meal import Meal


def retrieveMealByMealName(name: str):
    # Optional argument, if not specified will search path.
    driver = webdriver.Chrome()

    driver.get('http://www.youtube.com/')
    # Let the user actually see something!
    #driver.quit()


def sendMealToMyFitnessPal(meal: Meal):
    return True
