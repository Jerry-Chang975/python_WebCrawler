# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 14:52:57 2021

@author: jerry
web data extract

"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time 

class BingoBingo:
    
    def __init__(self, website):
        self.options = Options()
        self.options.add_argument("--disable-notifications") # 取消所有alert彈出視窗
        
        self.browser = webdriver.Chrome(
                    ChromeDriverManager().install(),
                    chrome_options = self.options) # 瀏覽器
        self.browser.get(website)
    
    def web_data(self, month, date):
        
        date_button = self.browser.find_element_by_css_selector("[title*='{0}月{1}日']".format(month, date))
        time.sleep(0.5)
        self.browser.execute_script("arguments[0].click();", date_button) # 點擊網頁按鈕
        time.sleep(0.5)
        soup = BeautifulSoup(self.browser.page_source, "html.parser") # bs4讀取網頁資訊
        # 關閉網頁
        self.browser.close()
        
        return soup
    
class data_extract:
    
    def __init__(self, soup):
        result = soup.find_all("td", class_="tdA_4") # 取出賓果每期開出資訊(只有一半)
        result1 = soup.find_all("td", class_="tdA_3") # 取出賓果每期開出資訊(另一半)
        
        self.data = [] # 存取資料
        self.data1 = [] # 存取資料
        for i in result:
            self.data.append(i.getText())
        for j in result1:
            self.data1.append(j.getText())
    
    
    def string_to_intlist(str_list): 
        str_list = str_list.replace("  ", " ")
        int_list = []
        
        for i in range(20):
            try:
                int_list.append(int(str_list[i*3:(i*3+2)]))
            except SyntaxError:
                int_list.append(int(str_list[i*3+1]))
        
        return int_list
            
    def data_dict(self):
        
        data = self.data
        data1 = self.data1
    
        res_dict = {} # 用字典方式存取資料
        for i in range(len(data)):
            if len(data[i]) == 9: # 期數特徵: len() = 9
                res_dict[int(data[i])] = data_extract.string_to_intlist(data[i+1]) # 期數下一項剛好是開出獎號
        for i in range(len(data1)):
            if len(data1[i]) == 9:
                res_dict[int(data1[i])] = data_extract.string_to_intlist(data1[i+1])
        
        return res_dict
    
    

