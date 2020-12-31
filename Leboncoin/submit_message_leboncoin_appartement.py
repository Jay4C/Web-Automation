from selenium import webdriver
import sys
id = sys.argv[1]
votreNom = sys.argv[2]
votreEmail = sys.argv[3]

browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://www.leboncoin.fr/ar?id=' + id)

name = browser.find_element_by_xpath("//form[@id='adreply_form']/div[1]/div[1]/input[1]")
email = browser.find_element_by_xpath("//form[@id='adreply_form']/div[2]/div[1]/input[1]")
message = browser.find_element_by_xpath("//form[@id='adreply_form']/div[3]/div[1]/textarea[1]")

name.send_keys(votreNom)
email.send_keys(votreEmail)
message.send_keys("Bonjour. Je suis un particulier. Je suis dans la region parisienne. \n"+
                  "\n" +
                  "Questions: \n" +
                  "\n" +
                  "Statut du bien immobilier \n" +
                  "1) L'appartement est-il toujours en vente s'il vous plait ? \n" +
                  "3) Etes-vous le proprietaire de l'appartement s'il vous plait ? \n" +
                  "8) Y a-t-il l'existence d'hypotheques sur l'appartement s'il vous plait ? \n" +
                  "9) Y a-t-il l'existence de privileges (pris au profit d'une banque pour garantir un credit) s'il vous plait ? \n" +
                  "11) Les diagnostics immobiliers ont-ils ete realises s'il vous plait ? \n"+

                  "\n" +
                  "Impots \n" +
                  "17) Quelles sont les references cadastrales s'il vous plait ? \n" +
                  "18) Quel est le montant de la taxe fonciere s'il vous plait ? \n" +
                  "19) Quel est le montant de la taxe d'habitation s'il vous plait ? \n" +
                  "20) Quel est le montant de la charge de co-propriete s'il vous plait ? \n" +

                  "\n" +
                  "Urbanisme \n" +
                  "21) Pourriez-vous me donner l'adresse de l'appartement s'il vous plait ? \n" +

                  "\n" +
                  "Eau \n" +
                  "30) Y a-t-il toujours un compteur d'eau potable s'il vous plait ? \n" +

                  "\n" +
                  "Electricite \n" +
                  "33) Y a-t-il toujours un compteur d'electricite s'il vous plait ? \n" +

                  "\n"+
                  "Merci beaucoup de votre comprehension.\n"+

                  "\n"+
                  "Cordialement, \n"+

                  "\n" +
                  "Jason ALOYAU \n"+
                  "Telephone : 0769038124")

browser.find_element_by_xpath("//form[@id='adreply_form']").submit()
browser.close()