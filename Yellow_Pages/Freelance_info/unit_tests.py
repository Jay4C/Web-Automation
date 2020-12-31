import unittest
import time
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsDesktopAutomationFreelanceInfo(unittest.TestCase):
    def test_connect_to_my_account_from_one_ad(self):
        app = Application(backend="uia")

        url_ad = ""

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(6)

        # Open the Freelance-info.fr
        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        pywinauto.mouse.click(button="left", coords=(500, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(600, 450))

        time.sleep(3)

        # Type the eamil
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Type the password
        pywinauto.keyboard.send_keys('')

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        pywinauto.mouse.click(button="left", coords=(500, 670))

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(1170, 85))

        time.sleep(5)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_connect_to_my_account_from_several_ads(self):
        app = Application(backend="uia")

        urls_ad = [
            "https://www.freelance-info.fr/mission/ingenieur-citrix-ivanti-1563088",
            "https://www.freelance-info.fr/mission/developpeur-python-1563083",
            "https://www.freelance-info.fr/mission/chef-de-projet-securite-it-maroc-1563078",
            "https://www.freelance-info.fr/mission/developpeur-front-end-liferay-j-ee-h-f-1563065",
            "https://www.freelance-info.fr/mission/lsa-pega-1563058",
            "https://www.freelance-info.fr/mission/developpeur-net-core-azure-1563047"
        ]

        for url_ad in urls_ad:
            # Ouvrir l'application CCleaner
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            # Open the Freelance-info.fr
            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(3)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            pywinauto.mouse.click(button="left", coords=(500, 670))

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(600, 450))

            time.sleep(3)

            # Type the email
            pywinauto.keyboard.send_keys('')

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            # Type the password
            pywinauto.keyboard.send_keys('')

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            pywinauto.mouse.click(button="left", coords=(500, 670))

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(1170, 85))

            time.sleep(5)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_extract_all_pages_from_one_result_page(self):
        print("test_extract_all_pages_from_one_result_page")

        url_result_page = "https://www.freelance-info.fr/missions?remote=1&page=2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.select("#offre") is not None:
            print("offres ok")

            all_offre = soup.select("#offre")

            i = 1

            for offre in all_offre:
                print("link " + str(i) + " : https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href'))

                i += 1
        else:
            print("no offres")

    def test_extract_all_pages_from_all_result_page(self):
        print("test_extract_all_pages_from_all_result_page")

        i = 1

        for x in range(2, 55):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?remote=1&page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.freelance-info.fr"
                          + offre.select_one("#titre-mission").find('a').get('href'))

                    i += 1
            else:
                print("no offres")

    def test_connect_to_my_account_from_several_ads_from_all_result_page(self):
        print("test_connect_to_my_account_from_several_ads_from_all_result_page")

        i = 1

        # 55
        for x in range(3, 4):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions?remote=1&page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.freelance-info.fr"
                          + offre.select_one("#titre-mission").find('a').get('href'))

                    app = Application(backend="uia")

                    url_ad = "https://www.freelance-info.fr" + str(offre
                                                                   .select_one("#titre-mission")
                                                                   .find('a')
                                                                   .get('href'))

                    # Ouvrir l'application CCleaner
                    app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                    time.sleep(6)

                    # Open the Freelance-info.fr
                    pywinauto.keyboard.send_keys(url_ad)

                    time.sleep(3)

                    # Press the 'Enter' button
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(6)

                    pywinauto.mouse.click(button="left", coords=(500, 670))

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(3)

                    pywinauto.mouse.click(button="left", coords=(600, 450))

                    time.sleep(3)

                    # Type the email
                    pywinauto.keyboard.send_keys('')

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    # Type the password
                    pywinauto.keyboard.send_keys('')

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(7)

                    pywinauto.mouse.click(button="left", coords=(500, 670))

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(3)

                    pywinauto.mouse.click(button="left", coords=(1170, 85))

                    time.sleep(5)

                    # Close the browser
                    pywinauto.keyboard.send_keys('%{F4}')

                    time.sleep(5)

                    i += 1
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
