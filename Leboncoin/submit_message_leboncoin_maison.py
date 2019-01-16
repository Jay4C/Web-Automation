from selenium import webdriver
import sys
id = sys.argv[1]
votreNom = sys.argv[2]
votreEmail = sys.argv[3]

browser = webdriver.Firefox(executable_path = 'geckodriver.exe')
browser.get('https://www.leboncoin.fr/ar/form/0?id=' + id)

name = browser.find_element_by_xpath("//form[@id='adreply_form']/div[1]/div[1]/input[1]")
email = browser.find_element_by_xpath("//form[@id='adreply_form']/div[2]/div[1]/input[1]")
message = browser.find_element_by_xpath("//form[@id='adreply_form']/div[3]/div[1]/textarea[1]")

name.send_keys(votreNom)
email.send_keys(votreEmail)
message.send_keys("Bonjour. Je suis un particulier. \n"+
                  "\n" +
                  "Questions: \n" +
                  "\n" +
                  "Statut du bien immobilier \n" +
                  "1) La maison est-elle toujours en vente s'il vous plait ? \n" +
                  "2) La maison est-elle vendue avec le terrain s'il vous plait ? \n" +
                  "3) Etes-vous le proprietaire de la maison s'il vous plait ? \n" +
                  "4) Le bornage contradictoire de la parcelle est-il realise s'il vous plait ? \n" +
                  "5) Y a-t-il l'existence de servitudes de passages s'il vous plait ? \n" +
                  "6) Y a-t-il l'existence de servitudes de vues s'il vous plait ? \n"+
                  "7) Y a-t-il l'existence de servitudes d'ecoulements des eaux s'il vous plait ? \n"+
                  "8) Y a-t-il l'existence d'hypotheques sur la maison s'il vous plait ? \n" +
                  "9) Y a-t-il l'existence de privileges (pris au profit d'une banque pour garantir un credit) s'il vous plait ? \n" +
                  "10) Y a-t-il l'existence d'autres charges (pacte de preference ou contrat d'affichage publicitaire) s'il vous plait ? \n" +
                  "11) Les diagnostics immobiliers ont-ils ete realises s'il vous plait ? \n"+
                  "12) Y a-t-il l'existence eventuelle de risques naturels previsibles dans la region (inondation, mouvements de terrain) s'il vous plait ? \n" +
                  "13) Y a-t-il l'existence de servitude d'urbanisme s'il vous plait ? \n" +
                  "14) Est-ce que la conformite de l'installation d'assainissement individuel de la maison est bien respectee s'il vous plait ? \n" +
                  "15) Y a-t-il l'existence d'une exploitation d'une activite polluante a proximite de la maison s'il vous plait ? \n" +

                  "\n" +
                  "Impots \n" +
                  "17) Quelles sont les references cadastrales s'il vous plait ? \n" +
                  "18) Quel est le montant de la taxe fonciere s'il vous plait ? \n" +
                  "19) Quel est le montant de la taxe d'habitation s'il vous plait ? \n" +

                  "\n" +
                  "Urbanisme \n" +
                  "21) Pourriez-vous me donner l'adresse de la maison s'il vous plait ? \n" +
                  "22) Y a-t-il toujours la presence de la boite aux lettres s'il vous plait ? \n" +
                  "23) Avez-vous le plan local d'urbanisme s'il vous plait ? \n" +
                  "24) Quelle est le zonage urbain de la parcelle s'il vous plait ? \n" +
                  "25) Y a-t-il une fosse septique s'il vous plait ? \n"+
                  "26) Y a-t-il la possibilite d'un raccordement au tout a l'egout s'il vous plait ? \n" +
                  "27) Combien coute le raccordement au tout a l'egout s'il vous plait ? \n" +

                  "\n" +
                  "Eau \n" +
                  "28) Y a-t-il la possibilite d'un raccordement a l'eau potable s'il vous plait ? \n" +
                  "29) Combien coute le raccordement a l'eau potable s'il vous plait ? \n" +
                  "30) Y a-t-il deja un compteur d'eau potable s'il vous plait ? \n" +

                  "\n" +
                  "Electricite \n" +
                  "31) Y a-t-il la possibilite d'un raccordement a l'electricite de France s'il vous plait ? \n" +
                  "32) Combien coute le raccordement a l'electricite de France s'il vous plait ? \n" +
                  "33) Y a-t-il deja un compteur d'electricite s'il vous plait ? \n" +

                  "\n"+
                  "Merci de votre comprehension.\n"+

                  "\n"+
                  "Cordialement, \n"+

                  "\n" +
                  "Jason ALOYAU \n"+
                  "Telephone : 0769038124")

#browser.find_element_by_xpath("//form[@id='adreply_form']").submit()
#browser.close()