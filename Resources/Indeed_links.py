# import libraries 
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
from selenium.common.exceptions import NoSuchWindowException
from Resources.web_driver import web_driver
import datetime
import logging
import smtplib
import re
import pandas as pd

def indeed_link(driver,link):
    job_links = []
    try:
        #driver.implicitly_wait(5)
        driver.get(link)
    except (NoSuchWindowException):
        driver = web_driver()
        driver.implicitly_wait(5)
        driver.get(link)

    #scrolling down the entire page
    SCROLL_PAUSE_TIME = 3
    last_height = driver.execute_script('return document.body.scrolHeight')
    for i in range(4):
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight);') 
        time. sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script('return document.body.scrollHeight')
        last_height = new_height
#Beautifulsoup is used to prepare the data for scraping 
    src=driver.page_source 
    soup=BeautifulSoup(src,'lxml')
    job_div= soup.find_all('a', {'class': "jcs-JobTitle"}) 
    for i in range (0, len(job_div)):
        print(i)
        each_link='https://ca.indeed.com'+ job_div[i]['href']
        print(each_link)
        job_links.append(each_link)
    return (driver,job_links)