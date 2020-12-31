import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationPap(unittest.TestCase):
    def test_send_a_message_from_one_ad(self):
        url_ad = "https://www.pap.fr/annonces/bureaux-paris-16e-r427800161"

        app = Application(backend="uia")

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")
        time.sleep(7)

        # Open the Pap Application
        pywinauto.keyboard.send_keys(url_ad)
        time.sleep(5)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')
        time.sleep(10)

        # Clik on the form
        pywinauto.mouse.click(button='left', coords=(1150, 230))
        time.sleep(3)

        # Go to the "Votre prénom" input
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre nom" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre email" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre téléphone" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("")

        # Go to the "Votre message" input
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.keyboard.send_keys("""
        """)

        # Uncheck the "Je souhaite recevoir les annonces correspondant à ma recherche" checkbox
        time.sleep(3)
        pywinauto.keyboard.send_keys("{VK_TAB}")
        time.sleep(3)
        pywinauto.mouse.click(button='left', coords=(1000, 330))

        # Click on the "Envoyer votre message" button
        time.sleep(3)
        pywinauto.mouse.click(button='left', coords=(1000, 400))

        # Close the brower
        time.sleep(7)
        pywinauto.keyboard.send_keys('%{F4}')


if __name__ == '__main__':
    unittest.main()
