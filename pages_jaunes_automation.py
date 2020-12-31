import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse

app = Application(backend="uia")

#Ouvrir l'application Google Chrome
app.start("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe")

time.sleep(3)

#Write a URL
url = "pages jaunes contact with email"
pywinauto.keyboard.send_keys(url)

time.sleep(2)

#Press the 'Enter' button
pywinauto.keyboard.send_keys('{ENTER}')

time.sleep(3)

#Scroll down Demande d'informations
pywinauto.keyboard.send_keys('{DOWN 10}')

time.sleep(1)

#Move the mouse to the 'Contacter par mail' button
#Click the 'Contacter par mail' button
pywinauto.mouse.click(button='left',coords=(180, 310))

time.sleep(1)

#Move the mouse to the 'Nom' textbox
#Click on the 'Nom' textbox
pywinauto.mouse.click(button='left', coords=(400, 250))

time.sleep(1)

#Write my name in the 'Nom' textbox
myName = "myFirstName{VK_SPACE}myName"
pywinauto.keyboard.send_keys(myName)

time.sleep(1)

#Move the mouse to the 'Email' textbox
#Click on the 'Email' textbox
pywinauto.mouse.click(button='left', coords=(400, 340))

time.sleep(1)

#Write my name in the 'Email' textbox
myEmail = "email"
pywinauto.keyboard.send_keys(myEmail)

time.sleep(1)

#Move the mouse to the 'Objet du message' textbox
#Click on the 'Objet du message' textbox
pywinauto.mouse.click(button='left', coords=(400, 500))

time.sleep(1)

#Write my name in the 'Objet du message' textbox
mySubject = "subject"
pywinauto.keyboard.send_keys(mySubject)

time.sleep(1)

#Move the mouse to the 'Message' textbox
#Click on the 'Objet du message' textbox
pywinauto.mouse.click(button='left', coords=(400, 600))

time.sleep(1)

#Write my name in the 'Message' textbox
myMessage = (
        "Message{ENTER} "
        )
pywinauto.keyboard.send_keys(myMessage)

time.sleep(1)

#Click 10 times on down arrow 
for x in range(10):
    pywinauto.mouse.click(button='left', coords=(1020, 650))

time.sleep(1)
#Click on the 'Recevoir une copie du message' button
pywinauto.mouse.click(button='left', coords=(400, 330))

time.sleep(1)

#Click on the 'Envoyer' button
pywinauto.mouse.click(button='left', coords=(400, 400))

time.sleep(1)

#Close an active window with Alt+F4
pywinauto.keyboard.send_keys('%{F4}')