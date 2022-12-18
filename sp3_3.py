from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import unittest
import time
from selenium.common.exceptions import WebDriverException
from bs4 import BeautifulSoup
from lxml import etree
import requests



class sp3_ex3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "D:\kai\Selenium\chromedriver_win32/chromedriver.exe")
        
    def test_nav_tierra(self):
        driver = self.driver
        
        driver.get("https://www.arredo.com.ar/")

# validar link Preguntas frecuentes

        nav_tierra=driver.find_element(By.XPATH, '//*[@id="menu-item-footer-link-la-tierra"]')
     
        try:  
       
            nav_tierra.send_keys(Keys.RETURN)
            time.sleep(4)
        except WebDriverException as e:
            print("No se logró ir al link")
            print("El link de 'Tierra' fue validado")
        
        
 #Validar Jardines verticales    
        
        
        nav_jardinVert = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[1]/div/div[2]/a")

        print("El link 'Jardines verticales' funciona?")
        print(nav_jardinVert.is_enabled())
        
        
        
#Validar Productos Sustentables

        nav_productSust= driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/a")
        
        print ("El link 'Productos Sustentables' funciona?" )
        print(nav_productSust.is_enabled())
        
        
#Validar retorno a la HOME
        
        nav_home=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div/div/div[1]/div/div[1]/div/div/a')
     
        try:  
       
            nav_home.send_keys(Keys.RETURN)
            time.sleep(4)
        except WebDriverException as e:
            print("No se logró ir al link")
            print("El link de IR A LA HOME fue validado")
    
    
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
