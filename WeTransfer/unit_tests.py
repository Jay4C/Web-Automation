import unittest
import time
import warnings
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class UnitTestsWebAutomationWeTransferWithoutHeadless(unittest.TestCase):
    # ok
    def test_open_one_page(self):
        print("test_open_one_page")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://wetransfer.com/')

        time.sleep(5)

    # ok
    def test_send_one_email_with_one_file(self):
        print("test_send_one_email_with_one_file")

        envoye_a = ''

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='..\\geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open
        browser.get('https://wetransfer.com/')

        time.sleep(10)

        # click on the button "Non merci"
        non_merci_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[2]/div[2]/div[2]/div[1]/div[3]/div[4]/button[3]"
        )
        non_merci_button.click()
        print("non_merci_button.click()")

        time.sleep(5)

        # click on the button "J'accepte"
        j_accepte_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button"
        )
        j_accepte_button.click()
        print("j_accepte_button.click()")

        time.sleep(5)

        envoye_a_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[1]/div/div/input"
        )
        envoye_a_input.clear()
        envoye_a_input.send_keys(envoye_a)
        print("envoye_a_input inserted : " + str(envoye_a))

        time.sleep(5)

        votre_adresse_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[2]/input"
        )
        votre_adresse_input.clear()
        votre_adresse_input.send_keys("email")
        print("votre_adresse_input inserted")

        time.sleep(5)

        titre_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[3]/div/input"
        )
        titre_input.clear()
        titre_input.send_keys(
            "messsage"
        )
        print("titre_input inserted")

        time.sleep(5)

        file_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[1]/form/input[1]"
        )
        file_input.send_keys(
            "filename.pdf"
        )
        print("file_input inserted")

        time.sleep(5)

        message_input = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[1]/div[1]/div[2]/div[4]/div/textarea"
        )
        message_input.clear()
        message_input.send_keys(
"""
Hello world,
"""
        )
        print("message_input inserted")

        time.sleep(10)

        # click on the button "Transférer"
        transferer_button = browser.find_element_by_xpath(
            "/html/body/div[2]/div/div[3]/div/div[2]/button[2]"
        )
        transferer_button.click()
        print("transferer_button.click()")

        time.sleep(5)

        # Outlook

        # Open a new window
        browser.execute_script("window.open('');")

        # Switch to the new window and open new URL
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # open
        browser.get('https://outlook.live.com/owa/')

        time.sleep(5)

        # click on the button "Connexion"
        connexion_button = browser.find_element_by_xpath(
            "/html/body/header/div/aside/div/nav/ul/li[2]/a"
        )
        connexion_button.click()
        print("connexion_button.click()")

        time.sleep(5)

        email_input = browser.find_element_by_xpath(
            '//*[@id="i0116"]'
        )
        email_input.clear()
        email_input.send_keys("email_outlook")
        email_input.send_keys(Keys.ENTER)
        print("email_input inserted")

        time.sleep(5)

        password_input = browser.find_element_by_xpath(
            '//*[@id="i0118"]'
        )
        password_input.clear()
        password_input.send_keys("password_outlook")
        password_input.send_keys(Keys.ENTER)
        print("password_input inserted")

        time.sleep(5)

        # click on the checkbox "Ne plus afficher ce message"
        ne_plus_afficher_ce_message_checkbox = browser.find_element_by_xpath(
            '//*[@id="KmsiCheckboxField"]'
        )
        ne_plus_afficher_ce_message_checkbox.click()
        print("ne_plus_afficher_ce_message_checkbox.click()")

        time.sleep(5)

        # click on the button "Non"
        non_button = browser.find_element_by_xpath(
            '//*[@id="idBtn_Back"]'
        )
        non_button.click()
        print("non_button.click()")

        time.sleep(15)

        # Retrieve the code
        code = browser.find_element_by_xpath(
            "/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[3]/div/div/div/div"
            "/div/div[2]/div/div/div/div/div[2]/div/div[1]/span"
        ).text.replace('Votre code est : ', '')
        print('code : ' + str(code))

        time.sleep(5)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[0])

        time.sleep(5)

        code_input = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[1]/div/input'
        )
        code_input.clear()
        code_input.send_keys(str(code))
        print("code_input inserted")

        time.sleep(5)

        # click on the button "Vérification"
        verification_button = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div[3]/form/div[2]/button[2]'
        )
        verification_button.click()
        print("verification_button.click()")

        time.sleep(10)

        # Switch to the last window
        browser.switch_to.window(browser.window_handles[1])

        time.sleep(5)

        # click on the button "Sélectionner tous les messages"
        selectionner_tous_les_messages_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[2]/div/div[1]/div[1]/div[1]/div/div[1]'
            '/div/i[2]'
        )
        selectionner_tous_les_messages_button.click()
        print("selectionner_tous_les_messages_button.click()")

        # click on the button "Vider Prioritaire"
        vider_prioritaire_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[2]/div[2]/div[1]/div/div/div[3]/div[1]/div/div/div/div/div/div[1]/div[1]/button'
        )
        vider_prioritaire_button.click()
        print("vider_prioritaire_button.click()")

        time.sleep(5)

        # click on the button "Ok"
        ok_button = browser.find_element_by_xpath(
            '//*[@id="ok-1"]'
        )
        ok_button.click()
        print("ok_button.click()")

        time.sleep(5)

        # click on the button "Mon profile"
        mon_profile_button = browser.find_element_by_xpath(
            '/html/body/div[3]/div/div[1]/div/div[1]/div[3]/div[1]/button/div/div[2]/div/div/div/div/div/div[2]/img'
        )
        mon_profile_button.click()
        print("mon_profile_button.click()")

        time.sleep(5)

        # click on the button "Se déconnecter"
        se_deconnecter_button = browser.find_element_by_xpath(
            '//*[@id="mectrl_body_signOut"]'
        )
        se_deconnecter_button.click()
        print("se_deconnecter_button.click()")

        time.sleep(5)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
