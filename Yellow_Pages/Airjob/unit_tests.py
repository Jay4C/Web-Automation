import unittest
import time
import requests
from bs4 import BeautifulSoup
from pywinauto.application import Application
import pywinauto.mouse
import pywinauto.keyboard


class UnitTestsDesktopAutomationAirjob(unittest.TestCase):
    def test_connect_to_my_account_from_one_ad(self):
        app = Application(backend="uia")

        url_ad = ""

        time.sleep(3)

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(6)

        pywinauto.keyboard.send_keys(url_ad)

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        pywinauto.mouse.click(button="left", coords=(230, 460))

        time.sleep(3)

        pywinauto.mouse.click(button="left", coords=(500, 305))

        time.sleep(3)

        # Type the email
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(3)

        # Type the password
        pywinauto.keyboard.send_keys("")

        time.sleep(3)

        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(3)

        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(6)

        # click on Postuler
        pywinauto.mouse.click(button="left", coords=(230, 460))

        time.sleep(4)

        # click on CV
        pywinauto.mouse.click(button="left", coords=(900, 180))

        time.sleep(4)

        # select the file
        pywinauto.mouse.click(button="left", coords=(340, 50))
        time.sleep(3)
        pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
        time.sleep(3)
        pywinauto.keyboard.send_keys('{ENTER}')
        time.sleep(3)
        pywinauto.mouse.click(button="left", coords=(300, 230))
        time.sleep(3)
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(4)

        # select the input for the message
        pywinauto.mouse.click(button="left", coords=(860, 260))

        time.sleep(4)

        # write the message
        pywinauto.keyboard.send_keys("""
        """)

        time.sleep(4)

        pywinauto.keyboard.send_keys("{VK_TAB}")

        time.sleep(4)

        # envoyer ma candidature
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # revenir tout en haut de la page
        pywinauto.keyboard.send_keys('{PGUP 7}')

        time.sleep(3)

        # type on the url bar 2 times
        pywinauto.mouse.click(button="left", coords=(820, 50))
        time.sleep(2)
        pywinauto.mouse.click(button="left", coords=(820, 50))

        time.sleep(4)

        # erase the phrase (#postuler)
        pywinauto.keyboard.send_keys('{BACKSPACE 9}')

        time.sleep(4)

        # refresh the page
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(4)

        # Je me déconnecte
        pywinauto.mouse.click(button="left", coords=(1200, 230))

        time.sleep(4)

        # Close the browser
        pywinauto.keyboard.send_keys('%{F4}')

        time.sleep(5)

    def test_connect_to_my_account_from_several_ads(self):
        app = Application(backend="uia")

        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            print(url_ad)

            time.sleep(3)

            # Ouvrir l'application CCleaner
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(3)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(500, 305))

            time.sleep(3)

            # Type the email
            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            # Type the password
            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            # click on Postuler
            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(4)

            # click on CV
            pywinauto.mouse.click(button="left", coords=(900, 180))

            time.sleep(4)

            # select the file
            pywinauto.mouse.click(button="left", coords=(340, 50))
            time.sleep(3)
            pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')
            time.sleep(3)
            pywinauto.mouse.click(button="left", coords=(300, 230))
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # select the input for the message
            pywinauto.mouse.click(button="left", coords=(860, 260))

            time.sleep(4)

            # write the message
            pywinauto.keyboard.send_keys("""
            """)

            time.sleep(4)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(4)

            # envoyer ma candidature
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            # type on the url bar 2 times
            pywinauto.mouse.click(button="left", coords=(820, 50))
            time.sleep(2)
            pywinauto.mouse.click(button="left", coords=(820, 50))

            time.sleep(4)

            # erase the phrase (#postuler)
            pywinauto.keyboard.send_keys('{BACKSPACE 9}')

            time.sleep(4)

            # refresh the page
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # Je me déconnecte
            pywinauto.mouse.click(button="left", coords=(1200, 230))

            time.sleep(4)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_up_from_the_bottom(self):
        print("test_up_from_the_bottom")

        app = Application(backend="uia")

        time.sleep(3)

        # Ouvrir l'application CCleaner
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

        time.sleep(3)

        pywinauto.keyboard.send_keys("https://www.airjob.fr/annonce/consultant-scrum-master-confirme-h-f")

        time.sleep(3)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{DOWN 20}')

        time.sleep(3)

        pywinauto.keyboard.send_keys('{PGUP 7}')

    def test_connect_to_my_account_from_several_ads_from_one_result_page(self):
        app = Application(backend="uia")

        urls_ad = [
            ""
        ]

        for url_ad in urls_ad:
            print(url_ad)

            time.sleep(3)

            # Ouvrir l'application CCleaner
            app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

            time.sleep(6)

            pywinauto.keyboard.send_keys(url_ad)

            time.sleep(3)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(3)

            pywinauto.mouse.click(button="left", coords=(500, 305))

            time.sleep(3)

            # Type the email
            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(3)

            # Type the password
            pywinauto.keyboard.send_keys("")

            time.sleep(3)

            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(3)

            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(6)

            # click on Postuler
            pywinauto.mouse.click(button="left", coords=(230, 460))

            time.sleep(4)

            # click on CV
            pywinauto.mouse.click(button="left", coords=(900, 180))

            time.sleep(4)

            # select the file
            pywinauto.mouse.click(button="left", coords=(340, 50))
            time.sleep(3)
            pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')
            time.sleep(3)
            pywinauto.mouse.click(button="left", coords=(300, 230))
            time.sleep(3)
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # select the input for the message
            pywinauto.mouse.click(button="left", coords=(860, 260))

            time.sleep(4)

            # write the message
            pywinauto.keyboard.send_keys("""
            """)

            time.sleep(4)

            pywinauto.keyboard.send_keys("{VK_TAB}")

            time.sleep(4)

            # envoyer ma candidature
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            # type on the url bar 2 times
            pywinauto.mouse.click(button="left", coords=(820, 50))
            time.sleep(2)
            pywinauto.mouse.click(button="left", coords=(820, 50))

            time.sleep(4)

            # erase the phrase (#postuler)
            pywinauto.keyboard.send_keys('{BACKSPACE 9}')

            time.sleep(4)

            # refresh the page
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(4)

            # Je me déconnecte
            pywinauto.mouse.click(button="left", coords=(1200, 230))

            time.sleep(4)

            # Close the browser
            pywinauto.keyboard.send_keys('%{F4}')

            time.sleep(5)

    def test_extract_all_pages_from_one_result_page(self):
        print("test_extract_all_pages_from_one_result_page")

        url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:2"

        # Request the content of a page from the url
        html = requests.get(url_result_page)

        time.sleep(3)

        # Parse the content of html_doc
        soup = BeautifulSoup(html.content, 'html.parser')

        if soup.find('div', {'class': 'un-resultat'}) is not None:
            print("offres ok")

            all_offre = soup.find_all('div', {'class': 'un-resultat'})

            i = 1

            for offre in all_offre:
                print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                           .find('a', {'class': 'resultat-titre'})
                                                                           .get('href')))

                i += 1
        else:
            print("no offres")

    def test_extract_all_pages_from_all_result_page(self):
        print("test_extract_all_pages_from_all_result_page")

        i = 1

        for x in range(2, 148):
            print("result page : " + str(x))

            url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'un-resultat'}) is not None:
                print("offres ok")

                all_offre = soup.find_all('div', {'class': 'un-resultat'})

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                              .find('a', {'class': 'resultat-titre'})
                                                                              .get('href')))

                    i += 1
            else:
                print("no offres")

    def test_connect_to_my_account_from_several_ads_from_all_result_page(self):
        print("test_connect_to_my_account_from_several_ads_from_all_result_page")

        app = Application(backend="uia")

        i = 1

        # 148
        for x in range(3, 4):
            print("result page : " + str(x))

            url_result_page = "https://www.airjob.fr/recherche/keywords:d%25C3%25A9veloppeur,,l:10,p:" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.find('div', {'class': 'un-resultat'}) is not None:
                print("offres ok")

                all_offre = soup.find_all('div', {'class': 'un-resultat'})

                for offre in all_offre:
                    print("link " + str(i) + " : https://www.airjob.fr" + str(offre
                                                                              .find('a', {'class': 'resultat-titre'})
                                                                              .get('href')))

                    i += 1

                    url_ad = "https://www.airjob.fr" + str(offre.find('a', {'class': 'resultat-titre'}).get('href'))

                    time.sleep(3)

                    # Ouvrir l'application CCleaner
                    app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

                    time.sleep(6)

                    pywinauto.keyboard.send_keys(url_ad)

                    time.sleep(3)

                    # Press the 'Enter' button
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(6)

                    pywinauto.mouse.click(button="left", coords=(230, 460))

                    time.sleep(3)

                    pywinauto.mouse.click(button="left", coords=(500, 305))

                    time.sleep(3)

                    # Type the email
                    pywinauto.keyboard.send_keys("")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(3)

                    # Type the password
                    pywinauto.keyboard.send_keys("")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys("{VK_TAB 2}")

                    time.sleep(3)

                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(6)

                    # click on Postuler
                    pywinauto.mouse.click(button="left", coords=(230, 460))

                    time.sleep(4)

                    # click on CV
                    pywinauto.mouse.click(button="left", coords=(900, 180))

                    time.sleep(4)

                    # select the file
                    pywinauto.mouse.click(button="left", coords=(340, 50))
                    time.sleep(3)
                    pywinauto.keyboard.send_keys("C:\\Users\\DELL\\Documents")
                    time.sleep(3)
                    pywinauto.keyboard.send_keys('{ENTER}')
                    time.sleep(3)
                    pywinauto.mouse.click(button="left", coords=(300, 230))
                    time.sleep(3)
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(4)

                    # select the input for the message
                    pywinauto.mouse.click(button="left", coords=(860, 260))

                    time.sleep(4)

                    # write the message
                    pywinauto.keyboard.send_keys("""
                            """)

                    time.sleep(4)

                    pywinauto.keyboard.send_keys("{VK_TAB}")

                    time.sleep(4)

                    # envoyer ma candidature
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(7)

                    # revenir tout en haut de la page
                    pywinauto.keyboard.send_keys('{PGUP 7}')

                    time.sleep(4)

                    # type on the url bar 2 times
                    pywinauto.mouse.click(button="left", coords=(820, 50))
                    time.sleep(2)
                    pywinauto.mouse.click(button="left", coords=(820, 50))

                    time.sleep(4)

                    # erase the phrase (#postuler)
                    pywinauto.keyboard.send_keys('{BACKSPACE 9}')

                    time.sleep(4)

                    # refresh the page
                    pywinauto.keyboard.send_keys('{ENTER}')

                    time.sleep(4)

                    # Je me déconnecte
                    pywinauto.mouse.click(button="left", coords=(1200, 230))

                    time.sleep(4)

                    # Close the browser
                    pywinauto.keyboard.send_keys('%{F4}')

                    time.sleep(5)
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
