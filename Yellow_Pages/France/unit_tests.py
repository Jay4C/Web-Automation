import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import requests
from bs4 import BeautifulSoup
import json


class UnitTestsDesktopAutomationYellowPagesfrance(unittest.TestCase):
    def test_click_on_button_email_without_opencv_1(self):
        app = Application(backend="uia")
        contacts = [
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            }
        ]

        for contact in contacts:
            for x in range(1, int(contact.get('number_of_page')) + 1):
                url_page = ''

                url = contact.get('contact') + str(x)

                html = requests.get(url)

                time.sleep(5)

                print('url : ' + str(x))

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("section", {"id": "listResults"}) is not None:
                    all_article = soup.select("#listResults")[0].find_all('article')

                    for article in all_article:
                        if article.find("a", {"title": "E-Mail"}) is not None:
                            if article.find("h2", {"class": "company-name noTrad"}) is not None:
                                if article.find("h2", {"class": "company-name noTrad"}).select("a")[0].get('href') == "#":
                                    json_bloc = json.loads(
                                        article.get('data-pjtoggleclasshisto'))
                                    bloc_id = json_bloc["idbloc"]["id_bloc"]
                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                    json_code_rubrique = json.loads(article.select("div")[0].get(
                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))
                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                    url_page += 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                              '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                else:
                                    url_page += 'https://www.pagesjaunes.fr' + \
                                                article.find(
                                                  "h2", {"class": "company-name noTrad"}).select("a")[0].get('href')

                                # Ouvrir l'application Google Chrome
                                app.start(
                                    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                                time.sleep(7)

                                print(url_page)

                                pywinauto.keyboard.send_keys(url_page)

                                time.sleep(3)

                                # Press the 'Enter' button
                                pywinauto.keyboard.send_keys('{ENTER}')

                                time.sleep(7)

                                # Scroll down Demande d'informations
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')

                                time.sleep(4)

                                # Move the mouse to the 'Contacter par mail' button
                                # Click the 'Contacter par mail' button
                                # pywinauto.mouse.click(button='left', coords=(300, 460))
                                # pywinauto.mouse.click(button='left', coords=(300, 510))
                                pywinauto.mouse.click(button='left', coords=(300, 610))
                                # pywinauto.mouse.click(button='left', coords=(300, 600))
                                # pywinauto.mouse.click(button='left', coords=(300, 555))
                                # pywinauto.mouse.click(button='left', coords=(300, 590))

                                time.sleep(4)

                                # Move the mouse to the 'Nom' textbox
                                # Click on the 'Nom'
                                pywinauto.mouse.click(button='left', coords=(600, 250))

                                time.sleep(4)

                                # Write my name in the 'Nom' textbox
                                myName = ""
                                pywinauto.keyboard.send_keys(myName)

                                time.sleep(4)

                                # Move the mouse to the 'Email' textbox
                                # Click on the 'Email' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 340))

                                time.sleep(4)

                                # Write my name in the 'Email' textbox
                                myEmail = ""
                                pywinauto.keyboard.send_keys(myEmail)

                                time.sleep(4)

                                # Move the mouse to the 'Objet du message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 500))

                                time.sleep(4)

                                # Write my name in the 'Objet du message' textbox
                                mySubject = ""
                                pywinauto.keyboard.send_keys(mySubject)

                                time.sleep(4)

                                # Move the mouse to the 'Message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 600))

                                time.sleep(4)

                                # Write my name in the 'Message' textbox
                                myMessage = (
                                        ""
                                )
                                pywinauto.keyboard.send_keys(myMessage)

                                time.sleep(4)

                                # Tab
                                pywinauto.keyboard.send_keys('{VK_TAB 2}')

                                time.sleep(4)

                                # Click on the 'Recevoir une copie du message' button
                                pywinauto.mouse.click(button='left', coords=(600, 370))

                                time.sleep(4)

                                # Click on the 'Envoyer' button
                                pywinauto.mouse.click(button='left', coords=(600, 440))

                                time.sleep(4)

                                # Close an active window with Alt+F4
                                pywinauto.keyboard.send_keys('%{F4}')

    def test_click_on_button_email_without_opencv_2(self):
        app = Application(backend="uia")

        contacts = [
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            }
        ]

        for contact in contacts:
            for x in range(1, int(contact.get('number_of_page')) + 1):
                url_page = ''

                url = contact.get('contact') + str(x)

                html = requests.get(url)

                time.sleep(5)

                print('url : ' + str(x))

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("section", {"id": "listResults"}) is not None:
                    all_article = soup.select("#listResults")[0].find_all('article')

                    for article in all_article:
                        if article.find("a", {"title": "E-Mail"}) is not None:
                            if article.find("h2", {"class": "company-name noTrad"}) is not None:
                                if article.find("h2", {"class": "company-name noTrad"}).select("a")[0].get('href') == "#":
                                    json_bloc = json.loads(
                                        article.get('data-pjtoggleclasshisto'))
                                    bloc_id = json_bloc["idbloc"]["id_bloc"]
                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                    json_code_rubrique = json.loads(article.select("div")[0].get(
                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))
                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                    url_page += 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                              '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                else:
                                    url_page += 'https://www.pagesjaunes.fr' + \
                                                article.find(
                                                  "h2", {"class": "company-name noTrad"}).select("a")[0].get('href')

                                # Ouvrir l'application Google Chrome
                                app.start(
                                    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                                time.sleep(7)

                                print(url_page)

                                pywinauto.keyboard.send_keys(url_page)

                                time.sleep(3)

                                # Press the 'Enter' button
                                pywinauto.keyboard.send_keys('{ENTER}')

                                time.sleep(7)

                                # Scroll down Demande d'informations
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')

                                time.sleep(4)

                                # Move the mouse to the 'Contacter par mail' button
                                # Click the 'Contacter par mail' button
                                # pywinauto.mouse.click(button='left', coords=(300, 460))
                                # pywinauto.mouse.click(button='left', coords=(300, 510))
                                pywinauto.mouse.click(button='left', coords=(300, 610))
                                # pywinauto.mouse.click(button='left', coords=(300, 600))
                                # pywinauto.mouse.click(button='left', coords=(300, 555))
                                # pywinauto.mouse.click(button='left', coords=(300, 590))

                                time.sleep(4)

                                # Move the mouse to the 'Nom' textbox
                                # Click on the 'Nom'
                                pywinauto.mouse.click(button='left', coords=(600, 250))

                                time.sleep(4)

                                # Write my name in the 'Nom' textbox
                                my_name = ""
                                pywinauto.keyboard.send_keys(my_name)

                                time.sleep(4)

                                # Move the mouse to the 'Email' textbox
                                # Click on the 'Email' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 340))

                                time.sleep(4)

                                # Write my name in the 'Email' textbox
                                my_email = ""
                                pywinauto.keyboard.send_keys(my_email)

                                time.sleep(4)

                                # Move the mouse to the 'Objet du message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 500))

                                time.sleep(4)

                                # Write my name in the 'Objet du message' textbox
                                my_subject = ""
                                pywinauto.keyboard.send_keys(my_subject)

                                time.sleep(4)

                                # Move the mouse to the 'Message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 600))

                                time.sleep(4)

                                # Write my name in the 'Message' textbox
                                my_message = (
                                        ""
                                )
                                pywinauto.keyboard.send_keys(my_message)

                                time.sleep(4)

                                # Tab
                                pywinauto.keyboard.send_keys('{VK_TAB 2}')

                                time.sleep(4)

                                # Click on the 'Recevoir une copie du message' button
                                pywinauto.mouse.click(button='left', coords=(600, 370))

                                time.sleep(4)

                                # Click on the 'Envoyer' button
                                pywinauto.mouse.click(button='left', coords=(600, 440))

                                time.sleep(4)

                                # Close an active window with Alt+F4
                                pywinauto.keyboard.send_keys('%{F4}')

    def test_click_on_button_email_without_opencv_3(self):
        app = Application(backend="uia")

        contacts = [
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            },
            {
                'contact': '',
                'number_of_page': ''
            }
        ]

        for contact in contacts:
            for x in range(1, int(contact.get('number_of_page')) + 1):
                url_page = ''

                url = contact.get('contact') + str(x)

                html = requests.get(url)

                time.sleep(5)

                print('url : ' + str(x))

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("section", {"id": "listResults"}) is not None:
                    all_article = soup.select("#listResults")[0].find_all('article')

                    for article in all_article:
                        if article.find("a", {"title": "E-Mail"}) is not None:
                            if article.find("h2", {"class": "company-name noTrad"}) is not None:
                                if article.find("h2", {"class": "company-name noTrad"}).select("a")[0].get('href') == "#":
                                    json_bloc = json.loads(
                                        article.get('data-pjtoggleclasshisto'))
                                    bloc_id = json_bloc["idbloc"]["id_bloc"]
                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                    json_code_rubrique = json.loads(article.select("div")[0].get(
                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))
                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                    url_page += 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                              '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                else:
                                    url_page += 'https://www.pagesjaunes.fr' + \
                                                article.find(
                                                  "h2", {"class": "company-name noTrad"}).select("a")[0].get('href')

                                # Ouvrir l'application Google Chrome
                                app.start(
                                    "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                                time.sleep(7)

                                print(url_page)

                                pywinauto.keyboard.send_keys(url_page)

                                time.sleep(3)

                                # Press the 'Enter' button
                                pywinauto.keyboard.send_keys('{ENTER}')

                                time.sleep(7)

                                # Scroll down Demande d'informations
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')

                                time.sleep(4)

                                # Move the mouse to the 'Contacter par mail' button
                                # Click the 'Contacter par mail' button
                                # pywinauto.mouse.click(button='left', coords=(300, 460))
                                # pywinauto.mouse.click(button='left', coords=(300, 510))
                                pywinauto.mouse.click(button='left', coords=(300, 610))
                                # pywinauto.mouse.click(button='left', coords=(300, 600))
                                # pywinauto.mouse.click(button='left', coords=(300, 555))
                                # pywinauto.mouse.click(button='left', coords=(300, 590))

                                time.sleep(4)

                                # Move the mouse to the 'Nom' textbox
                                # Click on the 'Nom'
                                pywinauto.mouse.click(button='left', coords=(600, 250))

                                time.sleep(4)

                                # Write my name in the 'Nom' textbox
                                myName = ""
                                pywinauto.keyboard.send_keys(myName)

                                time.sleep(4)

                                # Move the mouse to the 'Email' textbox
                                # Click on the 'Email' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 340))

                                time.sleep(4)

                                # Write my name in the 'Email' textbox
                                myEmail = ""
                                pywinauto.keyboard.send_keys(myEmail)

                                time.sleep(4)

                                # Move the mouse to the 'Objet du message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 500))

                                time.sleep(4)

                                # Write my name in the 'Objet du message' textbox
                                mySubject = ""
                                pywinauto.keyboard.send_keys(mySubject)

                                time.sleep(4)

                                # Move the mouse to the 'Message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 600))

                                time.sleep(4)

                                # Write my name in the 'Message' textbox
                                myMessage = (
                                        ""
                                )
                                pywinauto.keyboard.send_keys(myMessage)

                                time.sleep(4)

                                # Tab
                                pywinauto.keyboard.send_keys('{VK_TAB 2}')

                                time.sleep(4)

                                # Click on the 'Recevoir une copie du message' button
                                pywinauto.mouse.click(button='left', coords=(600, 370))

                                time.sleep(4)

                                # Click on the 'Envoyer' button
                                pywinauto.mouse.click(button='left', coords=(600, 440))

                                time.sleep(4)

                                # Close an active window with Alt+F4
                                pywinauto.keyboard.send_keys('%{F4}')

    def test_click_on_button_email_without_opencv_4(self):
        app = Application(backend="uia")

        contacts = [
            # siderurgie
            {
                # Auvergne-Rhône-Alpes
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Auvergne-Rh%C3%B4ne-Alpes&proximite=0&quoiQuiInterprete=siderurgie&contexte=X670jNNGAb2aMzRhUJQWzw%3D%3D&idOu=R84&page=',
                'number_of_page': '21',
                'y': '580'
            },
            {
                # Bourgogne-Franche-Comté
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Bourgogne-Franche-Comt%C3%A9&proximite=0&quoiQuiInterprete=siderurgie&contexte=PT14eXDaujFwxxowNQVTFA%3D%3D&idOu=R27&page=',
                'number_of_page': '9',
                'y': '580'
            },
            {
                # Bretagne
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Bretagne&idOu=R53&proximite=0&quoiQuiInterprete=siderurgie&contexte=mVLjbCNFGx3Ul%2BpcBNwbLA%3D%3D&page=',
                'number_of_page': '5',
                'y': '580'
            },
            {
                # Centre-Val-de-Loire
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Centre-Val-de-Loire&proximite=0&quoiQuiInterprete=siderurgie&contexte=m82au55EdkOKvZky7L0fQA%3D%3D&idOu=R24&page=',
                'number_of_page': '4',
                'y': '580'
            },
            {
                # Corse
                'contact': 'https://www.pagesjaunes.fr/recherche/region/corse/siderurgie?quoiqui=siderurgie&ou=Corse&univers=pagesjaunes&idOu=&acOuSollicitee=1&nbPropositionOuTop=5&nbPropositionOuHisto=0&ouSaisi=Corse&acQuiQuoiSollicitee=0&nbPropositionQuiQuoiTop=0&nbPropositionQuiQuoiHisto=0&nbPropositionQuiQuoiGeo=0&quiQuoiSaisi=siderurgie&page=',
                'number_of_page': '1',
                'y': '580'
            },
            {
                # Grand-Est
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Grand-Est&proximite=0&quoiQuiInterprete=siderurgie&contexte=6X1jsfCLIss2yckhG3qjCw%3D%3D&idOu=R44&page=',
                'number_of_page': '14',
                'y': '580'
            },
            {
                # Hauts-de-France
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Hauts-de-France&proximite=0&quoiQuiInterprete=siderurgie&contexte=TI95WWBOqeN4MI9rrYkCaA%3D%3D&idOu=R32&page=',
                'number_of_page': '14',
                'y': '580'
            },
            {
                # Ile-de-France
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Ile-de-France&idOu=R11&proximite=0&quoiQuiInterprete=siderurgie&contexte=eJK8nXK7%2BLBq512knKytkQ%3D%3D&page=',
                'number_of_page': '13',
                'y': '580'
            },
            {
                # Normandie
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Normandie&idOu=R28&proximite=0&quoiQuiInterprete=siderurgie&contexte=7i/faE0vDhmMqitTNeRdsg%3D%3D&page=',
                'number_of_page': '6',
                'y': '580'
            },
            {
                # Nouvelle-Aquitaine
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Nouvelle-Aquitaine&proximite=0&quoiQuiInterprete=siderurgie&contexte=4cg8qOrYUfub0c6bCPcFqw%3D%3D&idOu=R75&page=',
                'number_of_page': '12',
                'y': '580'
            },
            {
                # Occitanie
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Occitanie&idOu=R76&proximite=0&quoiQuiInterprete=siderurgie&contexte=xuzZtNY/M7GibtQ5xMK1qQ%3D%3D&page=',
                'number_of_page': '11',
                'y': '580'
            },
            {
                # Pays%20de%20la%20Loire
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Pays%20de%20la%20Loire&proximite=0&quoiQuiInterprete=siderurgie&contexte=aWcblFLD8vcnzqOqQuFY1g%3D%3D&idOu=R52&page=',
                'number_of_page': '8',
                'y': '580'
            },
            {
                # Provence-Alpes-Côte-d%27Azur
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Provence-Alpes-C%C3%B4te-d%27Azur&proximite=0&quoiQuiInterprete=siderurgie&contexte=X7DCUb5%2BK%2BgLhvqI1ExajA%3D%3D&idOu=R93&page=',
                'number_of_page': '8',
                'y': '580'
            },
            {
                # Guadeloupe
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=Guadeloupe&proximite=0&quoiQuiInterprete=siderurgie&contexte=8rBcxFjt8SXVIR8LN2YnZ3eKL16bkxx3e0d5jKAkSaA%3D&idOu=D971&page=',
                'number_of_page': '2',
                'y': '580'
            },
            {
                # Martinique
                'contact': 'https://www.pagesjaunes.fr/recherche/departement/martinique-972/siderurgie?quoiqui=siderurgie&ou=Martinique+%28972%29&univers=pagesjaunes&idOu=D972&ouSaisi=Martinique&ouNbCar=10&acOuSollicitee=1&rangOu=2&sourceOu=TOP&typeOu=Departement&nbPropositionOuTop=5&nbPropositionOuHisto=0&acQuiQuoiSollicitee=0&nbPropositionQuiQuoiTop=0&nbPropositionQuiQuoiHisto=0&nbPropositionQuiQuoiGeo=0&quiQuoiSaisi=siderurgie&page=',
                'number_of_page': '1',
                'y': '580'
            },
            {
                # Guyane
                'contact': 'https://www.pagesjaunes.fr/recherche/departement/guyane-973/siderurgie?quoiqui=siderurgie&ou=Guyane+%28973%29&univers=pagesjaunes&idOu=D973&ouSaisi=Guyane&ouNbCar=6&acOuSollicitee=1&rangOu=2&sourceOu=TOP&typeOu=Departement&nbPropositionOuTop=5&nbPropositionOuHisto=0&acQuiQuoiSollicitee=0&nbPropositionQuiQuoiTop=0&nbPropositionQuiQuoiHisto=0&nbPropositionQuiQuoiGeo=0&quiQuoiSaisi=siderurgie&page=',
                'number_of_page': '1',
                'y': '580'
            },
            {
                # La%20Réunion%20%28974%29
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=siderurgie&ou=La%20R%C3%A9union%20%28974%29&idOu=D974&proximite=0&quoiQuiInterprete=siderurgie&contexte=PrfBkU3EisxgP7IY1H%2BLsQxISMRndNFsTX8Pg%2Byl0iE%3D&page=',
                'number_of_page': '2'
            },
            {
                # Mayotte
                'contact': 'https://www.pagesjaunes.fr/recherche/departement/mayotte-976/siderurgie?quoiqui=siderurgie&ou=Mayotte+%28976%29&univers=pagesjaunes&idOu=D976&ouSaisi=Mayotte&ouNbCar=7&acOuSollicitee=1&rangOu=2&sourceOu=TOP&typeOu=Departement&nbPropositionOuTop=5&nbPropositionOuHisto=0&acQuiQuoiSollicitee=0&nbPropositionQuiQuoiTop=0&nbPropositionQuiQuoiHisto=0&nbPropositionQuiQuoiGeo=0&quiQuoiSaisi=siderurgie&page=',
                'number_of_page': '1',
                'y': '580'
            },
            # achat or
            {
                # Auvergne-Rhône-Alpes
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Auvergne-Rh%C3%B4ne-Alpes&idOu=R84&proximite=0&quoiQuiInterprete=achat%20or&contexte=fTKLUOf1OYREdQhkmplVdQ%3D%3D&page=',
                'number_of_page': '8',
                'y': '560'
            },
            {
                # Bourgogne-Franche-Comté
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Bourgogne-Franche-Comt%C3%A9&idOu=R27&proximite=0&quoiQuiInterprete=achat%20or&contexte=H/dBBw%2BSq0qEv5VDHuPwvA%3D%3D&page=',
                'number_of_page': '3',
                'y': '560'
            },
            {
                # Bretagne
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Bretagne&idOu=R53&proximite=0&quoiQuiInterprete=achat%20or&contexte=N7VOEakOWYk4AvMbZX4rSQ%3D%3D&page=',
                'number_of_page': '3',
                'y': '560'
            },
            {
                # Centre-Val-de-Loire
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Centre-Val-de-Loire&proximite=0&quoiQuiInterprete=achat%20or&contexte=8nd4dT9dfMRkU4OkQWzieg%3D%3D&idOu=R24&page=',
                'number_of_page': '4',
                'y': '560'
            },
            {
                # Corse
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Corse&idOu=R94&proximite=0&quoiQuiInterprete=achat%20or&contexte=XGmYCgCx3RM3Kz7RzrZsBA%3D%3D&page=',
                'number_of_page': '4',
                'y': '560'
            },
            {
                # Grand-Est
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Grand-Est&proximite=0&quoiQuiInterprete=achat%20or&contexte=pEuB5H3TH6hxsFyxa4h50A%3D%3D&idOu=R44&page=',
                'number_of_page': '5',
                'y': '560'
            },
            {
                # Hauts-de-France
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Hauts-de-France&idOu=R32&proximite=0&quoiQuiInterprete=achat%20or&contexte=LnTHcMriHJQbbenO3wb9oA%3D%3D&page=',
                'number_of_page': '5',
                'y': '560'
            },
            {
                # Ile-de-France
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Ile-de-France&idOu=R11&proximite=0&quoiQuiInterprete=achat%20or&contexte=M2Hsy261NCjEa%2B0ILFz7Gg%3D%3D&page=',
                'number_of_page': '10',
                'y': '560'
            },
            {
                # Normandie
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Normandie&idOu=R28&proximite=0&quoiQuiInterprete=achat%20or&contexte=fp%2BfjxxH5jnwFLRrgtHqRg%3D%3D&page=',
                'number_of_page': '3',
                'y': '560'
            },
            {
                # Nouvelle-Aquitaine
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Nouvelle-Aquitaine&idOu=R75&proximite=0&quoiQuiInterprete=achat%20or&contexte=Qkrxiw/ZCb62tUa6IJPpDA%3D%3D&page=',
                'number_of_page': '9',
                'y': '560'
            },
            {
                # Occitanie
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Occitanie&idOu=R76&proximite=0&quoiQuiInterprete=achat%20or&contexte=tEdSPboj15xgSYPZHYeV5A%3D%3D&page=',
                'number_of_page': '9',
                'y': '560'
            },
            {
                # Pays%20de%20la%20Loire
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Pays%20de%20la%20Loire&proximite=0&quoiQuiInterprete=achat%20or&contexte=57tiCDeURWn8/5U5yFtaaA%3D%3D&idOu=R52&page=',
                'number_of_page': '4',
                'y': '560'
            },
            {
                # Provence-Alpes-Côte-d%27Azur
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Provence-Alpes-C%C3%B4te-d%27Azur&idOu=R93&proximite=0&quoiQuiInterprete=achat%20or&contexte=0pFDpjwvyqlzf88XtJ/uvw%3D%3D&page=',
                'number_of_page': '10'
            },
            {
                # Guadeloupe
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Guadeloupe%20%28971%29&idOu=D971&proximite=0&quoiQuiInterprete=achat%20or&contexte=q2ZP8zvBNHds6bGgkXGQtg%3D%3D&page=',
                'number_of_page': '5',
                'y': '560'
            },
            {
                # Martinique
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Martinique%20%28972%29&idOu=D972&proximite=0&quoiQuiInterprete=achat%20or&contexte=QYMAchgMrwtv1rieKfg0/g%3D%3D&page=',
                'number_of_page': '3',
                'y': '560'
            },
            {
                # Guyane
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=Guyane%20%28973%29&idOu=D973&proximite=0&quoiQuiInterprete=achat%20or&contexte=Q5laNK8vzizaZGaPg/BWsw%3D%3D&page=',
                'number_of_page': '2',
                'y': '560'
            },
            {
                # La%20Réunion%20%28974%29
                'contact': 'https://www.pagesjaunes.fr/annuaire/chercherlespros?quoiqui=achat%20or&ou=La%20R%C3%A9union%20%28974%29&idOu=D974&proximite=0&quoiQuiInterprete=achat%20or&contexte=HnWcSpZ6Kq/oerlH1nox1w%3D%3D&page=',
                'number_of_page': '7',
                'y': '560'
            },
            {
                # Mayotte
                'contact': 'https://www.pagesjaunes.fr/recherche/departement/mayotte-976/achat-or?quoiqui=achat+or&ou=Mayotte+%28976%29&univers=pagesjaunes&idOu=D976&ouSaisi=Mayotte&ouNbCar=7&acOuSollicitee=1&rangOu=2&sourceOu=HISTORIQUE&typeOu=Departement&nbPropositionOuTop=4&nbPropositionOuHisto=1&acQuiQuoiSollicitee=0&nbPropositionQuiQuoiTop=0&nbPropositionQuiQuoiHisto=0&nbPropositionQuiQuoiGeo=0&quiQuoiSaisi=achat+or&page=',
                'number_of_page': '1',
                'y': '560'
            }
        ]

        for contact in contacts:
            for x in range(1, int(contact.get('number_of_page')) + 1):
                url_page = ''

                url = contact.get('contact') + str(x)

                html = requests.get(url)

                time.sleep(5)

                print('url result : ' + url)

                # Parse the content of html_doc
                soup = BeautifulSoup(html.content, 'html.parser')

                if soup.find("section", {"id": "listResults"}) is not None:

                    all_article = soup.select_one("#listResults").find_all('li')

                    for article in all_article:
                        if article.find("li", {"class": "SEL-email"}) is not None:
                            if article.find("h3", {"class": "company-name noTrad"}) is not None:
                                if article.find("h3", {"class": "company-name noTrad"}).select("a")[0].get('href') == "#":
                                    json_bloc = json.loads(
                                        article.get('data-pjtoggleclasshisto'))

                                    bloc_id = json_bloc["idbloc"]["id_bloc"]

                                    no_sequence = json_bloc["idbloc"]["no_sequence"]

                                    json_code_rubrique = json.loads(article.select("div")[0].get(
                                        'data-pjinfosaccengage-rmk-connexefd-' + bloc_id.lower()))

                                    code_rubrique = json_code_rubrique["kAN9ProToUserInfo"]

                                    url_page += 'https://www.pagesjaunes.fr/pros/detail?bloc_id=' + bloc_id + \
                                              '&no_sequence=' + no_sequence + '&code_rubrique=' + code_rubrique

                                else:
                                    url_page += 'https://www.pagesjaunes.fr' + \
                                                article.find(
                                                  "h3", {"class": "company-name noTrad"}).select("a")[0].get('href')

                                print(url_page)

                                # Ouvrir l'application Google Chrome
                                app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                                time.sleep(7)

                                pywinauto.keyboard.send_keys(url_page)

                                time.sleep(3)

                                # Press the 'Enter' button
                                pywinauto.keyboard.send_keys('{ENTER}')

                                time.sleep(7)

                                # Scroll down Demande d'informations
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')
                                time.sleep(1)
                                pywinauto.keyboard.send_keys('{DOWN}')

                                time.sleep(4)

                                # Move the mouse to the 'Contacter par mail' button
                                # Click the 'Contacter par mail' button
                                pywinauto.mouse.click(button='left', coords=(300, int(contact.get('y'))))

                                time.sleep(4)

                                # Move the mouse to the 'Nom' textbox
                                # Click on the 'Nom'
                                pywinauto.mouse.click(button='left', coords=(600, 250))

                                time.sleep(4)

                                # Write my name in the 'Nom' textbox
                                my_name = ""
                                pywinauto.keyboard.send_keys(my_name)

                                time.sleep(4)

                                # Move the mouse to the 'Email' textbox
                                # Click on the 'Email' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 340))

                                time.sleep(4)

                                # Write my name in the 'Email' textbox
                                my_email = ""
                                pywinauto.keyboard.send_keys(my_email)

                                time.sleep(4)

                                # Move the mouse to the 'Objet du message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 500))

                                time.sleep(4)

                                # Write my name in the 'Objet du message' textbox
                                my_subject = ""
                                pywinauto.keyboard.send_keys(my_subject)

                                time.sleep(4)

                                # Move the mouse to the 'Message' textbox
                                # Click on the 'Objet du message' textbox
                                pywinauto.mouse.click(button='left', coords=(600, 600))

                                time.sleep(4)

                                # Write my name in the 'Message' textbox
                                my_message = (
                                        ""
                                )
                                pywinauto.keyboard.send_keys(my_message)

                                time.sleep(4)

                                # Tab
                                pywinauto.keyboard.send_keys('{VK_TAB 2}')

                                time.sleep(4)

                                # Click on the 'Recevoir une copie du message' button
                                pywinauto.mouse.click(button='left', coords=(600, 370))

                                time.sleep(4)

                                # Click on the 'Envoyer' button
                                pywinauto.mouse.click(button='left', coords=(600, 440))

                                time.sleep(4)

                                # Close an active window with Alt+F4
                                pywinauto.keyboard.send_keys('%{F4}')


if __name__ == '__main__':
    unittest.main()
