import unittest
import time
from pywinauto.application import Application
import pywinauto.mouse
import pywinauto.keyboard
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import warnings


class UnitTestsDesktopAutomationFreelanceInfoWithPywinauto(unittest.TestCase):
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


class UnitTestsDesktopAutomationFreelanceInfoWithSeleniumWebdriver(unittest.TestCase):
    # ok
    def test_se_connecter(self):
        print("test_se_connecter")

        email = ""

        password = ""

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://www.freelance-info.fr/login-page.php')

        time.sleep(15)

        accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/a"
        )
        accepter_button.click()

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            '//*[@id="_username"]'
        )
        email_input.clear()
        email_input.send_keys(email)

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="_password"]'
        )
        password_input.clear()
        password_input.send_keys(password)

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '//*[@id="connecter-button"]'
        )
        log_in_button.click()

        time.sleep(5)

    # ok
    def test_send_my_cv_for_one_ad_without_headless(self):
        print("test_send_my_cv_for_one_ad")

        email = ""

        password = ""

        url_ad = 'https://www.freelance-info.fr/mission/developpeur-python-h-f-1676844?hl=python'
        print("url_ad : " + url_ad)

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe'
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_ad)
        print('browser.get(url_ad)')

        time.sleep(15)

        accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/a"
        )
        accepter_button.click()
        print("accepter_button.click()")

        time.sleep(5)

        postuler_button = browser.find_element_by_xpath(
            '//*[@id="depose-cv-mission"]'
        )
        postuler_button.click()
        print("postuler_button.click()")

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            '//*[@id="_username"]'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys()')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="_password"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys()')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '//*[@id="connecter-button"]'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(10)

        envoyer_candidature_button = browser.find_element_by_xpath(
            '//*[@id="depose-cv-mission-envoyer"]'
        )
        envoyer_candidature_button.click()
        print('envoyer_candidature_button.click()')

        time.sleep(10)

        candidature_envoyee = browser.find_element_by_xpath(
            '//*[@id="delete-cv"]'
        ).text
        print(candidature_envoyee)

        time.sleep(10)

        deconnexion_button = browser.find_element_by_xpath(
            '/html/body/div[2]/nav[1]/div/div/div/ul[3]/li[3]/a'
        )
        deconnexion_button.click()
        print('deconnexion_button.click()')

        time.sleep(10)

        browser.close()
        print('browser.close()')

    # ok
    def test_send_my_cv_for_one_ad_with_headless(self):
        print("test_send_my_cv_for_one_ad_with_headless")

        email = ""

        password = ""

        url_ad = 'https://www.freelance-info.fr/mission/data-python-developer-1676778?hl=python'
        print("url_ad : " + url_ad)

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        options = Options()
        options.headless = True
        browser = webdriver.Firefox(
            executable_path='geckodriver.exe',
            options=options
        )

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get(url_ad)
        print('browser.get(url_ad)')

        time.sleep(15)

        accepter_button = browser.find_element_by_xpath(
            "/html/body/div[1]/div/a"
        )
        accepter_button.click()
        print("accepter_button.click()")

        time.sleep(5)

        postuler_button = browser.find_element_by_xpath(
            '//*[@id="depose-cv-mission"]'
        )
        postuler_button.click()
        print("postuler_button.click()")

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            '//*[@id="_username"]'
        )
        email_input.clear()
        email_input.send_keys(email)
        print('email_input.send_keys()')

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="_password"]'
        )
        password_input.clear()
        password_input.send_keys(password)
        print('password_input.send_keys()')

        time.sleep(5)

        log_in_button = browser.find_element_by_xpath(
            '//*[@id="connecter-button"]'
        )
        log_in_button.click()
        print("log_in_button.click()")

        time.sleep(10)

        envoyer_candidature_button = browser.find_element_by_xpath(
            '//*[@id="depose-cv-mission-envoyer"]'
        )
        envoyer_candidature_button.click()
        print('envoyer_candidature_button.click()')

        time.sleep(10)

        candidature_envoyee = browser.find_element_by_xpath(
            '//*[@id="delete-cv"]'
        ).text
        print(candidature_envoyee)

        time.sleep(10)

        deconnexion_button = browser.find_element_by_xpath(
            '/html/body/div[2]/nav[1]/div/div/div/ul[3]/li[3]/a'
        )
        deconnexion_button.click()
        print('deconnexion_button.click()')

        time.sleep(10)

        browser.quit()
        print('browser.quit()')

    # ok
    def test_send_my_cv_for_several_ads_with_headless(self):
        print("test_send_my_cv_for_one_ad_with_headless")

        urls_ad = [

        ]

        for url_ad in urls_ad:
            email = ""

            password = ""

            print("url_ad : " + url_ad)

            time.sleep(5)

            warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

            time.sleep(5)

            # with Firefox
            options = Options()
            options.headless = True
            browser = webdriver.Firefox(
                executable_path='geckodriver.exe',
                options=options
            )

            time.sleep(5)

            # maximize window
            browser.maximize_window()

            time.sleep(5)

            # open
            browser.get(url_ad)
            print('browser.get(url_ad)')

            time.sleep(15)

            accepter_button = browser.find_element_by_xpath(
                "/html/body/div[1]/div/a"
            )
            accepter_button.click()
            print("accepter_button.click()")

            time.sleep(5)

            postuler_button = browser.find_element_by_xpath(
                '//*[@id="depose-cv-mission"]'
            )
            postuler_button.click()
            print("postuler_button.click()")

            time.sleep(5)

            email_input = browser.find_element_by_xpath(
                '//*[@id="_username"]'
            )
            email_input.clear()
            email_input.send_keys(email)
            print('email_input.send_keys()')

            time.sleep(5)

            password_input = browser.find_element_by_xpath(
                '//*[@id="_password"]'
            )
            password_input.clear()
            password_input.send_keys(password)
            print('password_input.send_keys()')

            time.sleep(5)

            log_in_button = browser.find_element_by_xpath(
                '//*[@id="connecter-button"]'
            )
            log_in_button.click()
            print("log_in_button.click()")

            time.sleep(10)

            try:
                envoyer_candidature_button = browser.find_element_by_xpath(
                    '//*[@id="depose-cv-mission-envoyer"]'
                )
                envoyer_candidature_button.click()
                print('envoyer_candidature_button.click()')
            except Exception as e:
                print('error envoyer_candidature_button : ' + str(e))

            time.sleep(10)

            try:
                candidature_envoyee = browser.find_element_by_xpath(
                    '//*[@id="delete-cv"]'
                ).text
                print(candidature_envoyee)
            except Exception as e:
                print("error candidature_envoyee : " + str(e))

            time.sleep(10)

            try:
                deconnexion_button = browser.find_element_by_xpath(
                    '/html/body/div[2]/nav[1]/div/div/div/ul[3]/li[3]/a'
                )
                deconnexion_button.click()
                print('deconnexion_button.click()')
            except Exception as e:
                print('error deconnexion_button : ' + str(e))

            time.sleep(10)

            browser.quit()
            print('browser.quit()')

    # ok
    def test_send_my_cv_for_several_ads_with_data_mining_and_headless(self):
        print("test_send_my_cv_for_several_ads_with_data_mining_and_headless")

        i = 0

        options = Options()
        options.headless = True

        email = ""

        password = ""

        for x in range(1, 22):
            print("result page : " + str(x))

            url_result_page = "https://www.freelance-info.fr/missions/ile-de-france?keywords=d%C3%A9veloppeur%20python&page=" + str(x)

            # Request the content of a page from the url
            html = requests.get(url_result_page)

            time.sleep(3)

            # Parse the content of html_doc
            soup = BeautifulSoup(html.content, 'html.parser')

            if soup.select("#offre") is not None:
                print("offres ok")

                all_offre = soup.select("#offre")

                for offre in all_offre:
                    link = "https://www.freelance-info.fr" + offre.select_one("#titre-mission").find('a').get('href')

                    print("url_ad " + str(i) + " : " + link)

                    time.sleep(5)

                    warnings.filterwarnings(
                        action="ignore",
                        message="unclosed",
                        category=ResourceWarning
                    )

                    time.sleep(5)

                    # with Firefox
                    browser = webdriver.Firefox(
                        executable_path='geckodriver.exe',
                        options=options
                    )

                    time.sleep(5)

                    # maximize window
                    browser.maximize_window()

                    time.sleep(5)

                    # open
                    browser.get(link)
                    print('browser.get(url_ad)')

                    time.sleep(15)

                    accepter_button = browser.find_element_by_xpath(
                        "/html/body/div[1]/div/a"
                    )
                    accepter_button.click()
                    print("accepter_button.click()")

                    time.sleep(5)

                    try:
                        postuler_button = browser.find_element_by_xpath(
                            '//*[@id="depose-cv-mission"]'
                        )
                        postuler_button.click()
                        print("postuler_button.click()")

                        time.sleep(5)

                        email_input = browser.find_element_by_xpath(
                            '//*[@id="_username"]'
                        )
                        email_input.clear()
                        email_input.send_keys(email)
                        print('email_input.send_keys()')

                        time.sleep(5)

                        password_input = browser.find_element_by_xpath(
                            '//*[@id="_password"]'
                        )
                        password_input.clear()
                        password_input.send_keys(password)
                        print('password_input.send_keys()')

                        time.sleep(5)

                        log_in_button = browser.find_element_by_xpath(
                            '//*[@id="connecter-button"]'
                        )
                        log_in_button.click()
                        print("log_in_button.click()")

                        time.sleep(10)

                        try:
                            envoyer_candidature_button = browser.find_element_by_xpath(
                                '//*[@id="depose-cv-mission-envoyer"]'
                            )
                            envoyer_candidature_button.click()
                            print('envoyer_candidature_button.click()')
                        except Exception as e:
                            print('error envoyer_candidature_button : ' + str(e))

                        time.sleep(10)

                        try:
                            candidature_envoyee = browser.find_element_by_xpath(
                                '//*[@id="delete-cv"]'
                            ).text
                            print(candidature_envoyee)
                        except Exception as e:
                            print("error candidature_envoyee : " + str(e))

                        time.sleep(10)

                        try:
                            deconnexion_button = browser.find_element_by_xpath(
                                '/html/body/div[2]/nav[1]/div/div/div/ul[3]/li[3]/a'
                            )
                            deconnexion_button.click()
                            print('deconnexion_button.click()')
                        except Exception as e:
                            print('error deconnexion_button : ' + str(e))
                    except Exception as e:
                        print('error postuler_button : ' + str(e))

                    time.sleep(10)

                    browser.quit()
                    print('browser.quit()')

                    i += 1
            else:
                print("no offres")


if __name__ == '__main__':
    unittest.main()
