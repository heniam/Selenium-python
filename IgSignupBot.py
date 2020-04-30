from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 

class IgSignupBot:
    def __init__(self, email,fullname,username,password,year,month,day):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.instagram.com/accounts/emailsignup/")
        time.sleep(2)
    
        self.driver.find_element_by_xpath("//input[@name=\"emailOrPhone\"]").send_keys(email)

        self.driver.find_element_by_xpath("//input[@name=\"fullName\"]").send_keys(fullname)

        self.driver.find_element_by_xpath("//input[@name=\"username\"]").send_keys(username)

        self.driver.find_element_by_xpath("//input[@name=\"password\"]").send_keys(password)
        
        time.sleep(3)
        #press signup button after done with that 
        self.driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        time.sleep(2)

        #birthday page 
        self.driver.find_element_by_xpath("//select[@title='Year:']").send_keys(year)
        self.driver.find_element_by_xpath("//select[@title='Month:']").send_keys(month)
        self.driver.find_element_by_xpath("//select[@title='Day:']").send_keys(day)
        time.sleep(10)
       
        #close the birthday learnmore part
        # self.driver.find_element_by_xpath("//button[@aria-label=\"Close\"]").click()
        
        #click next button 

        self.driver.find_element_by_xpath("//button[contains(text(),'Next')]").click()
        
        time.sleep(22)
       
        
        
       

IgSignupBot( 'YOUR EMAIL ','FULLNAME ','USERNAME','PASSWORD','YY','MM','DD')