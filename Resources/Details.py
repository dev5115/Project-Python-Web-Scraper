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

def details(driver,links_page):
    data = pd.DataFrame(columns = ['Job_title','Company','Salary','time_saved'])
    #go to the link
    for each in links_page:
        print(each)
        driver.get(each)
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
        print(data)
        try:
            title = soup.find('h1', {'class': "jobsearch-JobInfoHeader-title css-1hwk56k e1tiznh50"}).find('span').get_text()
        except:
            title = 'nan'
        try:
            company = soup.find('a', {'class': "css-775knl e19afand0"}).get_text()
        except:
            company = 'nan'
        try:
            salary = soup.find('div', {'id': "salaryInfoAndJobType"}).get_text()
        except:
            salary = 'nan'
        time_save = datetime.datetime.now()
        data = data.append({'Job_title': title, 'Company' : company, 'Salary': salary, 'time_saved': time_save},ignore_index= True)
    return data
