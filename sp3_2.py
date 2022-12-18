import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains


class s3_U3_TC1(unittest.TestCase):
    nav_deco = ()
    nav_contacto = ()

    def setUp(self):
        self.driver = webdriver.Chrome(
            "D:\kai\Selenium\chromedriver_win32/chromedriver.exe")

    def test_nav_contacto(self):
        driver = self.driver
        driver.get("https://www.arredo.com.ar/")

        time.sleep(4)
        

# validar nombre de link contacto
        requirement="Contacto"
        resultdadoEsperado= driver.find_element(By.XPATH, '//*[@id="menu-item-footer-link-contacto"]' )
        resultadoObtenido= driver.find_element(By.XPATH, '//*[@id="menu-item-footer-link-contacto"]' ).text
        
        labelObtained =resultadoObtenido
        if  requirement in labelObtained:
            print ("El link CONTACTO está escrito de forma correcta ")
        else:
            print ("El link CONTACTO está escrito de forma incorrecta ")
        
        
        print  (labelObtained)
    
# validar link de contacto

        try:
            
            nav_contacto = driver.find_element(By.XPATH, '//*[@id="menu-item-footer-link-contacto"]')
            nav_contacto.send_keys(Keys.RETURN)
            time.sleep(3)

        except WebDriverException as e:
            print("No se logro ir al link")
            print("El link de CONTACTO fue validado")

        time.sleep(4)
        
       # validar el numero de Whatsapp
        
       
        if  requirement in labelObtained:
            print ("El link Whatsapp está escrito de forma correcta ")
        else:
            print ("El link Whatsapp está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div/div/div/div/p/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div/div/div/div/p/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='+54 9 11 7360 9060'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[1]/div/div[2]/div/div/div/div/div/p/a' )
        print("El link Whatsapp funciona?")
        
        print(resultadoObtenido.is_enabled())
        
        
        # validar el Chat
        
       
        if  requirement in labelObtained:
            print ("El link Chat está escrito de forma correcta ")
        else:
            print ("El link Chat está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/p/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/p/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='+54 9 11 7360 9060'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[2]/div/div[1]/div/div[1]/div[2]/div/p/a' )
        print("El link Chat funciona?")
        
        print(resultadoObtenido.is_enabled())
        
         # validar el telefono
        
       
        if  requirement in labelObtained:
            print ("El link Telefono está escrito de forma correcta ")
        else:
            print ("El link Telefono está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/p/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[3]/div/div[1]/div/div[1]/div[2]/div/p/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='0800-362-2740'
        
        print  (labelObtained)
        
         # validar el Mail
        
       
        if  requirement in labelObtained:
            print ("El Mail está escrito de forma correcta ")
        else:
            print ("El Mail está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/p/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/p/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='tiendaonline@arredo.com.ar'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[4]/div/div[1]/div/div[1]/div[2]/div/p/a' )
        print("El link Mail funciona?")
        
        print(resultadoObtenido.is_enabled())
        
        
        # validar el link Sucursal
        
       
        if  requirement in labelObtained:
            print ("El link Sucursal está escrito de forma correcta ")
        else:
            print ("El link Sucursal está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[5]/div/div[2]/div/div/p/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[5]/div/div[2]/div/div/p/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='tiendaonline@arredo.com.ar'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div/div[1]/div[4]/div/div[5]/div/div[2]/div/div/p/a' )
        print("El link Sucursal funciona?")
        
        print(resultadoObtenido.is_enabled())

        time.sleep(4)
        
        
#validar link home
        nav_home = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a')
        try:
            nav_home.send_keys(Keys.RETURN)
            time.sleep(4)
        except WebDriverException as e:
            print("No se logró ir al link")
            print("El link de IR A LA HOME fue validado")

            time.sleep(3)

  

    def tearDown(self):
        
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
