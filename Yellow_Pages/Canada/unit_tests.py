import requests
import os
import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from requests_tor import RequestsTor
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationYellowPagesCanadaWithPywinauto(unittest.TestCase):
    def test_click_on_button_email_for_one_page_without_ocr_for_distributing_open_source_code(self):
        app = Application(backend="uia")

        url_page = "https://www.yellowpages.ca/bus/Nova-Scotia/Middle-Sackville/After-Warranty-Automotive-Repair/5803120.html?what=car+repair&where=Halifax+NS&useContext=true"

        time.sleep(5)

        # Ouvrir l'application Microsoft Edge
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        print(url_page)

        pywinauto.keyboard.send_keys(url_page)

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Move the mouse to the 'Message' button
        # Click the 'Message' button
        pywinauto.mouse.click(button='left', coords=(480, 330))

        time.sleep(4)

        # Move the mouse to the 'Your email' textbox
        # Click on the 'Your email' textbox
        pywinauto.mouse.click(button='left', coords=(420, 260))

        time.sleep(4)

        # Write my name in the 'Your email' textbox
        myEmail = ""
        pywinauto.keyboard.send_keys(myEmail)

        time.sleep(4)

        # Move the mouse to the 'First name' textbox
        # Click on the 'First name' textbox
        pywinauto.mouse.click(button='left', coords=(430, 310))

        time.sleep(4)

        # Write my name in the 'First name' textbox
        myFirstName = ""
        pywinauto.keyboard.send_keys(myFirstName)

        time.sleep(4)

        # Move the mouse to the 'Last name' textbox
        # Click on the 'Last name' textbox
        pywinauto.mouse.click(button='left', coords=(700, 310))

        time.sleep(4)

        # Write my name in the 'Last name' textbox
        myLastName = ""
        pywinauto.keyboard.send_keys(myLastName)

        time.sleep(4)

        # Move the mouse to the 'Message' textbox
        # Click on the 'Objet du message' textbox
        pywinauto.mouse.click(button='left', coords=(430, 400))

        time.sleep(4)

        # Write my name in the 'Message' textbox
        myMessage = (
                ""
        )
        pywinauto.keyboard.send_keys(myMessage)

        time.sleep(4)

        # Click on the 'Envoyer' button
        #pywinauto.mouse.click(button='left', coords=(920, 620))

        time.sleep(4)

        # Close an active window with Alt+F4
        #pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(4)

    def test_click_on_button_email_for_all_pages_without_ocr_for_distributing_open_source_hydrogen_technologies_for_car_repair_in_canada(self):
        app = Application(backend="uia")

        contacts = [
            # edmonton
            {
                'location': 'Edmonton+AB',
                'start': '1',
                'number_of_page': '20'
            },

            # victoria
            {
                'location': 'Victoria+BC',
                'start': '1',
                'number_of_page': '8'
            },

            # winnipeg
            {
                'location': 'Winnipeg+MB',
                'start': '1',
                'number_of_page': '14'
            },

            # fredericton
            {
                'location': 'Fredericton+NB',
                'start': '1',
                'number_of_page': '4'
            },

            # saint john
            {
                'location': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL',
                'start': '1',
                'number_of_page': '6'
            },

            # halifax
            {
                'location': 'Halifax+NS',
                'start': '1',
                'number_of_page': '10'
            },

            # yellowknife
            {
                'location': 'Yellowknife+NT',
                'start': '1',
                'number_of_page': '1'
            },

            # iqaluit
            {
                'location': 'Iqaluit+NU',
                'start': '1',
                'number_of_page': '1'
            },

            # toronto
            {
                'location': 'Toronto+ON',
                'start': '1',
                'number_of_page': '60'
            },

            # charlottetown
            {
                'location': 'Charlottetown+PE',
                'start': '1',
                'number_of_page': '4'
            },

            # quebec
            {
                'location': 'Quebec+QC',
                'start': '1',
                'number_of_page': '23'
            },

            # regina
            {
                'location': 'Regina+SK',
                'start': '1',
                'number_of_page': '4'
            },

            # whitehorse
            {
                'location': 'Whitehorse+YT',
                'start': '1',
                'number_of_page': '2'
            }
        ]

        for contact in contacts:
            try:
                location = contact.get("location")
                start = int(contact.get("start"))
                number_of_pages = int(contact.get("number_of_page"))

                i_1 = 1

                for i in range(start, number_of_pages + 1):
                    url_page_results = "https://www.yellowpages.ca/search/si/" + str(i) + "/car+repair/" + location

                    print("url_page_results : " + url_page_results)

                    html_search = requests.get(url_page_results)

                    soup_search = BeautifulSoup(html_search.content, 'html.parser')

                    if soup_search.find("div", {"class": "resultList"}) is not None:
                        if soup_search\
                                .find("div", {"class": "resultList"})\
                                .find("div", {"class": "listing"}) is not None:
                            results = soup_search\
                                .find("div", {"class": "resultList"})\
                                .find_all("div", {"class": "listing"})

                            for result in results:
                                if result.find("li", {"class": "mlr__item--message"}) is not None:
                                    url_page = "https://www.yellowpages.ca" + result\
                                        .find("link", {"itemprop": "url"})\
                                        .get("href")

                                    print("url_page " + str(i_1) + " : " + url_page)

                                    time.sleep(5)

                                    # Ouvrir l'application Microsoft Edge
                                    app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                                    time.sleep(10)

                                    pywinauto.keyboard.send_keys(url_page)

                                    time.sleep(3)

                                    # Press the 'Enter' button
                                    pywinauto.keyboard.send_keys('{ENTER}')

                                    time.sleep(7)

                                    # Move the mouse to the 'Message' button
                                    # Click the 'Message' button
                                    pywinauto.mouse.click(button='left', coords=(480, 330))

                                    time.sleep(4)

                                    # Move the mouse to the 'Your email' textbox
                                    # Click on the 'Your email' textbox
                                    pywinauto.mouse.click(button='left', coords=(420, 260))

                                    time.sleep(4)

                                    # Write my name in the 'Your email' textbox
                                    myEmail = ""
                                    pywinauto.keyboard.send_keys(myEmail)

                                    time.sleep(4)

                                    # Move the mouse to the 'First name' textbox
                                    # Click on the 'First name' textbox
                                    pywinauto.mouse.click(button='left', coords=(430, 310))

                                    time.sleep(4)

                                    # Write my name in the 'First name' textbox
                                    myFirstName = ""
                                    pywinauto.keyboard.send_keys(myFirstName)

                                    time.sleep(4)

                                    # Move the mouse to the 'Last name' textbox
                                    # Click on the 'Last name' textbox
                                    pywinauto.mouse.click(button='left', coords=(700, 310))

                                    time.sleep(4)

                                    # Write my name in the 'Last name' textbox
                                    myLastName = ""
                                    pywinauto.keyboard.send_keys(myLastName)

                                    time.sleep(4)

                                    # Move the mouse to the 'Message' textbox
                                    # Click on the 'Objet du message' textbox
                                    pywinauto.mouse.click(button='left', coords=(430, 400))

                                    time.sleep(4)

                                    # Write my name in the 'Message' textbox
                                    myMessage = (
                                            ""
                                    )
                                    pywinauto.keyboard.send_keys(myMessage)

                                    time.sleep(4)

                                    # Click on the 'Envoyer' button
                                    pywinauto.mouse.move(coords=(920, 620))
                                    # pywinauto.mouse.click(button='left', coords=(920, 620))

                                    time.sleep(4)

                                    # Close an active window with Alt+F4
                                    pywinauto.keyboard.send_keys('%{F4}')

                                    time.sleep(4)
                                else:
                                    print(str(i_1) + " div class mlr__item--message is not present")

                                i_1 += 1
                        else:
                            print("div class listing is not present")
                    else:
                        print("div class resultList is not present")
            except Exception as e:
                print("error : " + str(e))


