import os
import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse


class UnitTestsDesktopAutomationYouTube(unittest.TestCase):
    def test_list_all_articles_from_one_folder(self):
        path = ""

        dirs = os.listdir(path)

        files = []

        debut_article = ""

        for file in dirs:
            files.append(file)

        #for i in range(0, len(files)):
        for i in range(0, 10):
            print(debut_article + files[i].replace(".avi", "").split("_Article_")[1].replace("_", " "))

    def test_insert_one_video(self):
        app = Application(backend="uia")

        time.sleep(5)

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(10)

        # Open the YouTube application
        pywinauto.keyboard.send_keys("https://www.youtube.com/")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the "Se connecter" button
        pywinauto.mouse.click(button='left', coords=(1250, 90))

        time.sleep(7)

        # Type my Gmail email address
        pywinauto.keyboard.send_keys('')

        time.sleep(7)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Type the password
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys('{VK_TAB 2}')

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(10)

        # Click on the button to create a video or other
        pywinauto.mouse.click(button='left', coords=(1150, 100))

        time.sleep(7)

        # Click on the button to put online a video
        pywinauto.mouse.click(button='left', coords=(1040, 140))

        time.sleep(12)

        # Click on the button to select a file
        pywinauto.mouse.click(button='left', coords=(680, 520))

        time.sleep(7)

        # Select the folder of videos
        pywinauto.mouse.click(button='left', coords=(350, 50))

        time.sleep(7)

        # Type the path of the folder
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(7)

        # Click on the bar of the name of the file
        pywinauto.mouse.click(button='left', coords=(300, 415))

        time.sleep(7)

        # Type the "Return" button in 15 times
        pywinauto.keyboard.send_keys("{VK_RETURN 15}")

        time.sleep(7)

        # Type the filename
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Type the "Tab" button in 2 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(7)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(11)

        # Type the title (mandatory)
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Type the "Tab" button in 3 times
        pywinauto.keyboard.send_keys("{VK_TAB 2}")

        time.sleep(7)

        # Type the description
        pywinauto.keyboard.send_keys("")

        time.sleep(7)

        # Type the "Tab" button in 3 times
        pywinauto.keyboard.send_keys("{VK_TAB 8}")

        time.sleep(7)

        # Click on the "Select" button to select one playlist
        pywinauto.mouse.click(button='left', coords=(380, 440))

        time.sleep(7)

        # Select one playlist
        pywinauto.mouse.click(button='left', coords=(350, 310))

        time.sleep(7)

        # Click on the "Ok" button
        pywinauto.mouse.click(button='left', coords=(540, 655))

        time.sleep(7)

        # Type the "Tab" button in several times
        pywinauto.keyboard.send_keys("{VK_TAB 3}")

        time.sleep(7)

        # Click on the "Non" button
        pywinauto.mouse.click(button='left', coords=(380, 530))

        time.sleep(7)

        # Click on the "Suivant" button of the step 1
        pywinauto.mouse.click(button='left', coords=(1110, 650))

        time.sleep(7)

        # Click on the "Suivant" button of the step 2
        pywinauto.mouse.click(button='left', coords=(1110, 650))

        time.sleep(7)

        # Click on the "Publique" radio button
        pywinauto.mouse.click(button='left', coords=(320, 560))

        time.sleep(7)

        # Click on the "Publier" button
        pywinauto.mouse.click(button='left', coords=(1110, 650))

        time.sleep(7)

        # Click on the "Fermer" button
        pywinauto.mouse.click(button='left', coords=(890, 595))

    def test_insert_several_videos_on_youtube(self):
        app = Application(backend="uia")

        time.sleep(9)

        # Ouvrir l'application Google Chrome
        app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

        time.sleep(9)

        # Open the YouTube application
        pywinauto.keyboard.send_keys("https://www.youtube.com/")

        time.sleep(9)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(9)

        # Click on the "Se connecter" button
        pywinauto.mouse.click(button='left', coords=(1250, 90))

        time.sleep(9)

        # Type my Gmail email address
        pywinauto.keyboard.send_keys('')

        time.sleep(9)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys('{VK_TAB 3}')

        time.sleep(9)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(9)

        # Type the password
        pywinauto.keyboard.send_keys("")

        time.sleep(9)

        # Press the 'Tab' button
        pywinauto.keyboard.send_keys('{VK_TAB 2}')

        time.sleep(9)

        # Press the 'Enter' button
        pywinauto.keyboard.send_keys('{ENTER}')

        time.sleep(9)

        path = ""

        playlist = ""

        # Click on the button to create a video or other
        pywinauto.mouse.click(button='left', coords=(1150, 100))

        time.sleep(9)

        # Click on the button to put online a video
        pywinauto.mouse.click(button='left', coords=(1040, 140))

        time.sleep(9)

        for i in range(7, 8):
            # Click on the button to select a file
            pywinauto.mouse.click(button='left', coords=(680, 520))

            time.sleep(9)

            # Select the folder of videos
            pywinauto.mouse.click(button='left', coords=(350, 50))

            time.sleep(9)

            # Type the path of the folder
            pywinauto.keyboard.send_keys(path)

            time.sleep(9)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(9)

            # Click on the bar of the name of the file
            pywinauto.mouse.click(button='left', coords=(300, 415))

            time.sleep(9)

            # Type the "Return" button in 15 times
            pywinauto.keyboard.send_keys("{VK_RETURN 15}")

            time.sleep(9)

            # Type the filename
            pywinauto.keyboard.send_keys(str(i) + "_")

            time.sleep(9)

            # Type the "{VK_DOWN}" button in 1 time
            pywinauto.keyboard.send_keys("{VK_DOWN}")

            time.sleep(9)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(9)

            # Click on the title
            pywinauto.mouse.click(button='left', coords=(530, 360))

            time.sleep(9)

            # Type the playlist
            pywinauto.keyboard.send_keys(playlist)

            time.sleep(9)

            # Type the "Tab" button in 3 times
            pywinauto.keyboard.send_keys("{VK_TAB 2}")

            time.sleep(9)

            # Type the description
            pywinauto.keyboard.send_keys("")

            time.sleep(9)

            # Type the "Tab" button in several times
            pywinauto.keyboard.send_keys("{VK_TAB 8}")

            time.sleep(9)

            # Click on the "Select" button to select one playlist
            pywinauto.mouse.click(button='left', coords=(380, 440))

            time.sleep(9)

            # Select one playlist
            pywinauto.mouse.click(button='left', coords=(350, 310))

            time.sleep(9)

            # Click on the "Ok" button
            pywinauto.mouse.click(button='left', coords=(540, 655))

            time.sleep(9)

            # Type the "Tab" button in several times
            pywinauto.keyboard.send_keys("{VK_TAB 3}")

            time.sleep(9)

            # Click on the "Non" button
            pywinauto.mouse.click(button='left', coords=(380, 530))

            time.sleep(9)

            # Click on the "Suivant" button of the step 1
            pywinauto.mouse.click(button='left', coords=(1110, 650))

            time.sleep(9)

            # Click on the "Suivant" button of the step 2
            pywinauto.mouse.click(button='left', coords=(1110, 650))

            time.sleep(9)

            # Click on the "Publique" radio button
            pywinauto.mouse.click(button='left', coords=(320, 560))

            time.sleep(9)

            # Click on the "Publier" button
            pywinauto.mouse.click(button='left', coords=(1110, 650))

            time.sleep(9)

            # Click on the "Fermer" button
            pywinauto.mouse.click(button='left', coords=(890, 595))

            time.sleep(9)

            # Click on the button to create a video or other
            pywinauto.mouse.click(button='left', coords=(1240, 100))

            time.sleep(9)

            # Click on the button to put online a video
            pywinauto.mouse.click(button='left', coords=(1180, 140))

            time.sleep(9)

        time.sleep(9)

        # Click on the "Ctrl + r"
        # pywinauto.keyboard.send_keys("^r")

        # time.sleep(9)

        # Click on the "Compte" button
        # pywinauto.mouse.click(button='left', coords=(1330, 100))

        # time.sleep(9)

        # Click on the "Se deconnecter" button
        # pywinauto.mouse.click(button='left', coords=(1180, 340))


if __name__ == '__main__':
    unittest.main()
