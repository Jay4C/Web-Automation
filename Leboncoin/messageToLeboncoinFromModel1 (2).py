from selenium import webdriver
import sys

id = sys.argv[1]
votrePrenom = sys.argv[2]
votreNom = sys.argv[3]
votreEmail = sys.argv[4]

browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://www.leboncoin.fr/ar/form/0?id=' + id)

prenomNom = browser.find_element_by_xpath("//form[@id='adreply_form']/div[1]/div[1]/input[1]")
email = browser.find_element_by_xpath("//form[@id='adreply_form']/div[2]/div[1]/input[1]")
message = browser.find_element_by_xpath("//form[@id='adreply_form']/div[3]/div[1]/textarea[1]")

prenomNom.send_keys(votrePrenom + " " + votreNom)
email.send_keys(votreEmail)
message.send_keys("Bonjour, \n"+

                  "\n" +
                  "Votre bien est-il toujours en vente s'il vous plait ? \n" +

                  "\n"+
                  "Bien cordialement, \n" +

                  "\n" +
                  votrePrenom + " " + votreNom)

#browser.find_element_by_xpath("//form[@id='adreply_form']").submit()
#browser.close()