from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time 

lat1 = input('Enter the latitude range1: ')
lat2 = input('Enter the latitude range2: ')
long1 = input('Enter the longitude range1: ')
long2 = input('Enter the longitude range2: ')

#Below is to remove the toolbar and open chrome and visit the webpage 
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-infobars")
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://ode.rsl.wustl.edu/moon/indexproductsearch.aspx')

#DOES NOT select the type of image box(variable) – do this?
#open lat long box
full = driver.find_element_by_xpath('//div[@id="pnlFindByLatLong_header]')
full.click()
#send values to the lat input boxes
latbox1 = driver.find_element_by_xpath('//input[@name="txtWestLongitude"]').send_keys(str(lat1))
latbox2 = driver.find_element_by_xpath('//input[@name="txtEastLongitude"]').send_keys(str(lat2))
driver.send_keys(Keys.RETURN)
#send values to the long input boxes
longbox1 = driver.find_element_by_xpath('//input[@name="txtMaxLatitude"]').send_keys(str(long1))
longbox2 = driver.find_element_by_xpath('//input[@name="txtMinLatitude"]').send_keys(str(long2))
driver.send_keys(Keys.RETURN)
#clicks the 'load all valid images' button
loadimages = driver.find_element_by_xpath('//input[@id="btnSearchb"]')
loadimages.click()
#waits for page to load
time.sleep(5)
#finds the first image – CHANGE TO ALL LATER?
firstimage = driver.find_element_by_id('gvQueryResults_ctl03_HyperlinkFile')
firstimage.click()
time.sleep(5)


download = driver.find_elment_by_xpath('//img[@title="Click to download product and detached label"]')
download.click()

driver.quit()







"""
full = driver.find_element_by_xpath('//div[@class="links"]')
full2 = full.find_element_by_xpath('//span[@class="smallHelpBox"]')
full3 = full2.find_element_by_xpath('//a[@class="fullscreen mapbutton"]').click()

arrow2 = driver.find_element_by_xpath('//div[@class="zoomSelectWrapper mapbutton"]').click()
arrow3 = driver.find_element_by_xpath('//ul[@class="zoomSelect ui-menu ui-widget ui-widget-content ui-corner-all"]')
arrow4 = driver.find_element_by_xpath('//li[@class="ui-menu-item"]')
arrow5 = driver.find_element_by_xpath('//a[@id="ui-id-58"]')
arrow5.click()

arrow = driver.find_element_by_xpath('//div[@id="OpenLayers.Control.MousePosition_19" and @class="olControlMousePosition olControlNoSelect"]')
arrow.click()

trial = driver.find_element_by_xpath('//div[@class="recenterWrapper"]')

trial.find_element_by_xpath('//input[@class = "latbox"]').send_keys(str(latitude)) 
trial.find_element_by_xpath('//input[@class = "lonbox"]').send_keys(str(longitude)) 
trial.find_element_by_xpath('//a[@class = "recenterBtn qm-icon icon-recenter"]').click()
arrow.click()

#This is used to sltop so taht i can wait for the image to laod 
time.sleep(10)

save = driver.save_screenshot('imageScreenshot.png')
time.sleep(10)
driver.quit()

#driver = webdriver.Chrome('/Users/arushi/Downloads/chromedriver')
#driver.save_screenshot('/Users/arushi/Desktop/Arushi/LROCScreenshots')
"""