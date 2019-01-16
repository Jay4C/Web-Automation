from selenium import webdriver

browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://www.leboncoin.fr/ar/form/0?id=1398572346')

prenomNom = browser.find_element_by_xpath("//form[@id='adreply_form']/div[1]/div[1]/input[1]")
email = browser.find_element_by_xpath("//form[@id='adreply_form']/div[2]/div[1]/input[1]")
message = browser.find_element_by_xpath("//form[@id='adreply_form']/div[3]/div[1]/textarea[1]")

prenomNom.send_keys("Jason ALOYAU")
email.send_keys("jason.aloyau@outlook.fr")
message.send_keys("Bonjour, \n"+

                  "\n" +
                  "Votre bien est-il toujours en vente s'il vous plait ? \n" +

                  "\n"+
                  "Bien cordialement,")

#browser.find_element_by_xpath("//form[@id='adreply_form']").submit()
#browser.close()