# -*- coding: utf-8 -*-
"""
Spyder Editor

Python scrapper
"""
import requests
import bs4
import pandas as pd
from fake_useragent import UserAgent
import itertools as it
import random

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.common.exceptions import TimeoutException
import time
from bs4 import BeautifulSoup

from selenium.webdriver.common.action_chains import ActionChains


class Element:
    def __init__(self,value,property="class",tag="div"):
        self.value = value
        self.tag = tag
        self.property = property

    def find_all(self,soup):
        return soup.find_all(self.tag, {self.property:self.value})

    def find_childs(self,parent):
        return parent.find(self.tag, {self.property:self.value})


class Scrapper:
    
    def __init__(self,element,headers,parameters):
        self.outer_element = element
        self.headers = headers
        self.inner_elements = parameters
        
        if len(headers) != len(parameters):
            print("Warning length of headers and parameters mismatch")

    def scroll(self,driver,times,wait=2):
        height = driver.execute_script("return document.body.scrollHeight")
        step = height // times

        for i in range(times+1):
            driver.execute_script(f"console.log('scroll to {i*step}');")
            driver.execute_script(f"window.scrollTo(0, {i*step})")
            time.sleep(wait)
            
    def parse_and_get(self,url,category,add_scroll=False):
        response = self.get_page(url,add_scroll=add_scroll)
        return self.scrap(response,category)
        
    def scrap(self,response,category):
        soup = bs4.BeautifulSoup(response, 'html.parser')
        #print(self.outer_element.get())
        elements = self.outer_element.find_all(soup)

        print("Found {} products".format(len(elements)))
        
        products = []
        skipped = 0
        wasSkipped = False

        for e in elements:
            #print(e)
            retrieved_item = []

            for inner_element in self.inner_elements:
                item = inner_element.find_childs(e)

                if item == None:
                    skipped+=1
                    wasSkipped = True
                    break
                else:
                    item = item.contents
                    if item == None:
                        skipped+=1
                        wasSkipped = True
                        break
                    else:
                        #print(f"Added {item}")
                        retrieved_item.append(item)
            #if len(retrieved_item) == len(self.headers):
            if not(wasSkipped):
                products.append(retrieved_item)
            
        
        print(f'Skipped {skipped}/{len(elements)} elements')
        return pd.DataFrame(products,columns=self.headers)
    
    def get_page(self,url,includeChromium=True,add_scroll=True):
        response = None
        driver = None

        if includeChromium:
            chrome_options = Options()
            ua = UserAgent()
            userAgent = ua.random
            print(userAgent)
            chrome_options.add_argument(f'--user-agent={userAgent}')
            chrome_options.add_argument("--disable-web-security")
            chrome_options.add_argument("--user-data-dir=~/chromeTemp")
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(url)
            
            #print(f"Height of windows {height}")
            if add_scroll:
                self.scroll(driver,5,wait=1)
                print("Scroll finished")
            else:
                time.sleep(20)

            response = driver.page_source.encode('utf-8').strip()

        else:
            response = requests.get(self.endpoint).text

        return response