class UnitTestsWebAutomationYellowPagesCanadaWithClearWebWithSelenium(unittest.TestCase):
    # ok
    def test_insert_the_email_for_one_company_with_clear_web(self):
        print('test_insert_the_email_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                "email_outlook"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_insert_the_first_name_for_one_company_with_clear_web(self):
        print('test_insert_the_first_name_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                "First_name"
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print("browser.quit()")

    # ok
    def test_insert_the_last_name_for_one_company_with_clear_web(self):
        print('test_insert_the_last_name_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                "Last_name"
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_count_characters_of_the_message(self):
        print('test_count_characters_of_the_message')

        text = "Hello,\n\n"

        if len(text) < 1000:
            print("length text good : " + str(len(text)))
        else:
            print("length text bad : " + str(len(text)))

    # ok
    def test_insert_the_message_for_one_company_with_clear_web(self):
        print('test_insert_the_message_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n"

            message_input.send_keys(
                text
            )
            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    #
    def test_insert_the_file_for_one_company_with_clear_web(self):
        print('test_insert_the_file_for_one_company_with_clear_web')

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Whitby/Ontario-Shores-Centre-for-Mental-Health-'
                    'Sciences/6707729.html?what=Hospital&where=Toronto+ON&useContext=true')

        time.sleep(15)

        file = "filename.png"

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert on the file
        file_upload = browser.find_element_by_xpath(
            '//*[@id="uploadfiles"]'
        )
        file_upload.send_keys(file)

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_send_a_message_for_one_company_with_clear_web(self):
        print("test_send_a_message_for_one_company_with_clear_web")

        time.sleep(5)

        warnings.filterwarnings(
            action="ignore",
            message="unclosed",
            category=ResourceWarning
        )

        time.sleep(5)

        firefox_options = Options()
        firefox_options.headless = False
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=firefox_options
        )

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.yellowpages.ca/bus/Ontario/Toronto/The-Big-Carrot-Danforth-Community-Market/102254127.html?what=Restaurant&where=Toronto+ON&useContext=true')
        print('page opened')

        time.sleep(15)

        # click on the message button
        message_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
        )
        message_button.click()

        time.sleep(10)

        # insert the email
        try:
            email_input = browser.find_element_by_xpath(
                '//*[@id="emailMessage"]'
            )
            email_input.clear()
            email_input.send_keys(
                "email_outlook"
            )
            print("email inserted")
        except Exception as e:
            print('error email inserted : ' + str(e))

        time.sleep(10)

        # insert the first name
        try:
            first_name_input = browser.find_element_by_xpath(
                '//*[@id="firstNameMessage"]'
            )
            first_name_input.clear()
            first_name_input.send_keys(
                "first_name"
            )
            print("first_name_input inserted")
        except Exception as e:
            print('error first_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the last name
        try:
            last_name_input = browser.find_element_by_xpath(
                '//*[@id="lastNameMessage"]'
            )
            last_name_input.clear()
            last_name_input.send_keys(
                "last_name"
            )
            print("last_name_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # insert the message
        try:
            message_input = browser.find_element_by_xpath(
                '//*[@id="contentMessage"]'
            )
            message_input.clear()

            text = "Hello,\n\n"

            message_input.send_keys(
                text
            )

            print("message_input inserted")
        except Exception as e:
            print('error last_name_input inserted : ' + str(e))

        time.sleep(10)

        # click on the "Yes" checkbox
        yes_checkbox = browser.find_element_by_xpath(
            '//*[@id="agreementMessage"]'
        )
        yes_checkbox.click()
        print('yes_checkbox.click()')

        time.sleep(10)

        # click on the "Send the copy of the message" checkbox
        copy_checkbox = browser.find_element_by_xpath(
            '//*[@id="sendCopy"]'
        )
        copy_checkbox.click()
        print('copy_checkbox.click()')

        time.sleep(10)

        # click on the 'send' button
        send_button = browser.find_element_by_xpath(
            '/html/body/div[5]/div/div/div/div[2]/form/div[8]/button'
        )
        send_button.click()
        print('send_button.click()')

        time.sleep(10)

        # Print the success
        success = browser.find_element_by_xpath(
            "/html/body/div[5]/div/div/div/div[2]/div[2]"
        ).get_attribute("data-msg-name")
        print('success : ' + str(success))

        time.sleep(10)

        print("ccleaner running")
        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
        os.system("start ccleaner /AUTO")

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_send_a_message_for_companies_with_clear_web(self):
        print('test_send_a_message_for_companies_with_clear_web')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103'
            }

            activites = [
                {'id': '1', 'url': 'agence+de+placement', 'start': 1},
                # {'id': '2', 'url': 'agence+immobilière', 'start': 1},
                # {'id': '3', 'url': "recrutement", 'start': 1},
                # {'id': '4', 'url': 'logiciel', 'start': 1},
                # {'id': '5', 'url': 'hotel', 'start': 1},
                # {'id': '6', 'url': 'social', 'start': 1},
                # {'id': '7', 'url': 'nettoyage', 'start': 1},
                # {'id': '8', 'url': 'association', 'start': 1},
                # {'id': '9', 'url': 'etablissement+financier', 'start': 1},
                # {'id': '10', 'url': 'restaurant', 'start': 1},
                # {'id': '11', 'url': 'batiment', 'start': 1},
                # {'id': '12', 'url': 'coiffeur', 'start': 1},
                # {'id': '13', 'url': 'fleuriste', 'start': 1},
                # {'id': '14', 'url': 'serrurier', 'start': 1},
                # {'id': '15', 'url': 'boulangerie', 'start': 1},
                # {'id': '16', 'url': 'assurance', 'start': 1},
                # {'id': '17', 'url': 'pharmacie', 'start': 1},
                # {'id': '18', 'url': 'demenagement', 'start': 1},
                # {'id': '19', 'url': 'electricite', 'start': 1},
                # {'id': '20', 'url': 'plomberie', 'start': 1},
                # {'id': '21', 'url': 'securite', 'start': 1},
                # {'id': '22', 'url': 'avocat', 'start': 1},
                # {'id': '23', 'url': 'banque', 'start': 1},
                # {'id': '24', 'url': 'garage', 'start': 1},
                # {'id': '25', 'url': 'dentiste', 'start': 1},
                # {'id': '26', 'url': 'docteur', 'start': 1},
                # {'id': '27', 'url': 'comptable', 'start': 1},
                # {'id': '28', 'url': 'supermarche', 'start': 1},
                # {'id': '29', 'url': 'notaire', 'start': 1},
                # {'id': '30', 'url': 'bijoutier', 'start': 1},
                # {'id': '31', 'url': 'couturier', 'start': 1},
                # {'id': '32', 'url': 'boucherie', 'start': 1},
                # {'id': '33', 'url': 'librairie', 'start': 1},
                # {'id': '34', 'url': 'architecte', 'start': 1}
                # {'id': '36', 'url': 'ciment', 'start': 1},
                # {'id': '37', 'url': 'chauffage', 'start': 1},
                # {'id': '38', 'url': 'bateau', 'start': 1},
                # {'id': '39', 'url': 'climatisation', 'start': 1},
                # {'id': '41', 'url': 'acier', 'start': 1},
                # {'id': '42', 'url': 'produits+chimiques', 'start': 1},
                # {'id': '43', 'url': 'gaz', 'start': 1},
                # {'id': '44', 'url': 'achat+or', 'start': 1},
                # {'id': '45', 'url': 'énergie', 'start': 1},
                # {'id': '46', 'url': 'agriculteur', 'start': 1},
            ]

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'},  # edmonton
                # {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
                # {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
                # {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
                # {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'},
                # #saint john
                # {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
                # {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
                # {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
                # {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
                # {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
                # {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
                # {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
                # {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        city = capitale.get('nom')
                        url_search = "https://www.pagesjaunes.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        i_1 = 0

                        if number_of_pages > 1:
                            for i in range(activite.get('start'), number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        i_1 += 1

                                                        try:
                                                            if listing.find("a", {
                                                                "class": "listing__name--link"}) is not None:
                                                                website = "https://www.pagesjaunes.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_contact = website

                                                                    print(url_contact)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html_contact = rt.get(url_contact, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')
                                                                        print('\n')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(
                                                                            action="ignore",
                                                                            message="unclosed",
                                                                            category=ResourceWarning
                                                                        )

                                                                        time.sleep(5)

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = True
                                                                        browser = webdriver.Firefox(
                                                                            executable_path='geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_contact)
                                                                        print('page opened')

                                                                        time.sleep(15)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                "email_input"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                "first_name_input"
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                "last_name_input"
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )

                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print('error last_name_input inserted '
                                                                                  ': ' + str(e))

                                                                        time.sleep(10)

                                                                        # click on the "Yes" checkbox
                                                                        yes_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="agreementMessage"]'
                                                                        )
                                                                        yes_checkbox.click()
                                                                        print('yes_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the "Send the copy of the message"
                                                                        # checkbox
                                                                        copy_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="sendCopy"]'
                                                                        )
                                                                        copy_checkbox.click()
                                                                        print('copy_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            send_button = browser.find_element_by_xpath(
                                                                                '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                            )
                                                                            send_button.click()
                                                                            print('send_button.click()')
                                                                        except Exception as e:
                                                                            print("error send_button : " + str(e))

                                                                        time.sleep(10)

                                                                        # Print the success
                                                                        try:
                                                                            success = browser.find_element_by_xpath(
                                                                                "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                            ).get_attribute("data-msg-name")
                                                                            print('success : ' + str(success))
                                                                        except Exception as e:
                                                                            print('error success : ' + str(e))

                                                                        time.sleep(10)

                                                                        print("ccleaner running")
                                                                        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(10)

                                                                        browser.quit()
                                                                        print('browser.quit()')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))
                                                            else:
                                                                print("")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    i_1 += 1

                                                    try:
                                                        if listing.find("a",
                                                                        {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.pagesjaunes.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_contact = website

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html_contact = rt.get(
                                                                    url_contact,
                                                                    headers=headers
                                                                )

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                if soup.find('li', {
                                                                    'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')
                                                                    print('\n')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(
                                                                        action="ignore",
                                                                        message="unclosed",
                                                                        category=ResourceWarning
                                                                    )

                                                                    time.sleep(5)

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = True
                                                                    browser = webdriver.Firefox(
                                                                        executable_path='geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_contact)
                                                                    print('page opened')

                                                                    time.sleep(15)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            "email_input"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            "first_name_input"
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            "last_name_input"
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error last_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )

                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted '
                                                                              ': ' + str(e))

                                                                    time.sleep(10)

                                                                    # click on the "Yes" checkbox
                                                                    yes_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="agreementMessage"]'
                                                                    )
                                                                    yes_checkbox.click()
                                                                    print('yes_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the "Send the copy of the message"
                                                                    # checkbox
                                                                    copy_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="sendCopy"]'
                                                                    )
                                                                    copy_checkbox.click()
                                                                    print('copy_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        send_button = browser.find_element_by_xpath(
                                                                            '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                        )
                                                                        send_button.click()
                                                                        print('send_button.click()')
                                                                    except Exception as e:
                                                                        print("error send_button : " + str(e))

                                                                    time.sleep(10)

                                                                    # Print the success
                                                                    try:
                                                                        success = browser.find_element_by_xpath(
                                                                            "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                        ).get_attribute("data-msg-name")
                                                                        print('success : ' + str(success))
                                                                    except Exception as e:
                                                                        print('error success : ' + str(e))

                                                                    time.sleep(10)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(10)

                                                                    browser.quit()
                                                                    print('browser.quit()')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))
                                                        else:
                                                            print("a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')

    # ok
    def test_send_a_message_for_companies_for_selling_electricity_with_clear_web(self):
        print('test_send_a_message_for_companies_for_selling_electricity_with_clear_web')

        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) '
                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                              'Chrome/51.0.2704.103'
            }

            activites = [
                {'id': '1', 'url': 'agence+de+placement', 'start': 1},
                # {'id': '2', 'url': 'agence+immobilière', 'start': 1},
                # {'id': '3', 'url': "recrutement", 'start': 1},
                # {'id': '4', 'url': 'logiciel', 'start': 1},
                # {'id': '5', 'url': 'hotel', 'start': 1},
                # {'id': '6', 'url': 'social', 'start': 1},
                # {'id': '7', 'url': 'nettoyage', 'start': 1},
                # {'id': '8', 'url': 'association', 'start': 1},
                # {'id': '9', 'url': 'etablissement+financier', 'start': 1},
                # {'id': '10', 'url': 'restaurant', 'start': 1},
                # {'id': '11', 'url': 'batiment', 'start': 1},
                # {'id': '12', 'url': 'coiffeur', 'start': 1},
                # {'id': '13', 'url': 'fleuriste', 'start': 1},
                # {'id': '14', 'url': 'serrurier', 'start': 1},
                # {'id': '15', 'url': 'boulangerie', 'start': 1},
                # {'id': '16', 'url': 'assurance', 'start': 1},
                # {'id': '17', 'url': 'pharmacie', 'start': 1},
                # {'id': '18', 'url': 'demenagement', 'start': 1},
                # {'id': '19', 'url': 'electricite', 'start': 1},
                # {'id': '20', 'url': 'plomberie', 'start': 1},
                # {'id': '21', 'url': 'securite', 'start': 1},
                # {'id': '22', 'url': 'avocat', 'start': 1},
                # {'id': '23', 'url': 'banque', 'start': 1},
                # {'id': '24', 'url': 'garage', 'start': 1},
                # {'id': '25', 'url': 'dentiste', 'start': 1},
                # {'id': '26', 'url': 'docteur', 'start': 1},
                # {'id': '27', 'url': 'comptable', 'start': 1},
                # {'id': '28', 'url': 'supermarche', 'start': 1},
                # {'id': '29', 'url': 'notaire', 'start': 1},
                # {'id': '30', 'url': 'bijoutier', 'start': 1},
                # {'id': '31', 'url': 'couturier', 'start': 1},
                # {'id': '32', 'url': 'boucherie', 'start': 1},
                # {'id': '33', 'url': 'librairie', 'start': 1},
                # {'id': '34', 'url': 'architecte', 'start': 1}
                # {'id': '36', 'url': 'ciment', 'start': 1},
                # {'id': '37', 'url': 'chauffage', 'start': 1},
                # {'id': '38', 'url': 'bateau', 'start': 1},
                # {'id': '39', 'url': 'climatisation', 'start': 1},
                # {'id': '41', 'url': 'acier', 'start': 1},
                # {'id': '42', 'url': 'produits+chimiques', 'start': 1},
                # {'id': '43', 'url': 'gaz', 'start': 1},
                # {'id': '44', 'url': 'achat+or', 'start': 1},
                # {'id': '45', 'url': 'énergie', 'start': 1},
                # {'id': '46', 'url': 'agriculteur', 'start': 1},
            ]

            capitales_du_monde = [
                {'id': '473', 'nom': 'Edmonton+AB', 'pays': 'Canada'}, #edmonton
                # {'id': '474', 'nom': 'Victoria+BC', 'pays': 'Canada'}, #victoria
                # {'id': '475', 'nom': 'Winnipeg+MB', 'pays': 'Canada'}, #winnipeg
                # {'id': '476', 'nom': 'Fredericton+NB', 'pays': 'Canada'}, #fredericton
                # {'id': '477', 'nom': 'Aeroport+De+Saint-Jean-De-Terre-Neuve+St+Johns+NL', 'pays': 'Canada'}, #saint john
                # {'id': '478', 'nom': 'Halifax+NS', 'pays': 'Canada'}, #halifax
                # {'id': '479', 'nom': 'Yellowknife+NT', 'pays': 'Canada'}, #yellowknife
                # {'id': '480', 'nom': 'Iqaluit+NU', 'pays': 'Canada'}, #iqaluit
                # {'id': '481', 'nom': 'Toronto+ON', 'pays': 'Canada'}, #toronto
                # {'id': '482', 'nom': 'Charlottetown+PE', 'pays': 'Canada'}, #charlottetown
                # {'id': '483', 'nom': 'Quebec+QC', 'pays': 'Canada'}, #quebec
                # {'id': '484', 'nom': 'Regina+SK', 'pays': 'Canada'}, #regina
                # {'id': '485', 'nom': 'Whitehorse+YT', 'pays': 'Canada'} #whitehorse
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get('url')
                        city = capitale.get('nom')
                        url_search = "https://www.pagesjaunes.ca/search/si/1/" \
                                     + activity + "/" + city

                        rt = RequestsTor()

                        html_search = rt.get(url_search, headers=headers)

                        rt.new_id()

                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        # find the number of pages
                        try:
                            if soup_search.find("span", {"class": "pageCount"}) is not None:
                                try:
                                    if soup_search.find("span", {"class": "pageCount"}).find("span") is not None:
                                        number_of_pages += int(soup_search
                                                               .find("span", {"class": "pageCount"})
                                                               .find_all("span")[1]
                                                               .text)
                                        print("number_of_pages : " + str(number_of_pages))
                                    else:
                                        print("no span")
                                except Exception as e:
                                    print("error span : " + str(e))
                            else:
                                print("no span class pageCount")
                        except Exception as e:
                            print("error span class pageCount : " + str(e))

                        i_1 = 0

                        if number_of_pages > 1:
                            for i in range(activite.get('start'), number_of_pages + 1):
                                try:
                                    url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/" \
                                                                 + str(i) + "/" \
                                                                 + activity + "/" \
                                                                 + city

                                    print(url_of_one_page_of_results)

                                    time.sleep(3)

                                    rt = RequestsTor()

                                    html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                    rt.new_id()

                                    soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                                'html.parser')

                                    try:
                                        if soup_of_one_page_of_results \
                                                .find("div", {"class": "resultList"}) is not None:
                                            try:
                                                if soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find("div", {"class": "listing"}) is not None:

                                                    all_listing = soup_of_one_page_of_results \
                                                        .find("div", {"class": "resultList"}) \
                                                        .find_all("div", {"class": "listing"})

                                                    for listing in all_listing:
                                                        i_1 += 1

                                                        try:
                                                            if listing.find("a", {
                                                                "class": "listing__name--link"}) is not None:
                                                                website = "https://www.pagesjaunes.ca" + listing \
                                                                    .find("a", {"class": "listing__name--link"}) \
                                                                    .get("href")

                                                                try:
                                                                    url_contact = website

                                                                    print(url_contact)

                                                                    time.sleep(3)

                                                                    rt = RequestsTor()

                                                                    html_contact = rt.get(url_contact, headers=headers)

                                                                    rt.new_id()

                                                                    soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                    if soup.find('li', {
                                                                        'class': 'mlr__item--message'}) is not None:
                                                                        print('yes message button')
                                                                        print('\n')

                                                                        time.sleep(5)

                                                                        warnings.filterwarnings(
                                                                            action="ignore",
                                                                            message="unclosed",
                                                                            category=ResourceWarning
                                                                        )

                                                                        time.sleep(5)

                                                                        firefox_options = Options()
                                                                        firefox_options.headless = False
                                                                        browser = webdriver.Firefox(
                                                                            executable_path='geckodriver.exe',
                                                                            options=firefox_options
                                                                        )

                                                                        # maximize window
                                                                        browser.maximize_window()

                                                                        time.sleep(5)

                                                                        # open
                                                                        browser.get(url_contact)
                                                                        print('page opened')

                                                                        time.sleep(15)

                                                                        # click on the message button
                                                                        message_button = browser.find_element_by_xpath(
                                                                            "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                        )
                                                                        message_button.click()

                                                                        time.sleep(10)

                                                                        # insert the email
                                                                        try:
                                                                            email_input = browser.find_element_by_xpath(
                                                                                '//*[@id="emailMessage"]'
                                                                            )
                                                                            email_input.clear()
                                                                            email_input.send_keys(
                                                                                "email_input"
                                                                            )
                                                                            print("email inserted")
                                                                        except Exception as e:
                                                                            print('error email inserted : ' + str(e))

                                                                        time.sleep(10)

                                                                        # insert the first name
                                                                        try:
                                                                            first_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="firstNameMessage"]'
                                                                            )
                                                                            first_name_input.clear()
                                                                            first_name_input.send_keys(
                                                                                "first_name_input"
                                                                            )
                                                                            print("first_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error first_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the last name
                                                                        try:
                                                                            last_name_input = browser.find_element_by_xpath(
                                                                                '//*[@id="lastNameMessage"]'
                                                                            )
                                                                            last_name_input.clear()
                                                                            last_name_input.send_keys(
                                                                                "last_name_input"
                                                                            )
                                                                            print("last_name_input inserted")
                                                                        except Exception as e:
                                                                            print(
                                                                                'error last_name_input inserted : ' + str(
                                                                                    e))

                                                                        time.sleep(10)

                                                                        # insert the message
                                                                        try:
                                                                            message_input = browser.find_element_by_xpath(
                                                                                '//*[@id="contentMessage"]'
                                                                            )
                                                                            message_input.clear()

                                                                            text = "Hello,\n\n"

                                                                            message_input.send_keys(
                                                                                text
                                                                            )

                                                                            print("message_input inserted")
                                                                        except Exception as e:
                                                                            print('error last_name_input inserted '
                                                                                  ': ' + str(e))

                                                                        time.sleep(10)

                                                                        # click on the "Yes" checkbox
                                                                        yes_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="agreementMessage"]'
                                                                        )
                                                                        yes_checkbox.click()
                                                                        print('yes_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the "Send the copy of the message"
                                                                        # checkbox
                                                                        copy_checkbox = browser.find_element_by_xpath(
                                                                            '//*[@id="sendCopy"]'
                                                                        )
                                                                        copy_checkbox.click()
                                                                        print('copy_checkbox.click()')

                                                                        time.sleep(10)

                                                                        # click on the 'send' button
                                                                        try:
                                                                            send_button = browser.find_element_by_xpath(
                                                                                '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                            )
                                                                            send_button.click()
                                                                            print('send_button.click()')
                                                                        except Exception as e:
                                                                            print("error send_button : " + str(e))

                                                                        time.sleep(10)

                                                                        # Print the success
                                                                        try:
                                                                            success = browser.find_element_by_xpath(
                                                                                "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                            ).get_attribute("data-msg-name")
                                                                            print('success : ' + str(success))
                                                                        except Exception as e:
                                                                            print('error success : ' + str(e))

                                                                        time.sleep(10)

                                                                        print("ccleaner running")
                                                                        os.system("set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                        os.system("start ccleaner /AUTO")

                                                                        time.sleep(10)

                                                                        browser.quit()
                                                                        print('browser.quit()')
                                                                    else:
                                                                        print('no message button')
                                                                        print('\n')
                                                                except Exception as e:
                                                                    print("error url : " + str(e))
                                                            else:
                                                                print("")
                                                        except Exception as e:
                                                            print("no a class listing__name--link : " + str(e))
                                                else:
                                                    print("no listing")
                                            except Exception as e:
                                                print("error  : " + str(e))
                                        else:
                                            print("no resultList")
                                    except Exception as e:
                                        print("error div class resultList : " + str(e))
                                except Exception as e:
                                    print("error url_of_one_page_of_results : " + str(e))
                        else:
                            try:
                                url_of_one_page_of_results = "https://www.pagesjaunes.ca/search/si/1/" \
                                                             + activity + "/" \
                                                             + city

                                print(url_of_one_page_of_results)

                                time.sleep(3)

                                rt = RequestsTor()

                                html_of_one_page_of_results = rt.get(url_of_one_page_of_results, headers=headers)

                                rt.new_id()

                                soup_of_one_page_of_results = BeautifulSoup(html_of_one_page_of_results.content,
                                                                            'html.parser')

                                try:
                                    if soup_of_one_page_of_results \
                                            .find("div", {"class": "resultList"}) is not None:
                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find("div", {"class": "listing"}) is not None:

                                                all_listing = soup_of_one_page_of_results \
                                                    .find("div", {"class": "resultList"}) \
                                                    .find_all("div", {"class": "listing"})

                                                for listing in all_listing:
                                                    i_1 += 1

                                                    try:
                                                        if listing.find("a",
                                                                        {"class": "listing__name--link"}) is not None:
                                                            website = "https://www.pagesjaunes.ca" + listing \
                                                                .find("a", {"class": "listing__name--link"}) \
                                                                .get("href")

                                                            try:
                                                                url_contact = website

                                                                time.sleep(3)

                                                                rt = RequestsTor()

                                                                html_contact = rt.get(
                                                                    url_contact,
                                                                    headers=headers
                                                                )

                                                                rt.new_id()

                                                                soup = BeautifulSoup(html_contact.content, 'html.parser')

                                                                if soup.find('li', {
                                                                    'class': 'mlr__item--message'}) is not None:
                                                                    print('yes message button')
                                                                    print('\n')

                                                                    time.sleep(5)

                                                                    warnings.filterwarnings(
                                                                        action="ignore",
                                                                        message="unclosed",
                                                                        category=ResourceWarning
                                                                    )

                                                                    time.sleep(5)

                                                                    firefox_options = Options()
                                                                    firefox_options.headless = False
                                                                    browser = webdriver.Firefox(
                                                                        executable_path='geckodriver.exe',
                                                                        options=firefox_options
                                                                    )

                                                                    # maximize window
                                                                    browser.maximize_window()

                                                                    time.sleep(5)

                                                                    # open
                                                                    browser.get(url_contact)
                                                                    print('page opened')

                                                                    time.sleep(15)

                                                                    # click on the message button
                                                                    message_button = browser.find_element_by_xpath(
                                                                        "/html/body/div[2]/div[3]/div/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[2]/a"
                                                                    )
                                                                    message_button.click()

                                                                    time.sleep(10)

                                                                    # insert the email
                                                                    try:
                                                                        email_input = browser.find_element_by_xpath(
                                                                            '//*[@id="emailMessage"]'
                                                                        )
                                                                        email_input.clear()
                                                                        email_input.send_keys(
                                                                            "email_input"
                                                                        )
                                                                        print("email inserted")
                                                                    except Exception as e:
                                                                        print('error email inserted : ' + str(e))

                                                                    time.sleep(10)

                                                                    # insert the first name
                                                                    try:
                                                                        first_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="firstNameMessage"]'
                                                                        )
                                                                        first_name_input.clear()
                                                                        first_name_input.send_keys(
                                                                            "first_name_input"
                                                                        )
                                                                        print("first_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error first_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the last name
                                                                    try:
                                                                        last_name_input = browser.find_element_by_xpath(
                                                                            '//*[@id="lastNameMessage"]'
                                                                        )
                                                                        last_name_input.clear()
                                                                        last_name_input.send_keys(
                                                                            "last_name_input"
                                                                        )
                                                                        print("last_name_input inserted")
                                                                    except Exception as e:
                                                                        print(
                                                                            'error last_name_input inserted : ' + str(
                                                                                e))

                                                                    time.sleep(10)

                                                                    # insert the message
                                                                    try:
                                                                        message_input = browser.find_element_by_xpath(
                                                                            '//*[@id="contentMessage"]'
                                                                        )
                                                                        message_input.clear()

                                                                        text = "Hello,\n\n"

                                                                        message_input.send_keys(
                                                                            text
                                                                        )

                                                                        print("message_input inserted")
                                                                    except Exception as e:
                                                                        print('error last_name_input inserted '
                                                                              ': ' + str(e))

                                                                    time.sleep(10)

                                                                    # click on the "Yes" checkbox
                                                                    yes_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="agreementMessage"]'
                                                                    )
                                                                    yes_checkbox.click()
                                                                    print('yes_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the "Send the copy of the message"
                                                                    # checkbox
                                                                    copy_checkbox = browser.find_element_by_xpath(
                                                                        '//*[@id="sendCopy"]'
                                                                    )
                                                                    copy_checkbox.click()
                                                                    print('copy_checkbox.click()')

                                                                    time.sleep(10)

                                                                    # click on the 'send' button
                                                                    try:
                                                                        send_button = browser.find_element_by_xpath(
                                                                            '/html/body/div[5]/div/div/div/div[2]/form/div[6]/button'
                                                                        )
                                                                        send_button.click()
                                                                        print('send_button.click()')
                                                                    except Exception as e:
                                                                        print("error send_button : " + str(e))

                                                                    time.sleep(10)

                                                                    # Print the success
                                                                    try:
                                                                        success = browser.find_element_by_xpath(
                                                                            "/html/body/div[5]/div/div/div/div[2]/div[2]"
                                                                        ).get_attribute("data-msg-name")
                                                                        print('success : ' + str(success))
                                                                    except Exception as e:
                                                                        print('error success : ' + str(e))

                                                                    time.sleep(10)

                                                                    print("ccleaner running")
                                                                    os.system(
                                                                        "set ccleaner='C:\\Program Files\\CCleaner\\CCleaner.exe'")
                                                                    os.system("start ccleaner /AUTO")

                                                                    time.sleep(10)

                                                                    browser.quit()
                                                                    print('browser.quit()')
                                                                else:
                                                                    print('no message button')
                                                                    print('\n')
                                                            except Exception as e:
                                                                print("error url : " + str(e))
                                                        else:
                                                            print("a class listing__name--link")
                                                    except Exception as e:
                                                        print("no a class listing__name--link : " + str(e))
                                            else:
                                                print("no listing")
                                        except Exception as e:
                                            print("error  : " + str(e))
                                    else:
                                        print("no resultList")
                                except Exception as e:
                                    print("error div class resultList : " + str(e))
                            except Exception as e:
                                print("error url_of_one_page_of_results : " + str(e))
                    except Exception as e:
                        print("error url_search : " + str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
