# -*- coding: utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.firefox.options import Options
import sys

class InstaBot:
    def __init__(self, username, pw):
        
        profile = webdriver.FirefoxProfile()
        options = Options()
        options.headless = True
        profile.set_preference('intl.accept_languages', 'en')
        self.driver = webdriver.Firefox(firefox_profile=profile)
      
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(2)

    def follow(self):
        print('--------- FOLLOW BOT')
        self.driver.get("https://www.instagram.com/explore/people/suggested/")
        sleep(2)
        j= 0
        while(j < 2):
            elements = self.driver.find_elements_by_xpath('//button[contains(text(), "Follow")]')
            i = 0
            for element in elements:
                element.click()
                print("Followed!")
                print(i)
                sleep(5)
                i = i+1

            print("esperando...")
            j = j+1
            sleep(30)

        print("terminou...")
        self.driver.close()  

    # def follow(self):
    #     print('--------- FOLLOW BOT')
    #     self.driver.get("https://www.instagram.com/godoijm_/")

    #     elements = self.driver.find_elements_by_xpath('//button[contains(text(), "Follow")]')
    #     print(elements)
    #     i = 0
    #     for element in elements:
    #         element.click()
    #         print("Followed!")
    #         print(i)
    #         sleep(5)
    #         i = i+1


    def unfollow(self):
        print('--------- UNFOLLOW BOT')
        login = str(sys.argv[1])
        self.driver.get("https://www.instagram.com/"+ login + "/")
        sleep(2)
        self.driver.find_element_by_xpath('//a[contains(@href,"/following")]').click()

        i = 1
        while(i < 100):  

            self.driver.implicitly_wait(60)
            self.driver.find_element_by_xpath('//li['+str(i) + ']//div[1]//div[3]//button[1]').click()
            sleep(2)
            self.driver.find_element_by_xpath("//button[contains(text(),'Unfollow')]").click()
            print("Unfollowed!" + str(i))  
            sleep(5)      
            i = i+1
    
        print("terminou...")
        self.driver.close()

        
    def like(self):

        print('--------- LIKE BOT')
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        
        j = 1
        while(j < 5):
            i= 1
            while(i < 7):

                self.driver.find_element_by_xpath('//article'+ "[" + str(i) + "]" +'//div[2]//section[1]//span[1]//button[1]').click()
                print("liked!")
                sleep(5)
                i = i+1
        
            print("proximo")
            j = j+1
            self.driver.get("https://www.instagram.com/")   

        # self.driver.close()




bot = InstaBot(str(sys.argv[1]), str(sys.argv[2]))


if(str(sys.argv[3]) == "like"):
    bot.like()
elif(str(sys.argv[3]) == "follow"):
    bot.follow()
elif(str(sys.argv[3]) == "unfollow"):
    bot.unfollow()
else:
    bot.like()