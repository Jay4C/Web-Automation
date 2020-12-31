import unittest
import time
from pywinauto.application import Application
import pywinauto.keyboard
import pywinauto.mouse
import requests
from bs4 import BeautifulSoup


class UnitTestsDesktopAutomationYellowPagesCanada(unittest.TestCase):
    def test_click_on_button_email_for_one_page_without_ocr_for_distributing_open_source_code_for_garage_in_italy(self):
        url_company = "https://www.paginegialle.it/centro-revisioni-nais-roma"

        html_company = requests.get(url_company)

        soup_company = BeautifulSoup(html_company.content, 'html.parser')

        if soup_company.find("a", {"class": "icn-contattaci"}) is not None:
            print("button Contattaci present")

            app = Application(backend="uia")

            # Ouvrir l'application Microsoft Edge
            app.start("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

            time.sleep(10)

            pywinauto.keyboard.send_keys(url_company + "/contattaci")

            time.sleep(4)

            # Press the 'Enter' button
            pywinauto.keyboard.send_keys('{ENTER}')

            time.sleep(7)

            # Click on the 'NOME' textbox
            pywinauto.mouse.click(button='left', coords=(120, 430))

            time.sleep(4)

            # Write my name in the 'NOME' textbox
            myNome = ""
            pywinauto.keyboard.send_keys(myNome)

            time.sleep(4)

            # Click on the 'COGNOME' textbox
            pywinauto.mouse.click(button='left', coords=(720, 430))

            time.sleep(4)

            # Write my name in the 'COGNOME' textbox
            myCognome = ""
            pywinauto.keyboard.send_keys(myCognome)

            time.sleep(4)

            # Click on the 'E-MAIL' textbox
            pywinauto.mouse.click(button='left', coords=(120, 540))

            time.sleep(4)

            # Write my name in the 'E-MAIL' textbox
            myEmail = ""
            pywinauto.keyboard.send_keys(myEmail)

            time.sleep(4)

            pywinauto.keyboard.send_keys('{VK_TAB 3}')

            time.sleep(4)

            # Write my 'Message' textbox
            myMessage = (
                    "{VK_SPACE}" +
                    "{ENTER}"
            )
            pywinauto.keyboard.send_keys(myMessage)

            time.sleep(4)

            pywinauto.keyboard.send_keys('{VK_TAB 3}')

            time.sleep(4)

            # Click on the 'privacy' button
            pywinauto.mouse.click(button='left', coords=(100, 360))

            time.sleep(4)

            # Click on the 'privacy' button
            pywinauto.mouse.move(coords=(1180, 650))
            # pywinauto.mouse.click(button='left', coords=(1180, 650))

            time.sleep(4)

            # Close an active window with Alt+F4
            pywinauto.keyboard.send_keys('%{F4}')

            # time.sleep(4)
        else:
            print("no button Contattaci")

    def test_click_on_button_email_for_all_pages_without_ocr_for_distributing_open_source_hydrogen_technologies_for_garage_in_italy(self):
        try:
            activites = [
                # {'id': '1', 'url': 'lavoro interinale'},
                # {'id': '2', 'url': 'immobiliari'},
                # {'id': '3', 'url': "centri per l'impiego"},
                # {'id': '4', 'url': 'software'},
                # {'id': '5', 'url': 'hotel'},
                # {'id': '6', 'url': 'locatore'},
                # {'id': '7', 'url': 'pulizia'},
                # {'id': '8', 'url': 'associazione'},
                # {'id': '9', 'url': 'finanziario'},
                # {'id': '10', 'url': 'ristorante'},
                # {'id': '11', 'url': 'costruzione'},
                # {'id': '12', 'url': 'parrucchiere'},
                # {'id': '13', 'url': 'fioraio'},
                # {'id': '14', 'url': 'fabbro ferraio'},
                # {'id': '15', 'url': 'panificio'},
                # {'id': '16', 'url': 'assicurazione'},
                # {'id': '17', 'url': 'farmacia'},
                # {'id': '18', 'url': 'motori'},
                # {'id': '19', 'url': 'elettricità'},
                # {'id': '20', 'url': 'piombatura'},
                # {'id': '21', 'url': 'sicurezza'},
                # {'id': '22', 'url': 'avvocato'},
                # {'id': '23', 'url': 'banca'},
                {'id': '24', 'url': 'garage'},
                # {'id': '25', 'url': 'dentista'},
                # {'id': '26', 'url': 'medico'},
                # {'id': '27', 'url': 'contabilità'},
                # {'id': '28', 'url': 'supermercato'},
                # {'id': '29', 'url': 'notaio'},
                # {'id': '30', 'url': 'gioielliere'},
                # {'id': '31', 'url': 'stilista'},
                # {'id': '32', 'url': 'macellaio'},
                # {'id': '33', 'url': 'libreria'},
                # {'id': '34', 'url': 'architetto'}
            ]

            capitales_du_monde = [
                {'id': '330', 'nom': 'Agrigento'},
                {'id': '331', 'nom': 'Alessandria'},
                {'id': '332', 'nom': 'Ancona'},
                {'id': '333', 'nom': 'Aosta'},
                {'id': '334', 'nom': 'Ascoli Piceno'},
                {'id': '335', "nom": "L'Aquila"},
                {'id': '336', 'nom': 'Arezzo'},
                {'id': '337', 'nom': 'Asti'},
                {'id': '338', 'nom': 'Avellino'},
                {'id': '339', 'nom': 'Bari'},
                {'id': '340', 'nom': 'Bergamo'},
                {'id': '341', 'nom': 'Biella'},
                {'id': '342', 'nom': 'Belluno'},
                {'id': '343', 'nom': 'Benevento'},
                # {'id': '344', 'nom': 'Bologna'},
                # {'id': '345', 'nom': 'Brindisi'},
                # {'id': '346', 'nom': 'Brescia'},
                # {'id': '347', 'nom': 'Trani'},
                # {'id': '348', 'nom': 'Bolzano'},
                # {'id': '349', 'nom': 'Cagliari'},
                # {'id': '350', 'nom': 'Campobasso'},
                # {'id': '351', 'nom': 'Caserta'},
                # {'id': '352', 'nom': 'Chieti'},
                # {'id': '353', 'nom': 'Caltanissetta'},
                # {'id': '354', 'nom': 'Cuneo'},
                # {'id': '355', 'nom': 'Vibo Valentia'},
                # {'id': '356', 'nom': 'Como'},
                # {'id': '357', 'nom': 'Cremona'},
                # {'id': '358', 'nom': 'Cosenza'},
                # {'id': '359', 'nom': 'Catania'},
                # {'id': '360', 'nom': 'Catanzaro'},
                # {'id': '361', 'nom': 'Enna'},
                # {'id': '362', 'nom': 'Forlì'},
                # {'id': '363', 'nom': 'Ferrara'},
                # {'id': '364', 'nom': 'Foggia'},
                # {'id': '365', 'nom': 'Firenze'},
                # {'id': '366', 'nom': 'Fermo'},
                # {'id': '367', 'nom': 'Frosinone'},
                # {'id': '368', 'nom': 'Genoa'},
                # {'id': '369', 'nom': 'Gorizia'},
                # {'id': '370', 'nom': 'Grosseto'},
                # {'id': '371', 'nom': 'Imperia'},
                # {'id': '372', 'nom': 'Isernia'},
                # {'id': '373', 'nom': 'Crotone'},
                # {'id': '374', 'nom': 'Lecco'},
                # {'id': '375', 'nom': 'Lecce'},
                # {'id': '376', 'nom': 'Livorno'},
                # {'id': '377', 'nom': 'Lodi'},
                # {'id': '378', 'nom': 'Latina'},
                # {'id': '379', 'nom': 'Lucca'},
                # {'id': '380', 'nom': 'Monza'},
                # {'id': '381', 'nom': 'Macerata'},
                # {'id': '382', 'nom': 'Messina'},
                # {'id': '383', 'nom': 'Milan'},
                # {'id': '384', 'nom': 'Mantova'},
                # {'id': '385', 'nom': 'Modena'},
                # {'id': '386', 'nom': 'Massa'},
                # {'id': '387', 'nom': 'Matera'},
                # {'id': '388', 'nom': 'Napoli'},
                # {'id': '389', 'nom': 'Novara'},
                # {'id': '390', 'nom': 'Nuoro'},
                # {'id': '391', 'nom': 'Oristano'},
                # {'id': '392', 'nom': 'Palermo'},
                # {'id': '393', 'nom': 'Piacenza'},
                # {'id': '394', 'nom': 'Padova'},
                # {'id': '395', 'nom': 'Pescara'},
                # {'id': '396', 'nom': 'Perugia'},
                # {'id': '397', 'nom': 'Pisa'},
                # {'id': '398', 'nom': 'Pordenone'},
                # {'id': '399', 'nom': 'Prato'},
                # {'id': '400', 'nom': 'Parma'},
                # {'id': '401', 'nom': 'Pistoia'},
                # {'id': '402', 'nom': 'Pesaro'},
                # {'id': '403', 'nom': 'Pavia'},
                # {'id': '404', 'nom': 'Potenza'},
                # {'id': '405', 'nom': 'Ravenna'},
                # {'id': '406', 'nom': 'Reggio Calabria'},
                # {'id': '407', 'nom': 'Reggio Emilia'},
                # {'id': '408', 'nom': 'Ragusa'},
                # {'id': '409', 'nom': 'Rieti'},
                # {'id': '410', 'nom': 'Roma'},
                # {'id': '411', 'nom': 'Rimini'},
                # {'id': '412', 'nom': 'Rovigo'},
                # {'id': '413', 'nom': 'Salerno'},
                # {'id': '414', 'nom': 'Carbonia'},
                # {'id': '415', 'nom': 'Siena'},
                # {'id': '416', 'nom': 'Sondrio'},
                # {'id': '417', 'nom': 'La Spezia'},
                # {'id': '418', 'nom': 'Siracusa'},
                # {'id': '419', 'nom': 'Sassari'},
                # {'id': '420', 'nom': 'Savona'},
                # {'id': '421', 'nom': 'Taranto'},
                # {'id': '422', 'nom': 'Teramo'},
                # {'id': '423', 'nom': 'Trento'},
                # {'id': '424', 'nom': 'Torino'},
                # {'id': '425', 'nom': 'Trapani'},
                # {'id': '426', 'nom': 'Terni'},
                # {'id': '427', 'nom': 'Trieste'},
                # {'id': '428', 'nom': 'Treviso'},
                # {'id': '429', 'nom': 'Udine'},
                # {'id': '430', 'nom': 'Varese'},
                # {'id': '431', 'nom': 'Verbania'},
                # {'id': '432', 'nom': 'Vercelli'},
                # {'id': '433', 'nom': 'Venice'},
                # {'id': '434', 'nom': 'Vicenza'},
                # {'id': '435', 'nom': 'Verona'},
                # {'id': '436', 'nom': 'Viterbo'}
            ]

            for capitale in capitales_du_monde:
                for activite in activites:
                    try:
                        activity = activite.get("url")
                        city = capitale.get("nom")
                        url_search = "https://www.paginegialle.it/ricerca/" + activity + "/" + city
                        html_search = requests.get(url_search)
                        soup_search = BeautifulSoup(html_search.content, 'html.parser')

                        number_of_pages = 0

                        try:
                            if soup_search \
                                    .find("h1", {"class": "searchDetailsTxt"}) \
                                    .find("span", {"class": "searchResNum"}) is not None:

                                number_of_pages_with_coma = int(soup_search
                                                                .find("h1", {"class": "searchDetailsTxt"})
                                                                .find("span", {"class": "searchResNum"})
                                                                .find_all("span")[0]
                                                                .text
                                                                ) / 20

                                if int(str(number_of_pages_with_coma).split(".")[1][:1]) < 5:
                                    number_of_pages += round(number_of_pages_with_coma) + 1
                                    print("number_of_pages : " + str(number_of_pages))

                                elif int(str(number_of_pages_with_coma).split(".")[1][:1]) >= 5:
                                    number_of_pages += round(number_of_pages_with_coma)
                                    print("number_of_pages : " + str(number_of_pages))

                                i_1 = 0

                                for i in range(1, number_of_pages + 1):
                                    try:
                                        url_of_one_page_of_results = "https://www.paginegialle.it/ricerca/" \
                                                                     + activity + "/" \
                                                                     + city \
                                                                     + "/p-" + str(i)

                                        print(url_of_one_page_of_results)

                                        time.sleep(2)

                                        html_of_one_page_of_results = requests.get(url_of_one_page_of_results)

                                        soup_of_one_page_of_results = BeautifulSoup(
                                            html_of_one_page_of_results.content,
                                            'html.parser')

                                        try:
                                            if soup_of_one_page_of_results \
                                                    .find("div", {"class": "pageContentWrapper"}) is not None:
                                                try:
                                                    if soup_of_one_page_of_results \
                                                            .find("div", {"class": "pageContentWrapper"}) \
                                                            .find("section", {"class": "vcard"}) is not None:
                                                        for result_item in soup_of_one_page_of_results \
                                                                .find("div", {"class": "pageContentWrapper"}) \
                                                                .find_all("section", {"class": "vcard"}):
                                                            i_1 += 1

                                                            try:
                                                                if result_item.find("header") \
                                                                        .find("h2", {"itemprop": "name"}) \
                                                                        .find("a") is not None:
                                                                    url_company = result_item.find("header") \
                                                                        .find("h2", {"itemprop": "name"}) \
                                                                        .find("a") \
                                                                        .get("href")

                                                                    print(str(i_1) + " : " + url_company)

                                                                    html_company = requests.get(url_company)

                                                                    soup_company = BeautifulSoup(html_company.content, 'html.parser')

                                                                    if soup_company.find("a", {"class": "icn-contattaci"}) is not None:
                                                                        print("button Contattaci present")

                                                                        app = Application(backend="uia")

                                                                        # Ouvrir l'application Microsoft Edge
                                                                        app.start(
                                                                            "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe")

                                                                        time.sleep(10)

                                                                        pywinauto.keyboard.send_keys(
                                                                            url_company + "/contattaci")

                                                                        time.sleep(4)

                                                                        # Press the 'Enter' button
                                                                        pywinauto.keyboard.send_keys('{ENTER}')

                                                                        time.sleep(7)

                                                                        # Click on the 'NOME' textbox
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(120, 430))

                                                                        time.sleep(4)

                                                                        # Write my name in the 'NOME' textbox
                                                                        myNome = ""
                                                                        pywinauto.keyboard.send_keys(myNome)

                                                                        time.sleep(4)

                                                                        # Click on the 'COGNOME' textbox
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(720, 430))

                                                                        time.sleep(4)

                                                                        # Write my name in the 'COGNOME' textbox
                                                                        myCognome = ""
                                                                        pywinauto.keyboard.send_keys(myCognome)

                                                                        time.sleep(4)

                                                                        # Click on the 'E-MAIL' textbox
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(120, 540))

                                                                        time.sleep(4)

                                                                        # Write my name in the 'E-MAIL' textbox
                                                                        myEmail = ""
                                                                        pywinauto.keyboard.send_keys(myEmail)

                                                                        time.sleep(4)

                                                                        pywinauto.keyboard.send_keys('{VK_TAB 3}')

                                                                        time.sleep(4)

                                                                        # Write my 'Message' textbox
                                                                        myMessage = (
                                                                                "{VK_SPACE}" +
                                                                                "{ENTER}"
                                                                        )
                                                                        pywinauto.keyboard.send_keys(myMessage)

                                                                        time.sleep(4)

                                                                        pywinauto.keyboard.send_keys('{VK_TAB 3}')

                                                                        time.sleep(4)

                                                                        # Click on the 'privacy' button
                                                                        pywinauto.mouse.click(button='left',
                                                                                              coords=(100, 360))

                                                                        time.sleep(4)

                                                                        # Click on the 'privacy' button
                                                                        pywinauto.mouse.move(coords=(1180, 650))
                                                                        # pywinauto.mouse.click(button='left', coords=(1180, 650))

                                                                        time.sleep(4)

                                                                        # Close an active window with Alt+F4
                                                                        pywinauto.keyboard.send_keys('%{F4}')

                                                                        time.sleep(4)
                                                                    else:
                                                                        print("no button Contattaci")
                                                                else:
                                                                    print("no url company")
                                                            except Exception as e:
                                                                print("error header h2 itemprop name : " + str(e))
                                                    else:
                                                        print("no vcard")
                                                except Exception as e:
                                                    print("error div class vcard : " + str(e))
                                            else:
                                                print("sorry there is no results")
                                        except Exception as e:
                                            print("error div class pageContentWrapper : " + str(e))
                                    except Exception as e:
                                        print("error url_of_one_page_of_results : " + str(e))
                            else:
                                print("no pages at all")
                        except Exception as e:
                            print(str(e))
                    except Exception as e:
                        print(str(e))
        finally:
            print('done')


if __name__ == '__main__':
    unittest.main()
