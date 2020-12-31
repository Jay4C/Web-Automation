import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import requests
from bs4 import BeautifulSoup


class UnitTestsDesktopAutomationYellowPagesCanada(unittest.TestCase):
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


if __name__ == '__main__':
    unittest.main()
