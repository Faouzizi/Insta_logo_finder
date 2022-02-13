#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# ----------------------------------------------------------------------
# Import packages
# ----------------------------------------------------------------------
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


# ----------------------------------------------------------------------
# Define credential
email, password = os.environ.get('EMAIL'), os.environ.get('PASSWORD')
print('-'*100)
print(email)
#------------------------------------------------------------------------------------------
#
# Scrap logos from instagram using selenium
#
#------------------------------------------------------------------------------------------
# Define a wait time: time needed to load html page on the web (in seconds)
wait_time = 1

def setup_driver():
    # Define instagram url
    insta_url = 'https://www.instagram.com/'
    #
    # Define the url to the webdriver
    webdriver_path = '/usr/local/bin/chromedriver'
    s = Service(webdriver_path)
    #
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    # Define the driver
    driver = webdriver.Chrome(service=s, options=chrome_options)
    time.sleep(wait_time)
    print('-'*100)
    print('driver selected')
    # Go to the web page
    driver.get(insta_url)
    time.sleep(wait_time)
    # Click on accept coockies
    try:
        driver.find_element(By.XPATH, '/html/body/div[4]/div/div/button[1]').click()
        print('Coockies accepted successfully!')
    except:
        print('Coockies already accepted. No thing to do!')
        pass
    return driver

#----- Login to Instagram
def login_2_insta(driver, email, password, wait_time):
    """
    The aim of this function is to connect to instagram account using selenium
    driver.
    Input : driver, wait_time, email and password
    Parameters
    ----------
    driver : webdriver (here chrome webdriver)
        Needed for selenium scrapping.
    email : email as string
        The id to be used for connection to instagram.
    password : string password
        Password to be used to connect to instagram.
    wait_time: time to sleep

    Returns
    -------
    None. Just log in  to instagram account

    """
    # Send email adress as identifier
    driver_email = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    driver_email.clear()
    driver_email.send_keys(email)
    time.sleep(wait_time)
    print('-'*100)
    print('email sent')
    # Send password
    driver_password = driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    driver_password.clear()
    driver_password.send_keys(password)
    time.sleep(wait_time)
    print('-'*100)
    print('Password sent')
    # Click on Log in button
    driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(wait_time * 3)
    print('-'*100)
    print('Login click')
    # Dont save my login info
    try:
        driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    except:
        pass
    time.sleep(wait_time)
    # Dont turn on notification
    try:
        driver.find_element(By.XPATH, '/html/body/div[6]/div/div/div/div[3]/button[2]').click()
    except:
        pass
    print('-'*100)
    print('Login up')
    return driver


#----- Make Logo Search
brand_name = 'leroy merlin'
def make_logo_search(driver, brand_name, wait_time=2):
    """
    The goal of this function is to get the logo url from the brand name

    Parameters
    ----------
    driver : web driver (here chrome webdriver)
    brand_name : string. The name of the brand
    wait_time : int. The time to sleep => time needed to uplaod html page
    Returns
    -------
    dict with the brand name and the logo url
    {'Nike': 'https://machin/chouette.fr'}
    """
    # Insert in search bar the brand name
    driver.get('https://www.instagram.com/')
    search_bar = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    print('-'*100)
    print('locate search bar')
    search_bar.clear()
    search_bar.send_keys(brand_name)
    time.sleep(wait_time)
    print('-'*100)
    print('Brand name sent to search bar')
    # Click on th first instagram profile
    search_bar.find_element(By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div').click()
    time.sleep(wait_time)
    print('-'*100)
    print('clicked on first element')
    # Try to get the logo url
    brand_url = driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/div/div/span/img').get_attribute('src')
    print('-'*100)
    print('brand getted')
    return {brand_name: brand_url}

def uplaod_logo(email=email, password=password, wait_time=wait_time):
    driver = setup_driver()
    driver = login_2_insta(driver, email, password, wait_time)
    return driver

if __name__ == '__main__':
    driver = uplaod_logo(email=email, password=password, wait_time=wait_time)
    brand_logo = make_logo_search(driver, brand_name, wait_time=2)
