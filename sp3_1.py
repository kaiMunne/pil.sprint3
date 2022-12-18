import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import WebDriverException 
from selenium.webdriver.common.action_chains import ActionChains


class s3_U3_TC1(unittest.TestCase):
    nav_deco=()
   
    
    def setUp(self):
        self.driver= webdriver.Chrome("D:\kai\Selenium\chromedriver_win32/chromedriver.exe")

        nav_deco=self.driver
       
        
    def test_nav_decoracion(self):
        driver= self.driver
        driver.get("https://www.arredo.com.ar/")

           
#validacion del nombre del link DECORAR
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div/a')
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div/a').text
        
        labelObtained =resultadoObtenido
        requirement='DECORACIÓN'
       
        if  requirement in labelObtained:
            print ("El link DECORACIÓN está escrito de forma correcta ")
        else:
            print ("El link DECORACIÓN está escrito de forma incorrecta ")
        
        
        
        print  (labelObtained)

#validar lista q aparece con el hover en el menu de DECORACION
        action = ActionChains(driver)
        deco_menu=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[1]/a')
        action.move_to_element(deco_menu)
        action.perform()
       
#validar ALFOMBRAS
            
       
        if  requirement in labelObtained:
            print ("El link ALFOMBRAS está escrito de forma correcta ")
        else:
            print ("El link ALFOMBRAS está escrito de forma incorrecta ")
        
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[1]/div/a').text
        
        labelObtained =resultadoObtenido
        requirement='Alfombras'  
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[1]/div/a')
        print("El link ALFOMBRAS funciona?")
        print(resultadoObtenido.is_enabled())
        
#validar ALMOHADONES
        
       
        if  requirement in labelObtained:
            print ("El link ALMOHADONES está escrito de forma correcta ")
        else:
            print ("El link ALMOHADONES está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[2]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[2]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Almohadones'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[2]/div/a' )
        print("El link ALMOHADONES funciona?")
        
        print(resultadoObtenido.is_enabled())
#validar Esencias y Aromas
        
        if  requirement in labelObtained:
            print ("El link ESENCIAS Y AROMAS está escrito de forma correcta ")
        else:
            print ("El link ESENCIAS Y AROMAS está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[3]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[3]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Esencias y Aromas'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[3]/div/a' )
        print("El link ESENCIAS Y AROMAS funciona?")
        
        print(resultadoObtenido.is_enabled())
        
  #validar CORTINAS
        
        if  requirement in labelObtained:
            print ("El link CORTINAS está escrito de forma correcta ")
        else:
            print ("El link CORTINAS está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[4]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[4]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Cortinas'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[4]/div/a' )
        print("El link CORTINAS funciona?")
       
        print( resultadoObtenido.is_enabled())
 
 #validar Cortinas Roller
        
        if  requirement in labelObtained:
            print ("El link CORTINAS ROLLER está escrito de forma correcta ")
        else:
            print ("El link CORTINAS ROLLER está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[5]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[5]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Cortinas Roller'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[5]/div/a' )
        print("El link CORTINAS ROLLER funciona?")
        
        print(resultadoObtenido.is_enabled())
        
#validar Objetos Decorativos
        
        if  requirement in labelObtained:
            print ("El link OBJETOS DECORATIVOS está escrito de forma correcta ")
        else:
            print ("El link OBJETOS DECORATIVOS está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[6]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[6]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Objetos Decorativos'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[6]/div/a' )
        print("El link OBJETOS DECORATIVOS funciona?")
       
        print(resultadoObtenido.is_enabled())
        
        
#validar ORGANIZADORES
        
        if  requirement in labelObtained:
            print ("El link ORGANIZADORES está escrito de forma correcta ")
        else:
            print ("El link ORGANIZADORES está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[7]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[7]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Organizadores'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[7]/div/a' )
        print("El link ORGANIZADORES funciona?")
        
        print(resultadoObtenido.is_enabled())
        
        
#validar MUEBLES
        
        if  requirement in labelObtained:
            print ("El link MUEBLES está escrito de forma correcta ")
        else:
            print ("El link MUEBLES está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[8]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[8]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Muebles'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[8]/div/a' )
        print("El link MUEBLES funciona?")
        
        print(resultadoObtenido.is_enabled())
        
#validar VER_TODO
        
        if  requirement in labelObtained:
            print ("El link VER TODO está escrito de forma correcta ")
        else:
            print ("El link VER TODO está escrito de forma incorrecta ")
        
        resultdadoEsperado= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[9]/div/a' )
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[9]/div/a' ).text
        
        labelObtained =resultadoObtenido
        requirement='Ver Todo'
        
        print  (labelObtained)
        
        resultadoObtenido= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div[2]/div/section/div/div/div[1]/nav/ul/li[9]/div/a' )
        print("El link VER TODO funciona?")
        
        print(resultadoObtenido.is_enabled())
        
        
 
 #Validar la funcionalidad del link DECORACION      
        try:
            nav_deco= driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[2]/section/div/div/nav/ul/li[4]/div/a' )
    
            nav_deco.click()
            time.sleep(3)
    
        except WebDriverException as e:
            print("No se pudo ir al link DECORACION")
            print("El link de DECORACION fue validado")
        
            time.sleep(4)
       
        nav_home=driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div/div[2]/div/div[1]/div/div[2]/a')
     
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
   
   
    