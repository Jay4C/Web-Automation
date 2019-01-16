# coding=utf-8
from selenium import webdriver

browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://www.leboncoin.fr/ar/form/0?id=1403315722')

name = browser.find_element_by_xpath("//form[@id='adreply_form']/div[1]/div[1]/input[1]")
email = browser.find_element_by_xpath("//form[@id='adreply_form']/div[2]/div[1]/input[1]")
motivations = browser.find_element_by_xpath("//form[@id='adreply_form']/div[3]/div[1]/textarea[1]")
file = browser.find_element_by_xpath("//form[@id='adreply_form']/div[4]/div[1]/input[1]")

name.send_keys("Jason ALOYAU")
email.send_keys("jason.aloyau@outlook.fr")
motivations.send_keys("Bonjour,\n"
                      "Je suis data miner junior, et je pense que je pourrai venir en aide au sein de votre entreprise.\n"
                      "Je fais du web scraping en utilisant la librairie Jsoup et du web automation en utilisant la librairie Selenium.\n"
                      "Dans l'attente de vous rencontrer prochainement, je vous prie de croire, mes salutations les plus respectueuses.\n"
                      "Jason ALOYAU")

file.send_keys("C:\Users\HP\Downloads\CV_Jason_ALOYAU_Data_Miner_Junior.pdf")

element = browser.find_element_by_xpath("//form[@id='adreply_form']/input[@type='submit' and @value='Envoyer votre candidature']")
browser.execute_script("arguments[0].click();", element)

#browser.find_element_by_xpath("//form[@id='adreply_form']/input[@type='submit' and @value='Envoyer votre candidature']").click()
#browser.close()
