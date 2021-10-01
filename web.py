from selenium import webdriver
from time import sleep


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        sleep(2)


InstaBot()
