from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path='./chromedriver.exe')
cidade = input(f'Digite uma cidade para saber a temperatura de hoje: ')

driver.get('https://www.google.com')
pesq = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
pesq.click()
pesq.send_keys(cidade)
pesq.send_keys(Keys.RETURN)








