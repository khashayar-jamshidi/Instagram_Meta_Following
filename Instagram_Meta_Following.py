"""
khashayar_jamshidi@yahoo.com

@author: khashayar-jamshidi
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from selenium.webdriver.support import ui
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
###################     
class Instagram_Meta_Following :
    ###################     
    def __init__ (self,username,password):
        self.username = username
        self.password = password
      #  self.driver =  webdriver.PhantomJS()
        self.driver =  webdriver.Firefox()
    ###################         
    def  CloseBrowrse(self):
        self.driver.close()
    ###################         
    def login (self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
       # driver.get('https://www.instagram.com/accounts/login/?source=reset_password')
        time.sleep(random.randint(Time_A,Time_B))
        user_name_box = driver.find_element_by_xpath("//input[@name='username']")
        user_name_box.clear()                                             
        user_name_box.send_keys(self.username)
        password_box = driver.find_element_by_xpath("//input[@name='password']")
        password_box.clear()
        password_box.send_keys(self.password)
        password_box.send_keys(u'\ue007')
        time.sleep(random.randint(Time_A,Time_B))
        driver.get('https://www.instagram.com/'+username+'/')
        ################
        print("REDY PASSWORD & USERNAME")
        ################
    def Following_Meta(self,hashtag):        
        driver =self.driver
        driver.get('https://www.instagram.com/explore/tags/'+hashtag+ '/')
        time.sleep(random.randint(Time_A,Time_B))
        pic_hrefs = []
        ################
        print('HASHTAG SET')
        ################
        hh=1
        ################
        for i in range(1,3):
            try:
              scheight = .001
              while scheight < x:
                  driver.execute_script("window.scrollTo(0, document.body.scrollHeight/%s);" % scheight)
                  scheight += .001
                  #driver.execute_script("window.scrollTo(500, 0)")
                  time.sleep(random.randint(Time_A,Time_B))
                  hrefs_in_view = driver.find_elements_by_tag_name('a')
                  hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view if '/p/' in elem.get_attribute('href')]
                  #ax tekrari bedi behsh ke like nashe
                  [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                  ################
                  time.sleep(random.randint(Time_A,Time_B))
                  print('SAVE LINK OK NUMBER : %s'%hh)
                  hh+=1
                  ################
            except Exception :
                continue

        #LIKE PIC & COMMENT
        for pic_href in pic_hrefs :
            driver.get(pic_href)
            time.sleep(random.randint(Time_A,Time_B))
            try:               
                print('CLICK LIKE AND COMMENT AND Following NAME IS : %s' %pic_href)
                # click comment pic 
                ################                             
                p=random.randint(0,4)
                q=random.randint(0,3)
                letter=list1[p]+list2[q] 
                ###################         
                time.sleep(random.randint(Time_A,Time_B))                                                                      
                driver.find_element_by_class_name("Ypffh").click()
                driver.find_element_by_class_name("Ypffh").send_keys(letter)
                driver.find_element_by_class_name("Ypffh").send_keys(Keys.ENTER)
                ###################     
                #Following                
                time.sleep(random.randint(Time_A,Time_B))
                driver.find_element_by_xpath('.//*[@type="button"]').click()
                time.sleep(random.randint(Time_A,Time_B))                                
            except Exception as e:
                time.sleep(3)
                
###################           
#x= .10 or. serch for following and comm 
x=.005
###################           
#time
##smailtime Time_A <Time_B
Time_A = 5
#bigtime
Time_B = 15                            
###################
list1=["niceeee ","aweeesome ","supeeerr ","cooool ","loool"]
list2=[":)", ";)",":o",":D"]
###################     
username = "***********"
password = "**********"
###################
#hashtag = ['CLOCK','Usa','black', ]
hashtag = ['black', ]      
###################
ig = Instagram_Meta_Following(username, password)
ig.login()        
###################
while True:
    try:
        flv =random.choice(hashtag)
        ig.Following_Meta(flv)
    except Exception:
        ig.CloseBrowrse()
        time.sleep(20)
        ig = Instagram_Meta_Following(username,password)
        ig.login()
        