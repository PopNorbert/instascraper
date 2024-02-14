from dataclasses import dataclass

import selenium.webdriver.chrome.webdriver
from selenium import webdriver
import os
import time
import datetime
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import random
import config
@dataclass
class InstaScraper:
    username:str
    password:str
    ec:EC=EC
    by:By=By

    def __post_init__(self):
        self.webDriverWait = WebDriverWait
        #self.proxy = random.choice(config.ips)
        self.chrome_options = webdriver.ChromeOptions()
        #self.chrome_options.add_argument("--headless")
        #self.chrome_options.add_argument("--disable-gpu")
        self.driver = webdriver.Chrome(options=self.chrome_options)
        time.sleep(1)
        self.login()
        while True:
            pass


    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]')))
        self.driver.find_element(self.by.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]').click()
        time.sleep(2)
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.NAME, 'username')))
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.NAME, 'password')))
        self.webDriverWait(self.driver, 20).until(self.ec.element_to_be_clickable((self.by.XPATH, '//*[contains(text(), "Log in")]')))
        self.driver.find_element(self.by.NAME, 'username').send_keys(self.username)
        self.driver.find_element(self.by.NAME, 'password').send_keys(self.password)
        self.driver.find_element(self.by.XPATH, '//*[contains(text(), "Log in")]').click()
        time.sleep(2)
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div')))
        self.driver.find_element(self.by.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/div/div').click()
        time.sleep(2)
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')))
        self.driver.find_element(self.by.XPATH,'/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click()
        self.webDriverWait(self.driver, 20).until(self.ec.presence_of_element_located((self.by.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div')))
        self.driver.find_element(self.by.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div').click()