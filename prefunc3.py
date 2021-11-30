
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import sys, os
pathname = os.path.dirname(sys.argv[0]) 


def testTask3():
 driver = webdriver.Chrome(os.path.abspath(pathname)+r"\chromedriver\chromedriver.exe")
 driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe")
 
 txt = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(@class,'cm-m-xml')][contains(text(),'https://www.w3schools.com')]"))
    )
 WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'w3-button w3-bar-item w3-hover-white w3-hover-text-green')]"))
    )
 actions = ActionChains(driver)
 actions.move_to_element_with_offset(txt, 0, 0)
 actions.perform()
 actions.click_and_hold().move_to_element_with_offset(txt, (8.25*27), 0).perform()
 actions.send_keys('"https://www.bing.com"').perform()

 driver.find_element(By.XPATH, "//button[contains(@class,'w3-button w3-bar-item w3-hover-white w3-hover-text-green')]").click()

 WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@id,'iframeResult')]"))
    )
 driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@id,'iframeResult')]"))
 WebDriverWait(driver, 60).until(
        EC.presence_of_element_located((By.XPATH, "//iframe[contains(@src,'https://www.bing.com')]"))
    )
 driver.switch_to.frame(driver.find_element_by_xpath("//iframe[contains(@src,'https://www.bing.com')]"))
 inp = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'sb_form_q')]"))
    )
 inp.click()
 inp.send_keys("redmond")

 
 try:
   WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(@query,'redmond washington')]"))
    ).click()
  
  
 except TimeoutException :
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'sb_form_q')]"))
    ).send_keys(" washington")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//input[contains(@id,'sb_form_q')]"))
    ).send_keys(Keys.ENTER)
    

    

 def IsLinkExist(dr):
  WebDriverWait(dr, 15).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@id,'b_footer')]"))
    )
  try:   
   WebDriverWait(dr, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'https://www.bing.com/travelguide?q=Redmond')]"))
    )
  except TimeoutException :
    try:
     WebDriverWait(dr, 5).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'https://bing.com/travelguide?q=Redmond')]"))
     ) 
    except:
     return False
    else:
     return True
  else:
    return True
 assert IsLinkExist(driver) == True
 driver.quit()
 






