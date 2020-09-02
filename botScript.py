#!/usr/bin/python3
import subprocess
import sys
import time
import pyautogui
import random
from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
from selenium import webdriver

def botStartChrome():
    print("give me a bottle of rum!")
    req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    proxies = req_proxy.get_proxy_list()
    number = random.randint(0,50)
    print("rand int ==== " + str(number))
    PROXY = proxies[number].get_address()
    print(proxies[number].get_address())
    print(proxies[number].country)
    webdriver.DesiredCapabilities.CHROME['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        
        "proxyType":"MANUAL",
        
    }
    driver = webdriver.Firefox(executable_path='chromedriver')
    try:
        driver.get('https://temanpost.com/games/daftar-game-berbayar-yang-bisa-diklaim-gratis-pada-agustus-2020/')
        time.sleep(30)
    except:
        print("error something wrong")
    
    driver.quit()


def botStartFirefox():
    print("give me a bottle of rum!")
    req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
    proxies = req_proxy.get_proxy_list()
    number = random.randint(0,50)
    print("rand int ==== " + str(number))
    PROXY = proxies[number].get_address()
    print(proxies[number].get_address())
    print(proxies[number].country)
    webdriver.DesiredCapabilities.FIREFOX['proxy']={
        "httpProxy":PROXY,
        "ftpProxy":PROXY,
        "sslProxy":PROXY,
        
        "proxyType":"MANUAL",
        
    }
    driver = webdriver.Firefox(executable_path='geckodriver')
    try:
        driver.get('https://temanpost.com/games/daftar-game-berbayar-yang-bisa-diklaim-gratis-pada-agustus-2020/')
        time.sleep(30)
    except:
        print("error something wrong")
    
    driver.quit()

var = 1
while var == 1:
    botStartChrome()
    time.sleep(3)