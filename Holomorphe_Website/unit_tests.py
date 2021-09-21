import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationHolomorpheWebsite(unittest.TestCase):
    def test_generate_html_to_pdf_twelve_month_operating_budget(self):
        print("test_generate_html_to_pdf_twelve_month_operating_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/twelve_month_operating_budget')
        browser.get('https://holomorphe.com/reporting/twelve_month_operating_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_twelve_month_operating_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_department_budget(self):
        print("test_generate_html_to_pdf_department_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/department_budget')
        browser.get('https://holomorphe.com/reporting/department_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        # fill r25c4
        r25c4 = browser.find_element_by_name("r25c4")
        r25c4.clear()
        r25c4.send_keys("r25c4")

        # fill r25c5
        r25c5 = browser.find_element_by_name("r25c5")
        r25c5.clear()
        r25c5.send_keys("r25c5")

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        # fill r26c4
        r26c4 = browser.find_element_by_name("r26c4")
        r26c4.clear()
        r26c4.send_keys("r26c4")

        # fill r26c5
        r26c5 = browser.find_element_by_name("r26c5")
        r26c5.clear()
        r26c5.send_keys("r26c5")

        # fill r27c1
        r27c1 = browser.find_element_by_name("r27c1")
        r27c1.clear()
        r27c1.send_keys("r27c1")

        # fill r27c2
        r27c2 = browser.find_element_by_name("r27c2")
        r27c2.clear()
        r27c2.send_keys("r27c2")

        # fill r27c3
        r27c3 = browser.find_element_by_name("r27c3")
        r27c3.clear()
        r27c3.send_keys("r27c3")

        # fill r27c4
        r27c4 = browser.find_element_by_name("r27c4")
        r27c4.clear()
        r27c4.send_keys("r27c4")

        # fill r27c5
        r27c5 = browser.find_element_by_name("r27c5")
        r27c5.clear()
        r27c5.send_keys("r27c5")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_department_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_annual_income_budget(self):
        print("test_generate_html_to_pdf_annual_income_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/annual_income_budget')
        browser.get('https://holomorphe.com/reporting/annual_income_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r1c14
        r1c14 = browser.find_element_by_name("r1c14")
        r1c14.clear()
        r1c14.send_keys("r1c14")

        # fill r1c15
        r1c15 = browser.find_element_by_name("r1c15")
        r1c15.clear()
        r1c15.send_keys("r1c15")

        # fill r1c16
        r1c16 = browser.find_element_by_name("r1c16")
        r1c16.clear()
        r1c16.send_keys("r1c16")

        # fill r1c17
        r1c17 = browser.find_element_by_name("r1c17")
        r1c17.clear()
        r1c17.send_keys("r1c17")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r2c14
        r2c14 = browser.find_element_by_name("r2c14")
        r2c14.clear()
        r2c14.send_keys("r2c14")

        # fill r2c15
        r2c15 = browser.find_element_by_name("r2c15")
        r2c15.clear()
        r2c15.send_keys("r2c15")

        # fill r2c16
        r2c16 = browser.find_element_by_name("r2c16")
        r2c16.clear()
        r2c16.send_keys("r2c16")

        # fill r2c17
        r2c17 = browser.find_element_by_name("r2c17")
        r2c17.clear()
        r2c17.send_keys("r2c17")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r3c14
        r3c14 = browser.find_element_by_name("r3c14")
        r3c14.clear()
        r3c14.send_keys("r3c14")

        # fill r3c15
        r3c15 = browser.find_element_by_name("r3c15")
        r3c15.clear()
        r3c15.send_keys("r3c15")

        # fill r3c16
        r3c16 = browser.find_element_by_name("r3c16")
        r3c16.clear()
        r3c16.send_keys("r3c16")

        # fill r3c17
        r3c17 = browser.find_element_by_name("r3c17")
        r3c17.clear()
        r3c17.send_keys("r3c17")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r4c14
        r4c14 = browser.find_element_by_name("r4c14")
        r4c14.clear()
        r4c14.send_keys("r4c14")

        # fill r4c15
        r4c15 = browser.find_element_by_name("r4c15")
        r4c15.clear()
        r4c15.send_keys("r4c15")

        # fill r4c16
        r4c16 = browser.find_element_by_name("r4c16")
        r4c16.clear()
        r4c16.send_keys("r4c16")

        # fill r4c17
        r4c17 = browser.find_element_by_name("r4c17")
        r4c17.clear()
        r4c17.send_keys("r4c17")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r5c14
        r5c14 = browser.find_element_by_name("r5c14")
        r5c14.clear()
        r5c14.send_keys("r5c14")

        # fill r5c15
        r5c15 = browser.find_element_by_name("r5c15")
        r5c15.clear()
        r5c15.send_keys("r5c15")

        # fill r5c16
        r5c16 = browser.find_element_by_name("r5c16")
        r5c16.clear()
        r5c16.send_keys("r5c16")

        # fill r5c17
        r5c17 = browser.find_element_by_name("r5c17")
        r5c17.clear()
        r5c17.send_keys("r5c17")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r6c14
        r6c14 = browser.find_element_by_name("r6c14")
        r6c14.clear()
        r6c14.send_keys("r6c14")

        # fill r6c15
        r6c15 = browser.find_element_by_name("r6c15")
        r6c15.clear()
        r6c15.send_keys("r6c15")

        # fill r6c16
        r6c16 = browser.find_element_by_name("r6c16")
        r6c16.clear()
        r6c16.send_keys("r6c16")

        # fill r6c17
        r6c17 = browser.find_element_by_name("r6c17")
        r6c17.clear()
        r6c17.send_keys("r6c17")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r7c14
        r7c14 = browser.find_element_by_name("r7c14")
        r7c14.clear()
        r7c14.send_keys("r7c14")

        # fill r7c15
        r7c15 = browser.find_element_by_name("r7c15")
        r7c15.clear()
        r7c15.send_keys("r7c15")

        # fill r7c16
        r7c16 = browser.find_element_by_name("r7c16")
        r7c16.clear()
        r7c16.send_keys("r7c16")

        # fill r7c17
        r7c17 = browser.find_element_by_name("r7c17")
        r7c17.clear()
        r7c17.send_keys("r7c17")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r8c14
        r8c14 = browser.find_element_by_name("r8c14")
        r8c14.clear()
        r8c14.send_keys("r8c14")

        # fill r8c15
        r8c15 = browser.find_element_by_name("r8c15")
        r8c15.clear()
        r8c15.send_keys("r8c15")

        # fill r8c16
        r8c16 = browser.find_element_by_name("r8c16")
        r8c16.clear()
        r8c16.send_keys("r8c16")

        # fill r8c17
        r8c17 = browser.find_element_by_name("r8c17")
        r8c17.clear()
        r8c17.send_keys("r8c17")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r9c14
        r9c14 = browser.find_element_by_name("r9c14")
        r9c14.clear()
        r9c14.send_keys("r9c14")

        # fill r9c15
        r9c15 = browser.find_element_by_name("r9c15")
        r9c15.clear()
        r9c15.send_keys("r9c15")

        # fill r9c16
        r9c16 = browser.find_element_by_name("r9c16")
        r9c16.clear()
        r9c16.send_keys("r9c16")

        # fill r9c17
        r9c17 = browser.find_element_by_name("r9c17")
        r9c17.clear()
        r9c17.send_keys("r9c17")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r10c14
        r10c14 = browser.find_element_by_name("r10c14")
        r10c14.clear()
        r10c14.send_keys("r10c14")

        # fill r10c15
        r10c15 = browser.find_element_by_name("r10c15")
        r10c15.clear()
        r10c15.send_keys("r10c15")

        # fill r10c16
        r10c16 = browser.find_element_by_name("r10c16")
        r10c16.clear()
        r10c16.send_keys("r10c16")

        # fill r10c17
        r10c17 = browser.find_element_by_name("r10c17")
        r10c17.clear()
        r10c17.send_keys("r10c17")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r11c14
        r11c14 = browser.find_element_by_name("r11c14")
        r11c14.clear()
        r11c14.send_keys("r11c14")

        # fill r11c15
        r11c15 = browser.find_element_by_name("r11c15")
        r11c15.clear()
        r11c15.send_keys("r11c15")

        # fill r11c16
        r11c16 = browser.find_element_by_name("r11c16")
        r11c16.clear()
        r11c16.send_keys("r11c16")

        # fill r11c17
        r11c17 = browser.find_element_by_name("r11c17")
        r11c17.clear()
        r11c17.send_keys("r11c17")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r12c14
        r12c14 = browser.find_element_by_name("r12c14")
        r12c14.clear()
        r12c14.send_keys("r12c14")

        # fill r12c15
        r12c15 = browser.find_element_by_name("r12c15")
        r12c15.clear()
        r12c15.send_keys("r12c15")

        # fill r12c16
        r12c16 = browser.find_element_by_name("r12c16")
        r12c16.clear()
        r12c16.send_keys("r12c16")

        # fill r12c17
        r12c17 = browser.find_element_by_name("r12c17")
        r12c17.clear()
        r12c17.send_keys("r12c17")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r13c14
        r13c14 = browser.find_element_by_name("r13c14")
        r13c14.clear()
        r13c14.send_keys("r13c14")

        # fill r13c15
        r13c15 = browser.find_element_by_name("r13c15")
        r13c15.clear()
        r13c15.send_keys("r13c15")

        # fill r13c16
        r13c16 = browser.find_element_by_name("r13c16")
        r13c16.clear()
        r13c16.send_keys("r13c16")

        # fill r13c17
        r13c17 = browser.find_element_by_name("r13c17")
        r13c17.clear()
        r13c17.send_keys("r13c17")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r14c14
        r14c14 = browser.find_element_by_name("r14c14")
        r14c14.clear()
        r14c14.send_keys("r14c14")

        # fill r14c15
        r14c15 = browser.find_element_by_name("r14c15")
        r14c15.clear()
        r14c15.send_keys("r14c15")

        # fill r14c16
        r14c16 = browser.find_element_by_name("r14c16")
        r14c16.clear()
        r14c16.send_keys("r14c16")

        # fill r14c17
        r14c17 = browser.find_element_by_name("r14c17")
        r14c17.clear()
        r14c17.send_keys("r14c17")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r15c14
        r15c14 = browser.find_element_by_name("r15c14")
        r15c14.clear()
        r15c14.send_keys("r15c14")

        # fill r15c15
        r15c15 = browser.find_element_by_name("r15c15")
        r15c15.clear()
        r15c15.send_keys("r15c15")

        # fill r15c16
        r15c16 = browser.find_element_by_name("r15c16")
        r15c16.clear()
        r15c16.send_keys("r15c16")

        # fill r15c17
        r15c17 = browser.find_element_by_name("r15c17")
        r15c17.clear()
        r15c17.send_keys("r15c17")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # fill r16c14
        r16c14 = browser.find_element_by_name("r16c14")
        r16c14.clear()
        r16c14.send_keys("r16c14")

        # fill r16c15
        r16c15 = browser.find_element_by_name("r16c15")
        r16c15.clear()
        r16c15.send_keys("r16c15")

        # fill r16c16
        r16c16 = browser.find_element_by_name("r16c16")
        r16c16.clear()
        r16c16.send_keys("r16c16")

        # fill r16c17
        r16c17 = browser.find_element_by_name("r16c17")
        r16c17.clear()
        r16c17.send_keys("r16c17")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r17c10
        r17c10 = browser.find_element_by_name("r17c10")
        r17c10.clear()
        r17c10.send_keys("r17c10")

        # fill r17c11
        r17c11 = browser.find_element_by_name("r17c11")
        r17c11.clear()
        r17c11.send_keys("r17c11")

        # fill r17c12
        r17c12 = browser.find_element_by_name("r17c12")
        r17c12.clear()
        r17c12.send_keys("r17c12")

        # fill r17c13
        r17c13 = browser.find_element_by_name("r17c13")
        r17c13.clear()
        r17c13.send_keys("r17c13")

        # fill r17c14
        r17c14 = browser.find_element_by_name("r17c14")
        r17c14.clear()
        r17c14.send_keys("r17c14")

        # fill r17c15
        r17c15 = browser.find_element_by_name("r17c15")
        r17c15.clear()
        r17c15.send_keys("r17c15")

        # fill r17c16
        r17c16 = browser.find_element_by_name("r17c16")
        r17c16.clear()
        r17c16.send_keys("r17c16")

        # fill r17c17
        r17c17 = browser.find_element_by_name("r17c17")
        r17c17.clear()
        r17c17.send_keys("r17c17")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r18c10
        r18c10 = browser.find_element_by_name("r18c10")
        r18c10.clear()
        r18c10.send_keys("r18c10")

        # fill r18c11
        r18c11 = browser.find_element_by_name("r18c11")
        r18c11.clear()
        r18c11.send_keys("r18c11")

        # fill r18c12
        r18c12 = browser.find_element_by_name("r18c12")
        r18c12.clear()
        r18c12.send_keys("r18c12")

        # fill r18c13
        r18c13 = browser.find_element_by_name("r18c13")
        r18c13.clear()
        r18c13.send_keys("r18c13")

        # fill r18c14
        r18c14 = browser.find_element_by_name("r18c14")
        r18c14.clear()
        r18c14.send_keys("r18c14")

        # fill r18c15
        r18c15 = browser.find_element_by_name("r18c15")
        r18c15.clear()
        r18c15.send_keys("r18c15")

        # fill r18c16
        r18c16 = browser.find_element_by_name("r18c16")
        r18c16.clear()
        r18c16.send_keys("r18c16")

        # fill r18c17
        r18c17 = browser.find_element_by_name("r18c17")
        r18c17.clear()
        r18c17.send_keys("r18c17")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        # fill r19c9
        r19c9 = browser.find_element_by_name("r19c9")
        r19c9.clear()
        r19c9.send_keys("r19c9")

        # fill r19c10
        r19c10 = browser.find_element_by_name("r19c10")
        r19c10.clear()
        r19c10.send_keys("r19c10")

        # fill r19c11
        r19c11 = browser.find_element_by_name("r19c11")
        r19c11.clear()
        r19c11.send_keys("r19c11")

        # fill r19c12
        r19c12 = browser.find_element_by_name("r19c12")
        r19c12.clear()
        r19c12.send_keys("r19c12")

        # fill r19c13
        r19c13 = browser.find_element_by_name("r19c13")
        r19c13.clear()
        r19c13.send_keys("r19c13")

        # fill r19c14
        r19c14 = browser.find_element_by_name("r19c14")
        r19c14.clear()
        r19c14.send_keys("r19c14")

        # fill r19c15
        r19c15 = browser.find_element_by_name("r19c15")
        r19c15.clear()
        r19c15.send_keys("r19c15")

        # fill r19c16
        r19c16 = browser.find_element_by_name("r19c16")
        r19c16.clear()
        r19c16.send_keys("r19c16")

        # fill r19c17
        r19c17 = browser.find_element_by_name("r19c17")
        r19c17.clear()
        r19c17.send_keys("r19c17")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        # fill r20c9
        r20c9 = browser.find_element_by_name("r20c9")
        r20c9.clear()
        r20c9.send_keys("r20c9")

        # fill r20c10
        r20c10 = browser.find_element_by_name("r20c10")
        r20c10.clear()
        r20c10.send_keys("r20c10")

        # fill r20c11
        r20c11 = browser.find_element_by_name("r20c11")
        r20c11.clear()
        r20c11.send_keys("r20c11")

        # fill r20c12
        r20c12 = browser.find_element_by_name("r20c12")
        r20c12.clear()
        r20c12.send_keys("r20c12")

        # fill r20c13
        r20c13 = browser.find_element_by_name("r20c13")
        r20c13.clear()
        r20c13.send_keys("r20c13")

        # fill r20c14
        r20c14 = browser.find_element_by_name("r20c14")
        r20c14.clear()
        r20c14.send_keys("r20c14")

        # fill r20c15
        r20c15 = browser.find_element_by_name("r20c15")
        r20c15.clear()
        r20c15.send_keys("r20c15")

        # fill r20c16
        r20c16 = browser.find_element_by_name("r20c16")
        r20c16.clear()
        r20c16.send_keys("r20c16")

        # fill r20c17
        r20c17 = browser.find_element_by_name("r20c17")
        r20c17.clear()
        r20c17.send_keys("r20c17")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        # fill r21c9
        r21c9 = browser.find_element_by_name("r21c9")
        r21c9.clear()
        r21c9.send_keys("r21c9")

        # fill r21c10
        r21c10 = browser.find_element_by_name("r21c10")
        r21c10.clear()
        r21c10.send_keys("r21c10")

        # fill r21c11
        r21c11 = browser.find_element_by_name("r21c11")
        r21c11.clear()
        r21c11.send_keys("r21c11")

        # fill r21c12
        r21c12 = browser.find_element_by_name("r21c12")
        r21c12.clear()
        r21c12.send_keys("r21c12")

        # fill r21c13
        r21c13 = browser.find_element_by_name("r21c13")
        r21c13.clear()
        r21c13.send_keys("r21c13")

        # fill r21c14
        r21c14 = browser.find_element_by_name("r21c14")
        r21c14.clear()
        r21c14.send_keys("r21c14")

        # fill r21c15
        r21c15 = browser.find_element_by_name("r21c15")
        r21c15.clear()
        r21c15.send_keys("r21c15")

        # fill r21c16
        r21c16 = browser.find_element_by_name("r21c16")
        r21c16.clear()
        r21c16.send_keys("r21c16")

        # fill r21c17
        r21c17 = browser.find_element_by_name("r21c17")
        r21c17.clear()
        r21c17.send_keys("r21c17")

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        # fill r22c6
        r22c6 = browser.find_element_by_name("r22c6")
        r22c6.clear()
        r22c6.send_keys("r22c6")

        # fill r22c7
        r22c7 = browser.find_element_by_name("r22c7")
        r22c7.clear()
        r22c7.send_keys("r22c7")

        # fill r22c8
        r22c8 = browser.find_element_by_name("r22c8")
        r22c8.clear()
        r22c8.send_keys("r22c8")

        # fill r22c9
        r22c9 = browser.find_element_by_name("r22c9")
        r22c9.clear()
        r22c9.send_keys("r22c9")

        # fill r22c10
        r22c10 = browser.find_element_by_name("r22c10")
        r22c10.clear()
        r22c10.send_keys("r22c10")

        # fill r22c11
        r22c11 = browser.find_element_by_name("r22c11")
        r22c11.clear()
        r22c11.send_keys("r22c11")

        # fill r22c12
        r22c12 = browser.find_element_by_name("r22c12")
        r22c12.clear()
        r22c12.send_keys("r22c12")

        # fill r22c13
        r22c13 = browser.find_element_by_name("r22c13")
        r22c13.clear()
        r22c13.send_keys("r22c13")

        # fill r22c14
        r22c14 = browser.find_element_by_name("r22c14")
        r22c14.clear()
        r22c14.send_keys("r22c14")

        # fill r22c15
        r22c15 = browser.find_element_by_name("r22c15")
        r22c15.clear()
        r22c15.send_keys("r22c15")

        # fill r22c16
        r22c16 = browser.find_element_by_name("r22c16")
        r22c16.clear()
        r22c16.send_keys("r22c16")

        # fill r22c17
        r22c17 = browser.find_element_by_name("r22c17")
        r22c17.clear()
        r22c17.send_keys("r22c17")

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        # fill r23c6
        r23c6 = browser.find_element_by_name("r23c6")
        r23c6.clear()
        r23c6.send_keys("r23c6")

        # fill r23c7
        r23c7 = browser.find_element_by_name("r23c7")
        r23c7.clear()
        r23c7.send_keys("r23c7")

        # fill r23c8
        r23c8 = browser.find_element_by_name("r23c8")
        r23c8.clear()
        r23c8.send_keys("r23c8")

        # fill r23c9
        r23c9 = browser.find_element_by_name("r23c9")
        r23c9.clear()
        r23c9.send_keys("r23c9")

        # fill r23c10
        r23c10 = browser.find_element_by_name("r23c10")
        r23c10.clear()
        r23c10.send_keys("r23c10")

        # fill r23c11
        r23c11 = browser.find_element_by_name("r23c11")
        r23c11.clear()
        r23c11.send_keys("r23c11")

        # fill r23c12
        r23c12 = browser.find_element_by_name("r23c12")
        r23c12.clear()
        r23c12.send_keys("r23c12")

        # fill r23c13
        r23c13 = browser.find_element_by_name("r23c13")
        r23c13.clear()
        r23c13.send_keys("r23c13")

        # fill r23c14
        r23c14 = browser.find_element_by_name("r23c14")
        r23c14.clear()
        r23c14.send_keys("r23c14")

        # fill r23c15
        r23c15 = browser.find_element_by_name("r23c15")
        r23c15.clear()
        r23c15.send_keys("r23c15")

        # fill r23c16
        r23c16 = browser.find_element_by_name("r23c16")
        r23c16.clear()
        r23c16.send_keys("r23c16")

        # fill r23c17
        r23c17 = browser.find_element_by_name("r23c17")
        r23c17.clear()
        r23c17.send_keys("r23c17")

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        # fill r24c6
        r24c6 = browser.find_element_by_name("r24c6")
        r24c6.clear()
        r24c6.send_keys("r24c6")

        # fill r24c7
        r24c7 = browser.find_element_by_name("r24c7")
        r24c7.clear()
        r24c7.send_keys("r24c7")

        # fill r24c8
        r24c8 = browser.find_element_by_name("r24c8")
        r24c8.clear()
        r24c8.send_keys("r24c8")

        # fill r24c9
        r24c9 = browser.find_element_by_name("r24c9")
        r24c9.clear()
        r24c9.send_keys("r24c9")

        # fill r24c10
        r24c10 = browser.find_element_by_name("r24c10")
        r24c10.clear()
        r24c10.send_keys("r24c10")

        # fill r24c11
        r24c11 = browser.find_element_by_name("r24c11")
        r24c11.clear()
        r24c11.send_keys("r24c11")

        # fill r24c12
        r24c12 = browser.find_element_by_name("r24c12")
        r24c12.clear()
        r24c12.send_keys("r24c12")

        # fill r24c13
        r24c13 = browser.find_element_by_name("r24c13")
        r24c13.clear()
        r24c13.send_keys("r24c13")

        # fill r24c14
        r24c14 = browser.find_element_by_name("r24c14")
        r24c14.clear()
        r24c14.send_keys("r24c14")

        # fill r24c15
        r24c15 = browser.find_element_by_name("r24c15")
        r24c15.clear()
        r24c15.send_keys("r24c15")

        # fill r24c16
        r24c16 = browser.find_element_by_name("r24c16")
        r24c16.clear()
        r24c16.send_keys("r24c16")

        # fill r24c17
        r24c17 = browser.find_element_by_name("r24c17")
        r24c17.clear()
        r24c17.send_keys("r24c17")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_annual_income_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_annual_expense_budget(self):
        print("test_generate_html_to_pdf_annual_expense_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/annual_expense_budget')
        browser.get('https://holomorphe.com/reporting/annual_expense_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r1c14
        r1c14 = browser.find_element_by_name("r1c14")
        r1c14.clear()
        r1c14.send_keys("r1c14")

        # fill r1c15
        r1c15 = browser.find_element_by_name("r1c15")
        r1c15.clear()
        r1c15.send_keys("r1c15")

        # fill r1c16
        r1c16 = browser.find_element_by_name("r1c16")
        r1c16.clear()
        r1c16.send_keys("r1c16")

        # fill r1c17
        r1c17 = browser.find_element_by_name("r1c17")
        r1c17.clear()
        r1c17.send_keys("r1c17")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r2c14
        r2c14 = browser.find_element_by_name("r2c14")
        r2c14.clear()
        r2c14.send_keys("r2c14")

        # fill r2c15
        r2c15 = browser.find_element_by_name("r2c15")
        r2c15.clear()
        r2c15.send_keys("r2c15")

        # fill r2c16
        r2c16 = browser.find_element_by_name("r2c16")
        r2c16.clear()
        r2c16.send_keys("r2c16")

        # fill r2c17
        r2c17 = browser.find_element_by_name("r2c17")
        r2c17.clear()
        r2c17.send_keys("r2c17")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r3c14
        r3c14 = browser.find_element_by_name("r3c14")
        r3c14.clear()
        r3c14.send_keys("r3c14")

        # fill r3c15
        r3c15 = browser.find_element_by_name("r3c15")
        r3c15.clear()
        r3c15.send_keys("r3c15")

        # fill r3c16
        r3c16 = browser.find_element_by_name("r3c16")
        r3c16.clear()
        r3c16.send_keys("r3c16")

        # fill r3c17
        r3c17 = browser.find_element_by_name("r3c17")
        r3c17.clear()
        r3c17.send_keys("r3c17")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r4c14
        r4c14 = browser.find_element_by_name("r4c14")
        r4c14.clear()
        r4c14.send_keys("r4c14")

        # fill r4c15
        r4c15 = browser.find_element_by_name("r4c15")
        r4c15.clear()
        r4c15.send_keys("r4c15")

        # fill r4c16
        r4c16 = browser.find_element_by_name("r4c16")
        r4c16.clear()
        r4c16.send_keys("r4c16")

        # fill r4c17
        r4c17 = browser.find_element_by_name("r4c17")
        r4c17.clear()
        r4c17.send_keys("r4c17")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r5c14
        r5c14 = browser.find_element_by_name("r5c14")
        r5c14.clear()
        r5c14.send_keys("r5c14")

        # fill r5c15
        r5c15 = browser.find_element_by_name("r5c15")
        r5c15.clear()
        r5c15.send_keys("r5c15")

        # fill r5c16
        r5c16 = browser.find_element_by_name("r5c16")
        r5c16.clear()
        r5c16.send_keys("r5c16")

        # fill r5c17
        r5c17 = browser.find_element_by_name("r5c17")
        r5c17.clear()
        r5c17.send_keys("r5c17")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r6c14
        r6c14 = browser.find_element_by_name("r6c14")
        r6c14.clear()
        r6c14.send_keys("r6c14")

        # fill r6c15
        r6c15 = browser.find_element_by_name("r6c15")
        r6c15.clear()
        r6c15.send_keys("r6c15")

        # fill r6c16
        r6c16 = browser.find_element_by_name("r6c16")
        r6c16.clear()
        r6c16.send_keys("r6c16")

        # fill r6c17
        r6c17 = browser.find_element_by_name("r6c17")
        r6c17.clear()
        r6c17.send_keys("r6c17")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r7c14
        r7c14 = browser.find_element_by_name("r7c14")
        r7c14.clear()
        r7c14.send_keys("r7c14")

        # fill r7c15
        r7c15 = browser.find_element_by_name("r7c15")
        r7c15.clear()
        r7c15.send_keys("r7c15")

        # fill r7c16
        r7c16 = browser.find_element_by_name("r7c16")
        r7c16.clear()
        r7c16.send_keys("r7c16")

        # fill r7c17
        r7c17 = browser.find_element_by_name("r7c17")
        r7c17.clear()
        r7c17.send_keys("r7c17")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r8c14
        r8c14 = browser.find_element_by_name("r8c14")
        r8c14.clear()
        r8c14.send_keys("r8c14")

        # fill r8c15
        r8c15 = browser.find_element_by_name("r8c15")
        r8c15.clear()
        r8c15.send_keys("r8c15")

        # fill r8c16
        r8c16 = browser.find_element_by_name("r8c16")
        r8c16.clear()
        r8c16.send_keys("r8c16")

        # fill r8c17
        r8c17 = browser.find_element_by_name("r8c17")
        r8c17.clear()
        r8c17.send_keys("r8c17")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r9c14
        r9c14 = browser.find_element_by_name("r9c14")
        r9c14.clear()
        r9c14.send_keys("r9c14")

        # fill r9c15
        r9c15 = browser.find_element_by_name("r9c15")
        r9c15.clear()
        r9c15.send_keys("r9c15")

        # fill r9c16
        r9c16 = browser.find_element_by_name("r9c16")
        r9c16.clear()
        r9c16.send_keys("r9c16")

        # fill r9c17
        r9c17 = browser.find_element_by_name("r9c17")
        r9c17.clear()
        r9c17.send_keys("r9c17")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r10c14
        r10c14 = browser.find_element_by_name("r10c14")
        r10c14.clear()
        r10c14.send_keys("r10c14")

        # fill r10c15
        r10c15 = browser.find_element_by_name("r10c15")
        r10c15.clear()
        r10c15.send_keys("r10c15")

        # fill r10c16
        r10c16 = browser.find_element_by_name("r10c16")
        r10c16.clear()
        r10c16.send_keys("r10c16")

        # fill r10c17
        r10c17 = browser.find_element_by_name("r10c17")
        r10c17.clear()
        r10c17.send_keys("r10c17")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r11c14
        r11c14 = browser.find_element_by_name("r11c14")
        r11c14.clear()
        r11c14.send_keys("r11c14")

        # fill r11c15
        r11c15 = browser.find_element_by_name("r11c15")
        r11c15.clear()
        r11c15.send_keys("r11c15")

        # fill r11c16
        r11c16 = browser.find_element_by_name("r11c16")
        r11c16.clear()
        r11c16.send_keys("r11c16")

        # fill r11c17
        r11c17 = browser.find_element_by_name("r11c17")
        r11c17.clear()
        r11c17.send_keys("r11c17")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r12c14
        r12c14 = browser.find_element_by_name("r12c14")
        r12c14.clear()
        r12c14.send_keys("r12c14")

        # fill r12c15
        r12c15 = browser.find_element_by_name("r12c15")
        r12c15.clear()
        r12c15.send_keys("r12c15")

        # fill r12c16
        r12c16 = browser.find_element_by_name("r12c16")
        r12c16.clear()
        r12c16.send_keys("r12c16")

        # fill r12c17
        r12c17 = browser.find_element_by_name("r12c17")
        r12c17.clear()
        r12c17.send_keys("r12c17")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r13c14
        r13c14 = browser.find_element_by_name("r13c14")
        r13c14.clear()
        r13c14.send_keys("r13c14")

        # fill r13c15
        r13c15 = browser.find_element_by_name("r13c15")
        r13c15.clear()
        r13c15.send_keys("r13c15")

        # fill r13c16
        r13c16 = browser.find_element_by_name("r13c16")
        r13c16.clear()
        r13c16.send_keys("r13c16")

        # fill r13c17
        r13c17 = browser.find_element_by_name("r13c17")
        r13c17.clear()
        r13c17.send_keys("r13c17")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r14c14
        r14c14 = browser.find_element_by_name("r14c14")
        r14c14.clear()
        r14c14.send_keys("r14c14")

        # fill r14c15
        r14c15 = browser.find_element_by_name("r14c15")
        r14c15.clear()
        r14c15.send_keys("r14c15")

        # fill r14c16
        r14c16 = browser.find_element_by_name("r14c16")
        r14c16.clear()
        r14c16.send_keys("r14c16")

        # fill r14c17
        r14c17 = browser.find_element_by_name("r14c17")
        r14c17.clear()
        r14c17.send_keys("r14c17")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r15c14
        r15c14 = browser.find_element_by_name("r15c14")
        r15c14.clear()
        r15c14.send_keys("r15c14")

        # fill r15c15
        r15c15 = browser.find_element_by_name("r15c15")
        r15c15.clear()
        r15c15.send_keys("r15c15")

        # fill r15c16
        r15c16 = browser.find_element_by_name("r15c16")
        r15c16.clear()
        r15c16.send_keys("r15c16")

        # fill r15c17
        r15c17 = browser.find_element_by_name("r15c17")
        r15c17.clear()
        r15c17.send_keys("r15c17")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # fill r16c14
        r16c14 = browser.find_element_by_name("r16c14")
        r16c14.clear()
        r16c14.send_keys("r16c14")

        # fill r16c15
        r16c15 = browser.find_element_by_name("r16c15")
        r16c15.clear()
        r16c15.send_keys("r16c15")

        # fill r16c16
        r16c16 = browser.find_element_by_name("r16c16")
        r16c16.clear()
        r16c16.send_keys("r16c16")

        # fill r16c17
        r16c17 = browser.find_element_by_name("r16c17")
        r16c17.clear()
        r16c17.send_keys("r16c17")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r17c10
        r17c10 = browser.find_element_by_name("r17c10")
        r17c10.clear()
        r17c10.send_keys("r17c10")

        # fill r17c11
        r17c11 = browser.find_element_by_name("r17c11")
        r17c11.clear()
        r17c11.send_keys("r17c11")

        # fill r17c12
        r17c12 = browser.find_element_by_name("r17c12")
        r17c12.clear()
        r17c12.send_keys("r17c12")

        # fill r17c13
        r17c13 = browser.find_element_by_name("r17c13")
        r17c13.clear()
        r17c13.send_keys("r17c13")

        # fill r17c14
        r17c14 = browser.find_element_by_name("r17c14")
        r17c14.clear()
        r17c14.send_keys("r17c14")

        # fill r17c15
        r17c15 = browser.find_element_by_name("r17c15")
        r17c15.clear()
        r17c15.send_keys("r17c15")

        # fill r17c16
        r17c16 = browser.find_element_by_name("r17c16")
        r17c16.clear()
        r17c16.send_keys("r17c16")

        # fill r17c17
        r17c17 = browser.find_element_by_name("r17c17")
        r17c17.clear()
        r17c17.send_keys("r17c17")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r18c10
        r18c10 = browser.find_element_by_name("r18c10")
        r18c10.clear()
        r18c10.send_keys("r18c10")

        # fill r18c11
        r18c11 = browser.find_element_by_name("r18c11")
        r18c11.clear()
        r18c11.send_keys("r18c11")

        # fill r18c12
        r18c12 = browser.find_element_by_name("r18c12")
        r18c12.clear()
        r18c12.send_keys("r18c12")

        # fill r18c13
        r18c13 = browser.find_element_by_name("r18c13")
        r18c13.clear()
        r18c13.send_keys("r18c13")

        # fill r18c14
        r18c14 = browser.find_element_by_name("r18c14")
        r18c14.clear()
        r18c14.send_keys("r18c14")

        # fill r18c15
        r18c15 = browser.find_element_by_name("r18c15")
        r18c15.clear()
        r18c15.send_keys("r18c15")

        # fill r18c16
        r18c16 = browser.find_element_by_name("r18c16")
        r18c16.clear()
        r18c16.send_keys("r18c16")

        # fill r18c17
        r18c17 = browser.find_element_by_name("r18c17")
        r18c17.clear()
        r18c17.send_keys("r18c17")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        # fill r19c9
        r19c9 = browser.find_element_by_name("r19c9")
        r19c9.clear()
        r19c9.send_keys("r19c9")

        # fill r19c10
        r19c10 = browser.find_element_by_name("r19c10")
        r19c10.clear()
        r19c10.send_keys("r19c10")

        # fill r19c11
        r19c11 = browser.find_element_by_name("r19c11")
        r19c11.clear()
        r19c11.send_keys("r19c11")

        # fill r19c12
        r19c12 = browser.find_element_by_name("r19c12")
        r19c12.clear()
        r19c12.send_keys("r19c12")

        # fill r19c13
        r19c13 = browser.find_element_by_name("r19c13")
        r19c13.clear()
        r19c13.send_keys("r19c13")

        # fill r19c14
        r19c14 = browser.find_element_by_name("r19c14")
        r19c14.clear()
        r19c14.send_keys("r19c14")

        # fill r19c15
        r19c15 = browser.find_element_by_name("r19c15")
        r19c15.clear()
        r19c15.send_keys("r19c15")

        # fill r19c16
        r19c16 = browser.find_element_by_name("r19c16")
        r19c16.clear()
        r19c16.send_keys("r19c16")

        # fill r19c17
        r19c17 = browser.find_element_by_name("r19c17")
        r19c17.clear()
        r19c17.send_keys("r19c17")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        # fill r20c9
        r20c9 = browser.find_element_by_name("r20c9")
        r20c9.clear()
        r20c9.send_keys("r20c9")

        # fill r20c10
        r20c10 = browser.find_element_by_name("r20c10")
        r20c10.clear()
        r20c10.send_keys("r20c10")

        # fill r20c11
        r20c11 = browser.find_element_by_name("r20c11")
        r20c11.clear()
        r20c11.send_keys("r20c11")

        # fill r20c12
        r20c12 = browser.find_element_by_name("r20c12")
        r20c12.clear()
        r20c12.send_keys("r20c12")

        # fill r20c13
        r20c13 = browser.find_element_by_name("r20c13")
        r20c13.clear()
        r20c13.send_keys("r20c13")

        # fill r20c14
        r20c14 = browser.find_element_by_name("r20c14")
        r20c14.clear()
        r20c14.send_keys("r20c14")

        # fill r20c15
        r20c15 = browser.find_element_by_name("r20c15")
        r20c15.clear()
        r20c15.send_keys("r20c15")

        # fill r20c16
        r20c16 = browser.find_element_by_name("r20c16")
        r20c16.clear()
        r20c16.send_keys("r20c16")

        # fill r20c17
        r20c17 = browser.find_element_by_name("r20c17")
        r20c17.clear()
        r20c17.send_keys("r20c17")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        # fill r21c9
        r21c9 = browser.find_element_by_name("r21c9")
        r21c9.clear()
        r21c9.send_keys("r21c9")

        # fill r21c10
        r21c10 = browser.find_element_by_name("r21c10")
        r21c10.clear()
        r21c10.send_keys("r21c10")

        # fill r21c11
        r21c11 = browser.find_element_by_name("r21c11")
        r21c11.clear()
        r21c11.send_keys("r21c11")

        # fill r21c12
        r21c12 = browser.find_element_by_name("r21c12")
        r21c12.clear()
        r21c12.send_keys("r21c12")

        # fill r21c13
        r21c13 = browser.find_element_by_name("r21c13")
        r21c13.clear()
        r21c13.send_keys("r21c13")

        # fill r21c14
        r21c14 = browser.find_element_by_name("r21c14")
        r21c14.clear()
        r21c14.send_keys("r21c14")

        # fill r21c15
        r21c15 = browser.find_element_by_name("r21c15")
        r21c15.clear()
        r21c15.send_keys("r21c15")

        # fill r21c16
        r21c16 = browser.find_element_by_name("r21c16")
        r21c16.clear()
        r21c16.send_keys("r21c16")

        # fill r21c17
        r21c17 = browser.find_element_by_name("r21c17")
        r21c17.clear()
        r21c17.send_keys("r21c17")

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        # fill r22c6
        r22c6 = browser.find_element_by_name("r22c6")
        r22c6.clear()
        r22c6.send_keys("r22c6")

        # fill r22c7
        r22c7 = browser.find_element_by_name("r22c7")
        r22c7.clear()
        r22c7.send_keys("r22c7")

        # fill r22c8
        r22c8 = browser.find_element_by_name("r22c8")
        r22c8.clear()
        r22c8.send_keys("r22c8")

        # fill r22c9
        r22c9 = browser.find_element_by_name("r22c9")
        r22c9.clear()
        r22c9.send_keys("r22c9")

        # fill r22c10
        r22c10 = browser.find_element_by_name("r22c10")
        r22c10.clear()
        r22c10.send_keys("r22c10")

        # fill r22c11
        r22c11 = browser.find_element_by_name("r22c11")
        r22c11.clear()
        r22c11.send_keys("r22c11")

        # fill r22c12
        r22c12 = browser.find_element_by_name("r22c12")
        r22c12.clear()
        r22c12.send_keys("r22c12")

        # fill r22c13
        r22c13 = browser.find_element_by_name("r22c13")
        r22c13.clear()
        r22c13.send_keys("r22c13")

        # fill r22c14
        r22c14 = browser.find_element_by_name("r22c14")
        r22c14.clear()
        r22c14.send_keys("r22c14")

        # fill r22c15
        r22c15 = browser.find_element_by_name("r22c15")
        r22c15.clear()
        r22c15.send_keys("r22c15")

        # fill r22c16
        r22c16 = browser.find_element_by_name("r22c16")
        r22c16.clear()
        r22c16.send_keys("r22c16")

        # fill r22c17
        r22c17 = browser.find_element_by_name("r22c17")
        r22c17.clear()
        r22c17.send_keys("r22c17")

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        # fill r23c6
        r23c6 = browser.find_element_by_name("r23c6")
        r23c6.clear()
        r23c6.send_keys("r23c6")

        # fill r23c7
        r23c7 = browser.find_element_by_name("r23c7")
        r23c7.clear()
        r23c7.send_keys("r23c7")

        # fill r23c8
        r23c8 = browser.find_element_by_name("r23c8")
        r23c8.clear()
        r23c8.send_keys("r23c8")

        # fill r23c9
        r23c9 = browser.find_element_by_name("r23c9")
        r23c9.clear()
        r23c9.send_keys("r23c9")

        # fill r23c10
        r23c10 = browser.find_element_by_name("r23c10")
        r23c10.clear()
        r23c10.send_keys("r23c10")

        # fill r23c11
        r23c11 = browser.find_element_by_name("r23c11")
        r23c11.clear()
        r23c11.send_keys("r23c11")

        # fill r23c12
        r23c12 = browser.find_element_by_name("r23c12")
        r23c12.clear()
        r23c12.send_keys("r23c12")

        # fill r23c13
        r23c13 = browser.find_element_by_name("r23c13")
        r23c13.clear()
        r23c13.send_keys("r23c13")

        # fill r23c14
        r23c14 = browser.find_element_by_name("r23c14")
        r23c14.clear()
        r23c14.send_keys("r23c14")

        # fill r23c15
        r23c15 = browser.find_element_by_name("r23c15")
        r23c15.clear()
        r23c15.send_keys("r23c15")

        # fill r23c16
        r23c16 = browser.find_element_by_name("r23c16")
        r23c16.clear()
        r23c16.send_keys("r23c16")

        # fill r23c17
        r23c17 = browser.find_element_by_name("r23c17")
        r23c17.clear()
        r23c17.send_keys("r23c17")

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        # fill r24c6
        r24c6 = browser.find_element_by_name("r24c6")
        r24c6.clear()
        r24c6.send_keys("r24c6")

        # fill r24c7
        r24c7 = browser.find_element_by_name("r24c7")
        r24c7.clear()
        r24c7.send_keys("r24c7")

        # fill r24c8
        r24c8 = browser.find_element_by_name("r24c8")
        r24c8.clear()
        r24c8.send_keys("r24c8")

        # fill r24c9
        r24c9 = browser.find_element_by_name("r24c9")
        r24c9.clear()
        r24c9.send_keys("r24c9")

        # fill r24c10
        r24c10 = browser.find_element_by_name("r24c10")
        r24c10.clear()
        r24c10.send_keys("r24c10")

        # fill r24c11
        r24c11 = browser.find_element_by_name("r24c11")
        r24c11.clear()
        r24c11.send_keys("r24c11")

        # fill r24c12
        r24c12 = browser.find_element_by_name("r24c12")
        r24c12.clear()
        r24c12.send_keys("r24c12")

        # fill r24c13
        r24c13 = browser.find_element_by_name("r24c13")
        r24c13.clear()
        r24c13.send_keys("r24c13")

        # fill r24c14
        r24c14 = browser.find_element_by_name("r24c14")
        r24c14.clear()
        r24c14.send_keys("r24c14")

        # fill r24c15
        r24c15 = browser.find_element_by_name("r24c15")
        r24c15.clear()
        r24c15.send_keys("r24c15")

        # fill r24c16
        r24c16 = browser.find_element_by_name("r24c16")
        r24c16.clear()
        r24c16.send_keys("r24c16")

        # fill r24c17
        r24c17 = browser.find_element_by_name("r24c17")
        r24c17.clear()
        r24c17.send_keys("r24c17")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_annual_expense_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_flexible_budget(self):
        print("test_generate_html_to_pdf_flexible_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/flexible_budget')
        browser.get('https://holomorphe.com/reporting/flexible_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_flexible_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_static_budget(self):
        print("test_generate_html_to_pdf_static_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/static_budget')
        browser.get('https://holomorphe.com/reporting/static_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_static_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_static_budget_variance(self):
        print("test_generate_html_to_pdf_static_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/static_budget_variance')
        browser.get('https://holomorphe.com/reporting/static_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_static_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_month_operating_budget_variance(self):
        print("test_generate_html_to_pdf_month_operating_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/month_operating_budget_variance')
        browser.get('https://holomorphe.com/reporting/month_operating_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r1c14
        r1c14 = browser.find_element_by_name("r1c14")
        r1c14.clear()
        r1c14.send_keys("r1c14")

        # fill r1c15
        r1c15 = browser.find_element_by_name("r1c15")
        r1c15.clear()
        r1c15.send_keys("r1c15")

        # fill r1c16
        r1c16 = browser.find_element_by_name("r1c16")
        r1c16.clear()
        r1c16.send_keys("r1c16")

        # fill r1c17
        r1c17 = browser.find_element_by_name("r1c17")
        r1c17.clear()
        r1c17.send_keys("r1c17")

        # fill r1c18
        r1c18 = browser.find_element_by_name("r1c18")
        r1c18.clear()
        r1c18.send_keys("r1c18")

        # fill r1c19
        r1c19 = browser.find_element_by_name("r1c19")
        r1c19.clear()
        r1c19.send_keys("r1c19")

        # fill r1c20
        r1c20 = browser.find_element_by_name("r1c20")
        r1c20.clear()
        r1c20.send_keys("r1c20")

        # fill r1c21
        r1c21 = browser.find_element_by_name("r1c21")
        r1c21.clear()
        r1c21.send_keys("r1c21")

        # fill r1c22
        r1c22 = browser.find_element_by_name("r1c22")
        r1c22.clear()
        r1c22.send_keys("r1c22")

        # fill r1c23
        r1c23 = browser.find_element_by_name("r1c23")
        r1c23.clear()
        r1c23.send_keys("r1c23")

        # fill r1c24
        r1c24 = browser.find_element_by_name("r1c24")
        r1c24.clear()
        r1c24.send_keys("r1c24")

        # fill r1c25
        r1c25 = browser.find_element_by_name("r1c25")
        r1c25.clear()
        r1c25.send_keys("r1c25")

        # fill r1c26
        r1c26 = browser.find_element_by_name("r1c26")
        r1c26.clear()
        r1c26.send_keys("r1c26")

        # fill r1c27
        r1c27 = browser.find_element_by_name("r1c27")
        r1c27.clear()
        r1c27.send_keys("r1c27")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r2c14
        r2c14 = browser.find_element_by_name("r2c14")
        r2c14.clear()
        r2c14.send_keys("r2c14")

        # fill r2c15
        r2c15 = browser.find_element_by_name("r2c15")
        r2c15.clear()
        r2c15.send_keys("r2c15")

        # fill r2c16
        r2c16 = browser.find_element_by_name("r2c16")
        r2c16.clear()
        r2c16.send_keys("r2c16")

        # fill r2c17
        r2c17 = browser.find_element_by_name("r2c17")
        r2c17.clear()
        r2c17.send_keys("r2c17")

        # fill r2c18
        r2c18 = browser.find_element_by_name("r2c18")
        r2c18.clear()
        r2c18.send_keys("r2c18")

        # fill r2c19
        r2c19 = browser.find_element_by_name("r2c19")
        r2c19.clear()
        r2c19.send_keys("r2c19")

        # fill r2c20
        r2c20 = browser.find_element_by_name("r2c20")
        r2c20.clear()
        r2c20.send_keys("r2c20")

        # fill r2c21
        r2c21 = browser.find_element_by_name("r2c21")
        r2c21.clear()
        r2c21.send_keys("r2c21")

        # fill r2c22
        r2c22 = browser.find_element_by_name("r2c22")
        r2c22.clear()
        r2c22.send_keys("r2c22")

        # fill r2c23
        r2c23 = browser.find_element_by_name("r2c23")
        r2c23.clear()
        r2c23.send_keys("r2c23")

        # fill r2c24
        r2c24 = browser.find_element_by_name("r2c24")
        r2c24.clear()
        r2c24.send_keys("r2c24")

        # fill r2c25
        r2c25 = browser.find_element_by_name("r2c25")
        r2c25.clear()
        r2c25.send_keys("r2c25")

        # fill r2c26
        r2c26 = browser.find_element_by_name("r2c26")
        r2c26.clear()
        r2c26.send_keys("r2c26")

        # fill r2c27
        r2c27 = browser.find_element_by_name("r2c27")
        r2c27.clear()
        r2c27.send_keys("r2c27")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r3c14
        r3c14 = browser.find_element_by_name("r3c14")
        r3c14.clear()
        r3c14.send_keys("r3c14")

        # fill r3c15
        r3c15 = browser.find_element_by_name("r3c15")
        r3c15.clear()
        r3c15.send_keys("r3c15")

        # fill r3c16
        r3c16 = browser.find_element_by_name("r3c16")
        r3c16.clear()
        r3c16.send_keys("r3c16")

        # fill r3c17
        r3c17 = browser.find_element_by_name("r3c17")
        r3c17.clear()
        r3c17.send_keys("r3c17")

        # fill r3c18
        r3c18 = browser.find_element_by_name("r3c18")
        r3c18.clear()
        r3c18.send_keys("r3c18")

        # fill r3c19
        r3c19 = browser.find_element_by_name("r3c19")
        r3c19.clear()
        r3c19.send_keys("r3c19")

        # fill r3c20
        r3c20 = browser.find_element_by_name("r3c20")
        r3c20.clear()
        r3c20.send_keys("r3c20")

        # fill r3c21
        r3c21 = browser.find_element_by_name("r3c21")
        r3c21.clear()
        r3c21.send_keys("r3c21")

        # fill r3c22
        r3c22 = browser.find_element_by_name("r3c22")
        r3c22.clear()
        r3c22.send_keys("r3c22")

        # fill r3c23
        r3c23 = browser.find_element_by_name("r3c23")
        r3c23.clear()
        r3c23.send_keys("r3c23")

        # fill r3c24
        r3c24 = browser.find_element_by_name("r3c24")
        r3c24.clear()
        r3c24.send_keys("r3c24")

        # fill r3c25
        r3c25 = browser.find_element_by_name("r3c25")
        r3c25.clear()
        r3c25.send_keys("r3c25")

        # fill r3c26
        r3c26 = browser.find_element_by_name("r3c26")
        r3c26.clear()
        r3c26.send_keys("r3c26")

        # fill r3c27
        r3c27 = browser.find_element_by_name("r3c27")
        r3c27.clear()
        r3c27.send_keys("r3c27")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r4c14
        r4c14 = browser.find_element_by_name("r4c14")
        r4c14.clear()
        r4c14.send_keys("r4c14")

        # fill r4c15
        r4c15 = browser.find_element_by_name("r4c15")
        r4c15.clear()
        r4c15.send_keys("r4c15")

        # fill r4c16
        r4c16 = browser.find_element_by_name("r4c16")
        r4c16.clear()
        r4c16.send_keys("r4c16")

        # fill r4c17
        r4c17 = browser.find_element_by_name("r4c17")
        r4c17.clear()
        r4c17.send_keys("r4c17")

        # fill r4c18
        r4c18 = browser.find_element_by_name("r4c18")
        r4c18.clear()
        r4c18.send_keys("r4c18")

        # fill r4c19
        r4c19 = browser.find_element_by_name("r4c19")
        r4c19.clear()
        r4c19.send_keys("r4c19")

        # fill r4c20
        r4c20 = browser.find_element_by_name("r4c20")
        r4c20.clear()
        r4c20.send_keys("r4c20")

        # fill r4c21
        r4c21 = browser.find_element_by_name("r4c21")
        r4c21.clear()
        r4c21.send_keys("r4c21")

        # fill r4c22
        r4c22 = browser.find_element_by_name("r4c22")
        r4c22.clear()
        r4c22.send_keys("r4c22")

        # fill r4c23
        r4c23 = browser.find_element_by_name("r4c23")
        r4c23.clear()
        r4c23.send_keys("r4c23")

        # fill r4c24
        r4c24 = browser.find_element_by_name("r4c24")
        r4c24.clear()
        r4c24.send_keys("r4c24")

        # fill r4c25
        r4c25 = browser.find_element_by_name("r4c25")
        r4c25.clear()
        r4c25.send_keys("r4c25")

        # fill r4c26
        r4c26 = browser.find_element_by_name("r4c26")
        r4c26.clear()
        r4c26.send_keys("r4c26")

        # fill r4c27
        r4c27 = browser.find_element_by_name("r4c27")
        r4c27.clear()
        r4c27.send_keys("r4c27")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r5c14
        r5c14 = browser.find_element_by_name("r5c14")
        r5c14.clear()
        r5c14.send_keys("r5c14")

        # fill r5c15
        r5c15 = browser.find_element_by_name("r5c15")
        r5c15.clear()
        r5c15.send_keys("r5c15")

        # fill r5c16
        r5c16 = browser.find_element_by_name("r5c16")
        r5c16.clear()
        r5c16.send_keys("r5c16")

        # fill r5c17
        r5c17 = browser.find_element_by_name("r5c17")
        r5c17.clear()
        r5c17.send_keys("r5c17")

        # fill r5c18
        r5c18 = browser.find_element_by_name("r5c18")
        r5c18.clear()
        r5c18.send_keys("r5c18")

        # fill r5c19
        r5c19 = browser.find_element_by_name("r5c19")
        r5c19.clear()
        r5c19.send_keys("r5c19")

        # fill r5c20
        r5c20 = browser.find_element_by_name("r5c20")
        r5c20.clear()
        r5c20.send_keys("r5c20")

        # fill r5c21
        r5c21 = browser.find_element_by_name("r5c21")
        r5c21.clear()
        r5c21.send_keys("r5c21")

        # fill r5c22
        r5c22 = browser.find_element_by_name("r5c22")
        r5c22.clear()
        r5c22.send_keys("r5c22")

        # fill r5c23
        r5c23 = browser.find_element_by_name("r5c23")
        r5c23.clear()
        r5c23.send_keys("r5c23")

        # fill r5c24
        r5c24 = browser.find_element_by_name("r5c24")
        r5c24.clear()
        r5c24.send_keys("r5c24")

        # fill r5c25
        r5c25 = browser.find_element_by_name("r5c25")
        r5c25.clear()
        r5c25.send_keys("r5c25")

        # fill r5c26
        r5c26 = browser.find_element_by_name("r5c26")
        r5c26.clear()
        r5c26.send_keys("r5c26")

        # fill r5c27
        r5c27 = browser.find_element_by_name("r5c27")
        r5c27.clear()
        r5c27.send_keys("r5c27")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r6c14
        r6c14 = browser.find_element_by_name("r6c14")
        r6c14.clear()
        r6c14.send_keys("r6c14")

        # fill r6c15
        r6c15 = browser.find_element_by_name("r6c15")
        r6c15.clear()
        r6c15.send_keys("r6c15")

        # fill r6c16
        r6c16 = browser.find_element_by_name("r6c16")
        r6c16.clear()
        r6c16.send_keys("r6c16")

        # fill r6c17
        r6c17 = browser.find_element_by_name("r6c17")
        r6c17.clear()
        r6c17.send_keys("r6c17")

        # fill r6c18
        r6c18 = browser.find_element_by_name("r6c18")
        r6c18.clear()
        r6c18.send_keys("r6c18")

        # fill r6c19
        r6c19 = browser.find_element_by_name("r6c19")
        r6c19.clear()
        r6c19.send_keys("r6c19")

        # fill r6c20
        r6c20 = browser.find_element_by_name("r6c20")
        r6c20.clear()
        r6c20.send_keys("r6c20")

        # fill r6c21
        r6c21 = browser.find_element_by_name("r6c21")
        r6c21.clear()
        r6c21.send_keys("r6c21")

        # fill r6c22
        r6c22 = browser.find_element_by_name("r6c22")
        r6c22.clear()
        r6c22.send_keys("r6c22")

        # fill r6c23
        r6c23 = browser.find_element_by_name("r6c23")
        r6c23.clear()
        r6c23.send_keys("r6c23")

        # fill r6c24
        r6c24 = browser.find_element_by_name("r6c24")
        r6c24.clear()
        r6c24.send_keys("r6c24")

        # fill r6c25
        r6c25 = browser.find_element_by_name("r6c25")
        r6c25.clear()
        r6c25.send_keys("r6c25")

        # fill r6c26
        r6c26 = browser.find_element_by_name("r6c26")
        r6c26.clear()
        r6c26.send_keys("r6c26")

        # fill r6c27
        r6c27 = browser.find_element_by_name("r6c27")
        r6c27.clear()
        r6c27.send_keys("r6c27")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r7c14
        r7c14 = browser.find_element_by_name("r7c14")
        r7c14.clear()
        r7c14.send_keys("r7c14")

        # fill r7c15
        r7c15 = browser.find_element_by_name("r7c15")
        r7c15.clear()
        r7c15.send_keys("r7c15")

        # fill r7c16
        r7c16 = browser.find_element_by_name("r7c16")
        r7c16.clear()
        r7c16.send_keys("r7c16")

        # fill r7c17
        r7c17 = browser.find_element_by_name("r7c17")
        r7c17.clear()
        r7c17.send_keys("r7c17")

        # fill r7c18
        r7c18 = browser.find_element_by_name("r7c18")
        r7c18.clear()
        r7c18.send_keys("r7c18")

        # fill r7c19
        r7c19 = browser.find_element_by_name("r7c19")
        r7c19.clear()
        r7c19.send_keys("r7c19")

        # fill r7c20
        r7c20 = browser.find_element_by_name("r7c20")
        r7c20.clear()
        r7c20.send_keys("r7c20")

        # fill r7c21
        r7c21 = browser.find_element_by_name("r7c21")
        r7c21.clear()
        r7c21.send_keys("r7c21")

        # fill r7c22
        r7c22 = browser.find_element_by_name("r7c22")
        r7c22.clear()
        r7c22.send_keys("r7c22")

        # fill r7c23
        r7c23 = browser.find_element_by_name("r7c23")
        r7c23.clear()
        r7c23.send_keys("r7c23")

        # fill r7c24
        r7c24 = browser.find_element_by_name("r7c24")
        r7c24.clear()
        r7c24.send_keys("r7c24")

        # fill r7c25
        r7c25 = browser.find_element_by_name("r7c25")
        r7c25.clear()
        r7c25.send_keys("r7c25")

        # fill r7c26
        r7c26 = browser.find_element_by_name("r7c26")
        r7c26.clear()
        r7c26.send_keys("r7c26")

        # fill r7c27
        r7c27 = browser.find_element_by_name("r7c27")
        r7c27.clear()
        r7c27.send_keys("r7c27")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r8c14
        r8c14 = browser.find_element_by_name("r8c14")
        r8c14.clear()
        r8c14.send_keys("r8c14")

        # fill r8c15
        r8c15 = browser.find_element_by_name("r8c15")
        r8c15.clear()
        r8c15.send_keys("r8c15")

        # fill r8c16
        r8c16 = browser.find_element_by_name("r8c16")
        r8c16.clear()
        r8c16.send_keys("r8c16")

        # fill r8c17
        r8c17 = browser.find_element_by_name("r8c17")
        r8c17.clear()
        r8c17.send_keys("r8c17")

        # fill r8c18
        r8c18 = browser.find_element_by_name("r8c18")
        r8c18.clear()
        r8c18.send_keys("r8c18")

        # fill r8c19
        r8c19 = browser.find_element_by_name("r8c19")
        r8c19.clear()
        r8c19.send_keys("r8c19")

        # fill r8c20
        r8c20 = browser.find_element_by_name("r8c20")
        r8c20.clear()
        r8c20.send_keys("r8c20")

        # fill r8c21
        r8c21 = browser.find_element_by_name("r8c21")
        r8c21.clear()
        r8c21.send_keys("r8c21")

        # fill r8c22
        r8c22 = browser.find_element_by_name("r8c22")
        r8c22.clear()
        r8c22.send_keys("r8c22")

        # fill r8c23
        r8c23 = browser.find_element_by_name("r8c23")
        r8c23.clear()
        r8c23.send_keys("r8c23")

        # fill r8c24
        r8c24 = browser.find_element_by_name("r8c24")
        r8c24.clear()
        r8c24.send_keys("r8c24")

        # fill r8c25
        r8c25 = browser.find_element_by_name("r8c25")
        r8c25.clear()
        r8c25.send_keys("r8c25")

        # fill r8c26
        r8c26 = browser.find_element_by_name("r8c26")
        r8c26.clear()
        r8c26.send_keys("r8c26")

        # fill r8c27
        r8c27 = browser.find_element_by_name("r8c27")
        r8c27.clear()
        r8c27.send_keys("r8c27")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r9c14
        r9c14 = browser.find_element_by_name("r9c14")
        r9c14.clear()
        r9c14.send_keys("r9c14")

        # fill r9c15
        r9c15 = browser.find_element_by_name("r9c15")
        r9c15.clear()
        r9c15.send_keys("r9c15")

        # fill r9c16
        r9c16 = browser.find_element_by_name("r9c16")
        r9c16.clear()
        r9c16.send_keys("r9c16")

        # fill r9c17
        r9c17 = browser.find_element_by_name("r9c17")
        r9c17.clear()
        r9c17.send_keys("r9c17")

        # fill r9c18
        r9c18 = browser.find_element_by_name("r9c18")
        r9c18.clear()
        r9c18.send_keys("r9c18")

        # fill r9c19
        r9c19 = browser.find_element_by_name("r9c19")
        r9c19.clear()
        r9c19.send_keys("r9c19")

        # fill r9c20
        r9c20 = browser.find_element_by_name("r9c20")
        r9c20.clear()
        r9c20.send_keys("r9c20")

        # fill r9c21
        r9c21 = browser.find_element_by_name("r9c21")
        r9c21.clear()
        r9c21.send_keys("r9c21")

        # fill r9c22
        r9c22 = browser.find_element_by_name("r9c22")
        r9c22.clear()
        r9c22.send_keys("r9c22")

        # fill r9c23
        r9c23 = browser.find_element_by_name("r9c23")
        r9c23.clear()
        r9c23.send_keys("r9c23")

        # fill r9c24
        r9c24 = browser.find_element_by_name("r9c24")
        r9c24.clear()
        r9c24.send_keys("r9c24")

        # fill r9c25
        r9c25 = browser.find_element_by_name("r9c25")
        r9c25.clear()
        r9c25.send_keys("r9c25")

        # fill r9c26
        r9c26 = browser.find_element_by_name("r9c26")
        r9c26.clear()
        r9c26.send_keys("r9c26")

        # fill r9c27
        r9c27 = browser.find_element_by_name("r9c27")
        r9c27.clear()
        r9c27.send_keys("r9c27")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r10c14
        r10c14 = browser.find_element_by_name("r10c14")
        r10c14.clear()
        r10c14.send_keys("r10c14")

        # fill r10c15
        r10c15 = browser.find_element_by_name("r10c15")
        r10c15.clear()
        r10c15.send_keys("r10c15")

        # fill r10c16
        r10c16 = browser.find_element_by_name("r10c16")
        r10c16.clear()
        r10c16.send_keys("r10c16")

        # fill r10c17
        r10c17 = browser.find_element_by_name("r10c17")
        r10c17.clear()
        r10c17.send_keys("r10c17")

        # fill r10c18
        r10c18 = browser.find_element_by_name("r10c18")
        r10c18.clear()
        r10c18.send_keys("r10c18")

        # fill r10c19
        r10c19 = browser.find_element_by_name("r10c19")
        r10c19.clear()
        r10c19.send_keys("r10c19")

        # fill r10c20
        r10c20 = browser.find_element_by_name("r10c20")
        r10c20.clear()
        r10c20.send_keys("r10c20")

        # fill r10c21
        r10c21 = browser.find_element_by_name("r10c21")
        r10c21.clear()
        r10c21.send_keys("r10c21")

        # fill r10c22
        r10c22 = browser.find_element_by_name("r10c22")
        r10c22.clear()
        r10c22.send_keys("r10c22")

        # fill r10c23
        r10c23 = browser.find_element_by_name("r10c23")
        r10c23.clear()
        r10c23.send_keys("r10c23")

        # fill r10c24
        r10c24 = browser.find_element_by_name("r10c24")
        r10c24.clear()
        r10c24.send_keys("r10c24")

        # fill r10c25
        r10c25 = browser.find_element_by_name("r10c25")
        r10c25.clear()
        r10c25.send_keys("r10c25")

        # fill r10c26
        r10c26 = browser.find_element_by_name("r10c26")
        r10c26.clear()
        r10c26.send_keys("r10c26")

        # fill r10c27
        r10c27 = browser.find_element_by_name("r10c27")
        r10c27.clear()
        r10c27.send_keys("r10c27")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r11c14
        r11c14 = browser.find_element_by_name("r11c14")
        r11c14.clear()
        r11c14.send_keys("r11c14")

        # fill r11c15
        r11c15 = browser.find_element_by_name("r11c15")
        r11c15.clear()
        r11c15.send_keys("r11c15")

        # fill r11c16
        r11c16 = browser.find_element_by_name("r11c16")
        r11c16.clear()
        r11c16.send_keys("r11c16")

        # fill r11c17
        r11c17 = browser.find_element_by_name("r11c17")
        r11c17.clear()
        r11c17.send_keys("r11c17")

        # fill r11c18
        r11c18 = browser.find_element_by_name("r11c18")
        r11c18.clear()
        r11c18.send_keys("r11c18")

        # fill r11c19
        r11c19 = browser.find_element_by_name("r11c19")
        r11c19.clear()
        r11c19.send_keys("r11c19")

        # fill r11c20
        r11c20 = browser.find_element_by_name("r11c20")
        r11c20.clear()
        r11c20.send_keys("r11c20")

        # fill r11c21
        r11c21 = browser.find_element_by_name("r11c21")
        r11c21.clear()
        r11c21.send_keys("r11c21")

        # fill r11c22
        r11c22 = browser.find_element_by_name("r11c22")
        r11c22.clear()
        r11c22.send_keys("r11c22")

        # fill r11c23
        r11c23 = browser.find_element_by_name("r11c23")
        r11c23.clear()
        r11c23.send_keys("r11c23")

        # fill r11c24
        r11c24 = browser.find_element_by_name("r11c24")
        r11c24.clear()
        r11c24.send_keys("r11c24")

        # fill r11c25
        r11c25 = browser.find_element_by_name("r11c25")
        r11c25.clear()
        r11c25.send_keys("r11c25")

        # fill r11c26
        r11c26 = browser.find_element_by_name("r11c26")
        r11c26.clear()
        r11c26.send_keys("r11c26")

        # fill r11c27
        r11c27 = browser.find_element_by_name("r11c27")
        r11c27.clear()
        r11c27.send_keys("r11c27")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r12c14
        r12c14 = browser.find_element_by_name("r12c14")
        r12c14.clear()
        r12c14.send_keys("r12c14")

        # fill r12c15
        r12c15 = browser.find_element_by_name("r12c15")
        r12c15.clear()
        r12c15.send_keys("r12c15")

        # fill r12c16
        r12c16 = browser.find_element_by_name("r12c16")
        r12c16.clear()
        r12c16.send_keys("r12c16")

        # fill r12c17
        r12c17 = browser.find_element_by_name("r12c17")
        r12c17.clear()
        r12c17.send_keys("r12c17")

        # fill r12c18
        r12c18 = browser.find_element_by_name("r12c18")
        r12c18.clear()
        r12c18.send_keys("r12c18")

        # fill r12c19
        r12c19 = browser.find_element_by_name("r12c19")
        r12c19.clear()
        r12c19.send_keys("r12c19")

        # fill r12c20
        r12c20 = browser.find_element_by_name("r12c20")
        r12c20.clear()
        r12c20.send_keys("r12c20")

        # fill r12c21
        r12c21 = browser.find_element_by_name("r12c21")
        r12c21.clear()
        r12c21.send_keys("r12c21")

        # fill r12c22
        r12c22 = browser.find_element_by_name("r12c22")
        r12c22.clear()
        r12c22.send_keys("r12c22")

        # fill r12c23
        r12c23 = browser.find_element_by_name("r12c23")
        r12c23.clear()
        r12c23.send_keys("r12c23")

        # fill r12c24
        r12c24 = browser.find_element_by_name("r12c24")
        r12c24.clear()
        r12c24.send_keys("r12c24")

        # fill r12c25
        r12c25 = browser.find_element_by_name("r12c25")
        r12c25.clear()
        r12c25.send_keys("r12c25")

        # fill r12c26
        r12c26 = browser.find_element_by_name("r12c26")
        r12c26.clear()
        r12c26.send_keys("r12c26")

        # fill r12c27
        r12c27 = browser.find_element_by_name("r12c27")
        r12c27.clear()
        r12c27.send_keys("r12c27")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r13c14
        r13c14 = browser.find_element_by_name("r13c14")
        r13c14.clear()
        r13c14.send_keys("r13c14")

        # fill r13c15
        r13c15 = browser.find_element_by_name("r13c15")
        r13c15.clear()
        r13c15.send_keys("r13c15")

        # fill r13c16
        r13c16 = browser.find_element_by_name("r13c16")
        r13c16.clear()
        r13c16.send_keys("r13c16")

        # fill r13c17
        r13c17 = browser.find_element_by_name("r13c17")
        r13c17.clear()
        r13c17.send_keys("r13c17")

        # fill r13c18
        r13c18 = browser.find_element_by_name("r13c18")
        r13c18.clear()
        r13c18.send_keys("r13c18")

        # fill r13c19
        r13c19 = browser.find_element_by_name("r13c19")
        r13c19.clear()
        r13c19.send_keys("r13c19")

        # fill r13c20
        r13c20 = browser.find_element_by_name("r13c20")
        r13c20.clear()
        r13c20.send_keys("r13c20")

        # fill r13c21
        r13c21 = browser.find_element_by_name("r13c21")
        r13c21.clear()
        r13c21.send_keys("r13c21")

        # fill r13c22
        r13c22 = browser.find_element_by_name("r13c22")
        r13c22.clear()
        r13c22.send_keys("r13c22")

        # fill r13c23
        r13c23 = browser.find_element_by_name("r13c23")
        r13c23.clear()
        r13c23.send_keys("r13c23")

        # fill r13c24
        r13c24 = browser.find_element_by_name("r13c24")
        r13c24.clear()
        r13c24.send_keys("r13c24")

        # fill r13c25
        r13c25 = browser.find_element_by_name("r13c25")
        r13c25.clear()
        r13c25.send_keys("r13c25")

        # fill r13c26
        r13c26 = browser.find_element_by_name("r13c26")
        r13c26.clear()
        r13c26.send_keys("r13c26")

        # fill r13c27
        r13c27 = browser.find_element_by_name("r13c27")
        r13c27.clear()
        r13c27.send_keys("r13c27")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r14c14
        r14c14 = browser.find_element_by_name("r14c14")
        r14c14.clear()
        r14c14.send_keys("r14c14")

        # fill r14c15
        r14c15 = browser.find_element_by_name("r14c15")
        r14c15.clear()
        r14c15.send_keys("r14c15")

        # fill r14c16
        r14c16 = browser.find_element_by_name("r14c16")
        r14c16.clear()
        r14c16.send_keys("r14c16")

        # fill r14c17
        r14c17 = browser.find_element_by_name("r14c17")
        r14c17.clear()
        r14c17.send_keys("r14c17")

        # fill r14c18
        r14c18 = browser.find_element_by_name("r14c18")
        r14c18.clear()
        r14c18.send_keys("r14c18")

        # fill r14c19
        r14c19 = browser.find_element_by_name("r14c19")
        r14c19.clear()
        r14c19.send_keys("r14c19")

        # fill r14c20
        r14c20 = browser.find_element_by_name("r14c20")
        r14c20.clear()
        r14c20.send_keys("r14c20")

        # fill r14c21
        r14c21 = browser.find_element_by_name("r14c21")
        r14c21.clear()
        r14c21.send_keys("r14c21")

        # fill r14c22
        r14c22 = browser.find_element_by_name("r14c22")
        r14c22.clear()
        r14c22.send_keys("r14c22")

        # fill r14c23
        r14c23 = browser.find_element_by_name("r14c23")
        r14c23.clear()
        r14c23.send_keys("r14c23")

        # fill r14c24
        r14c24 = browser.find_element_by_name("r14c24")
        r14c24.clear()
        r14c24.send_keys("r14c24")

        # fill r14c25
        r14c25 = browser.find_element_by_name("r14c25")
        r14c25.clear()
        r14c25.send_keys("r14c25")

        # fill r14c26
        r14c26 = browser.find_element_by_name("r14c26")
        r14c26.clear()
        r14c26.send_keys("r14c26")

        # fill r14c27
        r14c27 = browser.find_element_by_name("r14c27")
        r14c27.clear()
        r14c27.send_keys("r14c27")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r15c14
        r15c14 = browser.find_element_by_name("r15c14")
        r15c14.clear()
        r15c14.send_keys("r15c14")

        # fill r15c15
        r15c15 = browser.find_element_by_name("r15c15")
        r15c15.clear()
        r15c15.send_keys("r15c15")

        # fill r15c16
        r15c16 = browser.find_element_by_name("r15c16")
        r15c16.clear()
        r15c16.send_keys("r15c16")

        # fill r15c17
        r15c17 = browser.find_element_by_name("r15c17")
        r15c17.clear()
        r15c17.send_keys("r15c17")

        # fill r15c18
        r15c18 = browser.find_element_by_name("r15c18")
        r15c18.clear()
        r15c18.send_keys("r15c18")

        # fill r15c19
        r15c19 = browser.find_element_by_name("r15c19")
        r15c19.clear()
        r15c19.send_keys("r15c19")

        # fill r15c20
        r15c20 = browser.find_element_by_name("r15c20")
        r15c20.clear()
        r15c20.send_keys("r15c20")

        # fill r15c21
        r15c21 = browser.find_element_by_name("r15c21")
        r15c21.clear()
        r15c21.send_keys("r15c21")

        # fill r15c22
        r15c22 = browser.find_element_by_name("r15c22")
        r15c22.clear()
        r15c22.send_keys("r15c22")

        # fill r15c23
        r15c23 = browser.find_element_by_name("r15c23")
        r15c23.clear()
        r15c23.send_keys("r15c23")

        # fill r15c24
        r15c24 = browser.find_element_by_name("r15c24")
        r15c24.clear()
        r15c24.send_keys("r15c24")

        # fill r15c25
        r15c25 = browser.find_element_by_name("r15c25")
        r15c25.clear()
        r15c25.send_keys("r15c25")

        # fill r15c26
        r15c26 = browser.find_element_by_name("r15c26")
        r15c26.clear()
        r15c26.send_keys("r15c26")

        # fill r15c27
        r15c27 = browser.find_element_by_name("r15c27")
        r15c27.clear()
        r15c27.send_keys("r15c27")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_month_operating_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_flexible_budget_variance(self):
        print("test_generate_html_to_pdf_flexible_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/flexible_budget_variance')
        browser.get('https://holomorphe.com/reporting/flexible_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_flexible_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_twelve_month_marketing_budget_variance(self):
        print("test_generate_html_to_pdf_twelve_month_marketing_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/twelve_month_marketing_budget_variance')
        browser.get('https://holomorphe.com/reporting/twelve_month_marketing_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r1c14
        r1c14 = browser.find_element_by_name("r1c14")
        r1c14.clear()
        r1c14.send_keys("r1c14")

        # fill r1c15
        r1c15 = browser.find_element_by_name("r1c15")
        r1c15.clear()
        r1c15.send_keys("r1c15")

        # fill r1c16
        r1c16 = browser.find_element_by_name("r1c16")
        r1c16.clear()
        r1c16.send_keys("r1c16")

        # fill r1c17
        r1c17 = browser.find_element_by_name("r1c17")
        r1c17.clear()
        r1c17.send_keys("r1c17")

        # fill r1c18
        r1c18 = browser.find_element_by_name("r1c18")
        r1c18.clear()
        r1c18.send_keys("r1c18")

        # fill r1c19
        r1c19 = browser.find_element_by_name("r1c19")
        r1c19.clear()
        r1c19.send_keys("r1c19")

        # fill r1c20
        r1c20 = browser.find_element_by_name("r1c20")
        r1c20.clear()
        r1c20.send_keys("r1c20")

        # fill r1c21
        r1c21 = browser.find_element_by_name("r1c21")
        r1c21.clear()
        r1c21.send_keys("r1c21")

        # fill r1c22
        r1c22 = browser.find_element_by_name("r1c22")
        r1c22.clear()
        r1c22.send_keys("r1c22")

        # fill r1c23
        r1c23 = browser.find_element_by_name("r1c23")
        r1c23.clear()
        r1c23.send_keys("r1c23")

        # fill r1c24
        r1c24 = browser.find_element_by_name("r1c24")
        r1c24.clear()
        r1c24.send_keys("r1c24")

        # fill r1c25
        r1c25 = browser.find_element_by_name("r1c25")
        r1c25.clear()
        r1c25.send_keys("r1c25")

        # fill r1c26
        r1c26 = browser.find_element_by_name("r1c26")
        r1c26.clear()
        r1c26.send_keys("r1c26")

        # fill r1c27
        r1c27 = browser.find_element_by_name("r1c27")
        r1c27.clear()
        r1c27.send_keys("r1c27")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r2c14
        r2c14 = browser.find_element_by_name("r2c14")
        r2c14.clear()
        r2c14.send_keys("r2c14")

        # fill r2c15
        r2c15 = browser.find_element_by_name("r2c15")
        r2c15.clear()
        r2c15.send_keys("r2c15")

        # fill r2c16
        r2c16 = browser.find_element_by_name("r2c16")
        r2c16.clear()
        r2c16.send_keys("r2c16")

        # fill r2c17
        r2c17 = browser.find_element_by_name("r2c17")
        r2c17.clear()
        r2c17.send_keys("r2c17")

        # fill r2c18
        r2c18 = browser.find_element_by_name("r2c18")
        r2c18.clear()
        r2c18.send_keys("r2c18")

        # fill r2c19
        r2c19 = browser.find_element_by_name("r2c19")
        r2c19.clear()
        r2c19.send_keys("r2c19")

        # fill r2c20
        r2c20 = browser.find_element_by_name("r2c20")
        r2c20.clear()
        r2c20.send_keys("r2c20")

        # fill r2c21
        r2c21 = browser.find_element_by_name("r2c21")
        r2c21.clear()
        r2c21.send_keys("r2c21")

        # fill r2c22
        r2c22 = browser.find_element_by_name("r2c22")
        r2c22.clear()
        r2c22.send_keys("r2c22")

        # fill r2c23
        r2c23 = browser.find_element_by_name("r2c23")
        r2c23.clear()
        r2c23.send_keys("r2c23")

        # fill r2c24
        r2c24 = browser.find_element_by_name("r2c24")
        r2c24.clear()
        r2c24.send_keys("r2c24")

        # fill r2c25
        r2c25 = browser.find_element_by_name("r2c25")
        r2c25.clear()
        r2c25.send_keys("r2c25")

        # fill r2c26
        r2c26 = browser.find_element_by_name("r2c26")
        r2c26.clear()
        r2c26.send_keys("r2c26")

        # fill r2c27
        r2c27 = browser.find_element_by_name("r2c27")
        r2c27.clear()
        r2c27.send_keys("r2c27")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r3c14
        r3c14 = browser.find_element_by_name("r3c14")
        r3c14.clear()
        r3c14.send_keys("r3c14")

        # fill r3c15
        r3c15 = browser.find_element_by_name("r3c15")
        r3c15.clear()
        r3c15.send_keys("r3c15")

        # fill r3c16
        r3c16 = browser.find_element_by_name("r3c16")
        r3c16.clear()
        r3c16.send_keys("r3c16")

        # fill r3c17
        r3c17 = browser.find_element_by_name("r3c17")
        r3c17.clear()
        r3c17.send_keys("r3c17")

        # fill r3c18
        r3c18 = browser.find_element_by_name("r3c18")
        r3c18.clear()
        r3c18.send_keys("r3c18")

        # fill r3c19
        r3c19 = browser.find_element_by_name("r3c19")
        r3c19.clear()
        r3c19.send_keys("r3c19")

        # fill r3c20
        r3c20 = browser.find_element_by_name("r3c20")
        r3c20.clear()
        r3c20.send_keys("r3c20")

        # fill r3c21
        r3c21 = browser.find_element_by_name("r3c21")
        r3c21.clear()
        r3c21.send_keys("r3c21")

        # fill r3c22
        r3c22 = browser.find_element_by_name("r3c22")
        r3c22.clear()
        r3c22.send_keys("r3c22")

        # fill r3c23
        r3c23 = browser.find_element_by_name("r3c23")
        r3c23.clear()
        r3c23.send_keys("r3c23")

        # fill r3c24
        r3c24 = browser.find_element_by_name("r3c24")
        r3c24.clear()
        r3c24.send_keys("r3c24")

        # fill r3c25
        r3c25 = browser.find_element_by_name("r3c25")
        r3c25.clear()
        r3c25.send_keys("r3c25")

        # fill r3c26
        r3c26 = browser.find_element_by_name("r3c26")
        r3c26.clear()
        r3c26.send_keys("r3c26")

        # fill r3c27
        r3c27 = browser.find_element_by_name("r3c27")
        r3c27.clear()
        r3c27.send_keys("r3c27")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r4c14
        r4c14 = browser.find_element_by_name("r4c14")
        r4c14.clear()
        r4c14.send_keys("r4c14")

        # fill r4c15
        r4c15 = browser.find_element_by_name("r4c15")
        r4c15.clear()
        r4c15.send_keys("r4c15")

        # fill r4c16
        r4c16 = browser.find_element_by_name("r4c16")
        r4c16.clear()
        r4c16.send_keys("r4c16")

        # fill r4c17
        r4c17 = browser.find_element_by_name("r4c17")
        r4c17.clear()
        r4c17.send_keys("r4c17")

        # fill r4c18
        r4c18 = browser.find_element_by_name("r4c18")
        r4c18.clear()
        r4c18.send_keys("r4c18")

        # fill r4c19
        r4c19 = browser.find_element_by_name("r4c19")
        r4c19.clear()
        r4c19.send_keys("r4c19")

        # fill r4c20
        r4c20 = browser.find_element_by_name("r4c20")
        r4c20.clear()
        r4c20.send_keys("r4c20")

        # fill r4c21
        r4c21 = browser.find_element_by_name("r4c21")
        r4c21.clear()
        r4c21.send_keys("r4c21")

        # fill r4c22
        r4c22 = browser.find_element_by_name("r4c22")
        r4c22.clear()
        r4c22.send_keys("r4c22")

        # fill r4c23
        r4c23 = browser.find_element_by_name("r4c23")
        r4c23.clear()
        r4c23.send_keys("r4c23")

        # fill r4c24
        r4c24 = browser.find_element_by_name("r4c24")
        r4c24.clear()
        r4c24.send_keys("r4c24")

        # fill r4c25
        r4c25 = browser.find_element_by_name("r4c25")
        r4c25.clear()
        r4c25.send_keys("r4c25")

        # fill r4c26
        r4c26 = browser.find_element_by_name("r4c26")
        r4c26.clear()
        r4c26.send_keys("r4c26")

        # fill r4c27
        r4c27 = browser.find_element_by_name("r4c27")
        r4c27.clear()
        r4c27.send_keys("r4c27")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r5c14
        r5c14 = browser.find_element_by_name("r5c14")
        r5c14.clear()
        r5c14.send_keys("r5c14")

        # fill r5c15
        r5c15 = browser.find_element_by_name("r5c15")
        r5c15.clear()
        r5c15.send_keys("r5c15")

        # fill r5c16
        r5c16 = browser.find_element_by_name("r5c16")
        r5c16.clear()
        r5c16.send_keys("r5c16")

        # fill r5c17
        r5c17 = browser.find_element_by_name("r5c17")
        r5c17.clear()
        r5c17.send_keys("r5c17")

        # fill r5c18
        r5c18 = browser.find_element_by_name("r5c18")
        r5c18.clear()
        r5c18.send_keys("r5c18")

        # fill r5c19
        r5c19 = browser.find_element_by_name("r5c19")
        r5c19.clear()
        r5c19.send_keys("r5c19")

        # fill r5c20
        r5c20 = browser.find_element_by_name("r5c20")
        r5c20.clear()
        r5c20.send_keys("r5c20")

        # fill r5c21
        r5c21 = browser.find_element_by_name("r5c21")
        r5c21.clear()
        r5c21.send_keys("r5c21")

        # fill r5c22
        r5c22 = browser.find_element_by_name("r5c22")
        r5c22.clear()
        r5c22.send_keys("r5c22")

        # fill r5c23
        r5c23 = browser.find_element_by_name("r5c23")
        r5c23.clear()
        r5c23.send_keys("r5c23")

        # fill r5c24
        r5c24 = browser.find_element_by_name("r5c24")
        r5c24.clear()
        r5c24.send_keys("r5c24")

        # fill r5c25
        r5c25 = browser.find_element_by_name("r5c25")
        r5c25.clear()
        r5c25.send_keys("r5c25")

        # fill r5c26
        r5c26 = browser.find_element_by_name("r5c26")
        r5c26.clear()
        r5c26.send_keys("r5c26")

        # fill r5c27
        r5c27 = browser.find_element_by_name("r5c27")
        r5c27.clear()
        r5c27.send_keys("r5c27")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r6c14
        r6c14 = browser.find_element_by_name("r6c14")
        r6c14.clear()
        r6c14.send_keys("r6c14")

        # fill r6c15
        r6c15 = browser.find_element_by_name("r6c15")
        r6c15.clear()
        r6c15.send_keys("r6c15")

        # fill r6c16
        r6c16 = browser.find_element_by_name("r6c16")
        r6c16.clear()
        r6c16.send_keys("r6c16")

        # fill r6c17
        r6c17 = browser.find_element_by_name("r6c17")
        r6c17.clear()
        r6c17.send_keys("r6c17")

        # fill r6c18
        r6c18 = browser.find_element_by_name("r6c18")
        r6c18.clear()
        r6c18.send_keys("r6c18")

        # fill r6c19
        r6c19 = browser.find_element_by_name("r6c19")
        r6c19.clear()
        r6c19.send_keys("r6c19")

        # fill r6c20
        r6c20 = browser.find_element_by_name("r6c20")
        r6c20.clear()
        r6c20.send_keys("r6c20")

        # fill r6c21
        r6c21 = browser.find_element_by_name("r6c21")
        r6c21.clear()
        r6c21.send_keys("r6c21")

        # fill r6c22
        r6c22 = browser.find_element_by_name("r6c22")
        r6c22.clear()
        r6c22.send_keys("r6c22")

        # fill r6c23
        r6c23 = browser.find_element_by_name("r6c23")
        r6c23.clear()
        r6c23.send_keys("r6c23")

        # fill r6c24
        r6c24 = browser.find_element_by_name("r6c24")
        r6c24.clear()
        r6c24.send_keys("r6c24")

        # fill r6c25
        r6c25 = browser.find_element_by_name("r6c25")
        r6c25.clear()
        r6c25.send_keys("r6c25")

        # fill r6c26
        r6c26 = browser.find_element_by_name("r6c26")
        r6c26.clear()
        r6c26.send_keys("r6c26")

        # fill r6c27
        r6c27 = browser.find_element_by_name("r6c27")
        r6c27.clear()
        r6c27.send_keys("r6c27")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r7c14
        r7c14 = browser.find_element_by_name("r7c14")
        r7c14.clear()
        r7c14.send_keys("r7c14")

        # fill r7c15
        r7c15 = browser.find_element_by_name("r7c15")
        r7c15.clear()
        r7c15.send_keys("r7c15")

        # fill r7c16
        r7c16 = browser.find_element_by_name("r7c16")
        r7c16.clear()
        r7c16.send_keys("r7c16")

        # fill r7c17
        r7c17 = browser.find_element_by_name("r7c17")
        r7c17.clear()
        r7c17.send_keys("r7c17")

        # fill r7c18
        r7c18 = browser.find_element_by_name("r7c18")
        r7c18.clear()
        r7c18.send_keys("r7c18")

        # fill r7c19
        r7c19 = browser.find_element_by_name("r7c19")
        r7c19.clear()
        r7c19.send_keys("r7c19")

        # fill r7c20
        r7c20 = browser.find_element_by_name("r7c20")
        r7c20.clear()
        r7c20.send_keys("r7c20")

        # fill r7c21
        r7c21 = browser.find_element_by_name("r7c21")
        r7c21.clear()
        r7c21.send_keys("r7c21")

        # fill r7c22
        r7c22 = browser.find_element_by_name("r7c22")
        r7c22.clear()
        r7c22.send_keys("r7c22")

        # fill r7c23
        r7c23 = browser.find_element_by_name("r7c23")
        r7c23.clear()
        r7c23.send_keys("r7c23")

        # fill r7c24
        r7c24 = browser.find_element_by_name("r7c24")
        r7c24.clear()
        r7c24.send_keys("r7c24")

        # fill r7c25
        r7c25 = browser.find_element_by_name("r7c25")
        r7c25.clear()
        r7c25.send_keys("r7c25")

        # fill r7c26
        r7c26 = browser.find_element_by_name("r7c26")
        r7c26.clear()
        r7c26.send_keys("r7c26")

        # fill r7c27
        r7c27 = browser.find_element_by_name("r7c27")
        r7c27.clear()
        r7c27.send_keys("r7c27")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r8c14
        r8c14 = browser.find_element_by_name("r8c14")
        r8c14.clear()
        r8c14.send_keys("r8c14")

        # fill r8c15
        r8c15 = browser.find_element_by_name("r8c15")
        r8c15.clear()
        r8c15.send_keys("r8c15")

        # fill r8c16
        r8c16 = browser.find_element_by_name("r8c16")
        r8c16.clear()
        r8c16.send_keys("r8c16")

        # fill r8c17
        r8c17 = browser.find_element_by_name("r8c17")
        r8c17.clear()
        r8c17.send_keys("r8c17")

        # fill r8c18
        r8c18 = browser.find_element_by_name("r8c18")
        r8c18.clear()
        r8c18.send_keys("r8c18")

        # fill r8c19
        r8c19 = browser.find_element_by_name("r8c19")
        r8c19.clear()
        r8c19.send_keys("r8c19")

        # fill r8c20
        r8c20 = browser.find_element_by_name("r8c20")
        r8c20.clear()
        r8c20.send_keys("r8c20")

        # fill r8c21
        r8c21 = browser.find_element_by_name("r8c21")
        r8c21.clear()
        r8c21.send_keys("r8c21")

        # fill r8c22
        r8c22 = browser.find_element_by_name("r8c22")
        r8c22.clear()
        r8c22.send_keys("r8c22")

        # fill r8c23
        r8c23 = browser.find_element_by_name("r8c23")
        r8c23.clear()
        r8c23.send_keys("r8c23")

        # fill r8c24
        r8c24 = browser.find_element_by_name("r8c24")
        r8c24.clear()
        r8c24.send_keys("r8c24")

        # fill r8c25
        r8c25 = browser.find_element_by_name("r8c25")
        r8c25.clear()
        r8c25.send_keys("r8c25")

        # fill r8c26
        r8c26 = browser.find_element_by_name("r8c26")
        r8c26.clear()
        r8c26.send_keys("r8c26")

        # fill r8c27
        r8c27 = browser.find_element_by_name("r8c27")
        r8c27.clear()
        r8c27.send_keys("r8c27")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r9c14
        r9c14 = browser.find_element_by_name("r9c14")
        r9c14.clear()
        r9c14.send_keys("r9c14")

        # fill r9c15
        r9c15 = browser.find_element_by_name("r9c15")
        r9c15.clear()
        r9c15.send_keys("r9c15")

        # fill r9c16
        r9c16 = browser.find_element_by_name("r9c16")
        r9c16.clear()
        r9c16.send_keys("r9c16")

        # fill r9c17
        r9c17 = browser.find_element_by_name("r9c17")
        r9c17.clear()
        r9c17.send_keys("r9c17")

        # fill r9c18
        r9c18 = browser.find_element_by_name("r9c18")
        r9c18.clear()
        r9c18.send_keys("r9c18")

        # fill r9c19
        r9c19 = browser.find_element_by_name("r9c19")
        r9c19.clear()
        r9c19.send_keys("r9c19")

        # fill r9c20
        r9c20 = browser.find_element_by_name("r9c20")
        r9c20.clear()
        r9c20.send_keys("r9c20")

        # fill r9c21
        r9c21 = browser.find_element_by_name("r9c21")
        r9c21.clear()
        r9c21.send_keys("r9c21")

        # fill r9c22
        r9c22 = browser.find_element_by_name("r9c22")
        r9c22.clear()
        r9c22.send_keys("r9c22")

        # fill r9c23
        r9c23 = browser.find_element_by_name("r9c23")
        r9c23.clear()
        r9c23.send_keys("r9c23")

        # fill r9c24
        r9c24 = browser.find_element_by_name("r9c24")
        r9c24.clear()
        r9c24.send_keys("r9c24")

        # fill r9c25
        r9c25 = browser.find_element_by_name("r9c25")
        r9c25.clear()
        r9c25.send_keys("r9c25")

        # fill r9c26
        r9c26 = browser.find_element_by_name("r9c26")
        r9c26.clear()
        r9c26.send_keys("r9c26")

        # fill r9c27
        r9c27 = browser.find_element_by_name("r9c27")
        r9c27.clear()
        r9c27.send_keys("r9c27")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r10c14
        r10c14 = browser.find_element_by_name("r10c14")
        r10c14.clear()
        r10c14.send_keys("r10c14")

        # fill r10c15
        r10c15 = browser.find_element_by_name("r10c15")
        r10c15.clear()
        r10c15.send_keys("r10c15")

        # fill r10c16
        r10c16 = browser.find_element_by_name("r10c16")
        r10c16.clear()
        r10c16.send_keys("r10c16")

        # fill r10c17
        r10c17 = browser.find_element_by_name("r10c17")
        r10c17.clear()
        r10c17.send_keys("r10c17")

        # fill r10c18
        r10c18 = browser.find_element_by_name("r10c18")
        r10c18.clear()
        r10c18.send_keys("r10c18")

        # fill r10c19
        r10c19 = browser.find_element_by_name("r10c19")
        r10c19.clear()
        r10c19.send_keys("r10c19")

        # fill r10c20
        r10c20 = browser.find_element_by_name("r10c20")
        r10c20.clear()
        r10c20.send_keys("r10c20")

        # fill r10c21
        r10c21 = browser.find_element_by_name("r10c21")
        r10c21.clear()
        r10c21.send_keys("r10c21")

        # fill r10c22
        r10c22 = browser.find_element_by_name("r10c22")
        r10c22.clear()
        r10c22.send_keys("r10c22")

        # fill r10c23
        r10c23 = browser.find_element_by_name("r10c23")
        r10c23.clear()
        r10c23.send_keys("r10c23")

        # fill r10c24
        r10c24 = browser.find_element_by_name("r10c24")
        r10c24.clear()
        r10c24.send_keys("r10c24")

        # fill r10c25
        r10c25 = browser.find_element_by_name("r10c25")
        r10c25.clear()
        r10c25.send_keys("r10c25")

        # fill r10c26
        r10c26 = browser.find_element_by_name("r10c26")
        r10c26.clear()
        r10c26.send_keys("r10c26")

        # fill r10c27
        r10c27 = browser.find_element_by_name("r10c27")
        r10c27.clear()
        r10c27.send_keys("r10c27")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r11c14
        r11c14 = browser.find_element_by_name("r11c14")
        r11c14.clear()
        r11c14.send_keys("r11c14")

        # fill r11c15
        r11c15 = browser.find_element_by_name("r11c15")
        r11c15.clear()
        r11c15.send_keys("r11c15")

        # fill r11c16
        r11c16 = browser.find_element_by_name("r11c16")
        r11c16.clear()
        r11c16.send_keys("r11c16")

        # fill r11c17
        r11c17 = browser.find_element_by_name("r11c17")
        r11c17.clear()
        r11c17.send_keys("r11c17")

        # fill r11c18
        r11c18 = browser.find_element_by_name("r11c18")
        r11c18.clear()
        r11c18.send_keys("r11c18")

        # fill r11c19
        r11c19 = browser.find_element_by_name("r11c19")
        r11c19.clear()
        r11c19.send_keys("r11c19")

        # fill r11c20
        r11c20 = browser.find_element_by_name("r11c20")
        r11c20.clear()
        r11c20.send_keys("r11c20")

        # fill r11c21
        r11c21 = browser.find_element_by_name("r11c21")
        r11c21.clear()
        r11c21.send_keys("r11c21")

        # fill r11c22
        r11c22 = browser.find_element_by_name("r11c22")
        r11c22.clear()
        r11c22.send_keys("r11c22")

        # fill r11c23
        r11c23 = browser.find_element_by_name("r11c23")
        r11c23.clear()
        r11c23.send_keys("r11c23")

        # fill r11c24
        r11c24 = browser.find_element_by_name("r11c24")
        r11c24.clear()
        r11c24.send_keys("r11c24")

        # fill r11c25
        r11c25 = browser.find_element_by_name("r11c25")
        r11c25.clear()
        r11c25.send_keys("r11c25")

        # fill r11c26
        r11c26 = browser.find_element_by_name("r11c26")
        r11c26.clear()
        r11c26.send_keys("r11c26")

        # fill r11c27
        r11c27 = browser.find_element_by_name("r11c27")
        r11c27.clear()
        r11c27.send_keys("r11c27")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r12c14
        r12c14 = browser.find_element_by_name("r12c14")
        r12c14.clear()
        r12c14.send_keys("r12c14")

        # fill r12c15
        r12c15 = browser.find_element_by_name("r12c15")
        r12c15.clear()
        r12c15.send_keys("r12c15")

        # fill r12c16
        r12c16 = browser.find_element_by_name("r12c16")
        r12c16.clear()
        r12c16.send_keys("r12c16")

        # fill r12c17
        r12c17 = browser.find_element_by_name("r12c17")
        r12c17.clear()
        r12c17.send_keys("r12c17")

        # fill r12c18
        r12c18 = browser.find_element_by_name("r12c18")
        r12c18.clear()
        r12c18.send_keys("r12c18")

        # fill r12c19
        r12c19 = browser.find_element_by_name("r12c19")
        r12c19.clear()
        r12c19.send_keys("r12c19")

        # fill r12c20
        r12c20 = browser.find_element_by_name("r12c20")
        r12c20.clear()
        r12c20.send_keys("r12c20")

        # fill r12c21
        r12c21 = browser.find_element_by_name("r12c21")
        r12c21.clear()
        r12c21.send_keys("r12c21")

        # fill r12c22
        r12c22 = browser.find_element_by_name("r12c22")
        r12c22.clear()
        r12c22.send_keys("r12c22")

        # fill r12c23
        r12c23 = browser.find_element_by_name("r12c23")
        r12c23.clear()
        r12c23.send_keys("r12c23")

        # fill r12c24
        r12c24 = browser.find_element_by_name("r12c24")
        r12c24.clear()
        r12c24.send_keys("r12c24")

        # fill r12c25
        r12c25 = browser.find_element_by_name("r12c25")
        r12c25.clear()
        r12c25.send_keys("r12c25")

        # fill r12c26
        r12c26 = browser.find_element_by_name("r12c26")
        r12c26.clear()
        r12c26.send_keys("r12c26")

        # fill r12c27
        r12c27 = browser.find_element_by_name("r12c27")
        r12c27.clear()
        r12c27.send_keys("r12c27")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r13c14
        r13c14 = browser.find_element_by_name("r13c14")
        r13c14.clear()
        r13c14.send_keys("r13c14")

        # fill r13c15
        r13c15 = browser.find_element_by_name("r13c15")
        r13c15.clear()
        r13c15.send_keys("r13c15")

        # fill r13c16
        r13c16 = browser.find_element_by_name("r13c16")
        r13c16.clear()
        r13c16.send_keys("r13c16")

        # fill r13c17
        r13c17 = browser.find_element_by_name("r13c17")
        r13c17.clear()
        r13c17.send_keys("r13c17")

        # fill r13c18
        r13c18 = browser.find_element_by_name("r13c18")
        r13c18.clear()
        r13c18.send_keys("r13c18")

        # fill r13c19
        r13c19 = browser.find_element_by_name("r13c19")
        r13c19.clear()
        r13c19.send_keys("r13c19")

        # fill r13c20
        r13c20 = browser.find_element_by_name("r13c20")
        r13c20.clear()
        r13c20.send_keys("r13c20")

        # fill r13c21
        r13c21 = browser.find_element_by_name("r13c21")
        r13c21.clear()
        r13c21.send_keys("r13c21")

        # fill r13c22
        r13c22 = browser.find_element_by_name("r13c22")
        r13c22.clear()
        r13c22.send_keys("r13c22")

        # fill r13c23
        r13c23 = browser.find_element_by_name("r13c23")
        r13c23.clear()
        r13c23.send_keys("r13c23")

        # fill r13c24
        r13c24 = browser.find_element_by_name("r13c24")
        r13c24.clear()
        r13c24.send_keys("r13c24")

        # fill r13c25
        r13c25 = browser.find_element_by_name("r13c25")
        r13c25.clear()
        r13c25.send_keys("r13c25")

        # fill r13c26
        r13c26 = browser.find_element_by_name("r13c26")
        r13c26.clear()
        r13c26.send_keys("r13c26")

        # fill r13c27
        r13c27 = browser.find_element_by_name("r13c27")
        r13c27.clear()
        r13c27.send_keys("r13c27")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r14c14
        r14c14 = browser.find_element_by_name("r14c14")
        r14c14.clear()
        r14c14.send_keys("r14c14")

        # fill r14c15
        r14c15 = browser.find_element_by_name("r14c15")
        r14c15.clear()
        r14c15.send_keys("r14c15")

        # fill r14c16
        r14c16 = browser.find_element_by_name("r14c16")
        r14c16.clear()
        r14c16.send_keys("r14c16")

        # fill r14c17
        r14c17 = browser.find_element_by_name("r14c17")
        r14c17.clear()
        r14c17.send_keys("r14c17")

        # fill r14c18
        r14c18 = browser.find_element_by_name("r14c18")
        r14c18.clear()
        r14c18.send_keys("r14c18")

        # fill r14c19
        r14c19 = browser.find_element_by_name("r14c19")
        r14c19.clear()
        r14c19.send_keys("r14c19")

        # fill r14c20
        r14c20 = browser.find_element_by_name("r14c20")
        r14c20.clear()
        r14c20.send_keys("r14c20")

        # fill r14c21
        r14c21 = browser.find_element_by_name("r14c21")
        r14c21.clear()
        r14c21.send_keys("r14c21")

        # fill r14c22
        r14c22 = browser.find_element_by_name("r14c22")
        r14c22.clear()
        r14c22.send_keys("r14c22")

        # fill r14c23
        r14c23 = browser.find_element_by_name("r14c23")
        r14c23.clear()
        r14c23.send_keys("r14c23")

        # fill r14c24
        r14c24 = browser.find_element_by_name("r14c24")
        r14c24.clear()
        r14c24.send_keys("r14c24")

        # fill r14c25
        r14c25 = browser.find_element_by_name("r14c25")
        r14c25.clear()
        r14c25.send_keys("r14c25")

        # fill r14c26
        r14c26 = browser.find_element_by_name("r14c26")
        r14c26.clear()
        r14c26.send_keys("r14c26")

        # fill r14c27
        r14c27 = browser.find_element_by_name("r14c27")
        r14c27.clear()
        r14c27.send_keys("r14c27")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r15c14
        r15c14 = browser.find_element_by_name("r15c14")
        r15c14.clear()
        r15c14.send_keys("r15c14")

        # fill r15c15
        r15c15 = browser.find_element_by_name("r15c15")
        r15c15.clear()
        r15c15.send_keys("r15c15")

        # fill r15c16
        r15c16 = browser.find_element_by_name("r15c16")
        r15c16.clear()
        r15c16.send_keys("r15c16")

        # fill r15c17
        r15c17 = browser.find_element_by_name("r15c17")
        r15c17.clear()
        r15c17.send_keys("r15c17")

        # fill r15c18
        r15c18 = browser.find_element_by_name("r15c18")
        r15c18.clear()
        r15c18.send_keys("r15c18")

        # fill r15c19
        r15c19 = browser.find_element_by_name("r15c19")
        r15c19.clear()
        r15c19.send_keys("r15c19")

        # fill r15c20
        r15c20 = browser.find_element_by_name("r15c20")
        r15c20.clear()
        r15c20.send_keys("r15c20")

        # fill r15c21
        r15c21 = browser.find_element_by_name("r15c21")
        r15c21.clear()
        r15c21.send_keys("r15c21")

        # fill r15c22
        r15c22 = browser.find_element_by_name("r15c22")
        r15c22.clear()
        r15c22.send_keys("r15c22")

        # fill r15c23
        r15c23 = browser.find_element_by_name("r15c23")
        r15c23.clear()
        r15c23.send_keys("r15c23")

        # fill r15c24
        r15c24 = browser.find_element_by_name("r15c24")
        r15c24.clear()
        r15c24.send_keys("r15c24")

        # fill r15c25
        r15c25 = browser.find_element_by_name("r15c25")
        r15c25.clear()
        r15c25.send_keys("r15c25")

        # fill r15c26
        r15c26 = browser.find_element_by_name("r15c26")
        r15c26.clear()
        r15c26.send_keys("r15c26")

        # fill r15c27
        r15c27 = browser.find_element_by_name("r15c27")
        r15c27.clear()
        r15c27.send_keys("r15c27")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # fill r16c14
        r16c14 = browser.find_element_by_name("r16c14")
        r16c14.clear()
        r16c14.send_keys("r16c14")

        # fill r16c15
        r16c15 = browser.find_element_by_name("r16c15")
        r16c15.clear()
        r16c15.send_keys("r16c15")

        # fill r16c16
        r16c16 = browser.find_element_by_name("r16c16")
        r16c16.clear()
        r16c16.send_keys("r16c16")

        # fill r16c17
        r16c17 = browser.find_element_by_name("r16c17")
        r16c17.clear()
        r16c17.send_keys("r16c17")

        # fill r16c18
        r16c18 = browser.find_element_by_name("r16c18")
        r16c18.clear()
        r16c18.send_keys("r16c18")

        # fill r16c19
        r16c19 = browser.find_element_by_name("r16c19")
        r16c19.clear()
        r16c19.send_keys("r16c19")

        # fill r16c20
        r16c20 = browser.find_element_by_name("r16c20")
        r16c20.clear()
        r16c20.send_keys("r16c20")

        # fill r16c21
        r16c21 = browser.find_element_by_name("r16c21")
        r16c21.clear()
        r16c21.send_keys("r16c21")

        # fill r16c22
        r16c22 = browser.find_element_by_name("r16c22")
        r16c22.clear()
        r16c22.send_keys("r16c22")

        # fill r16c23
        r16c23 = browser.find_element_by_name("r16c23")
        r16c23.clear()
        r16c23.send_keys("r16c23")

        # fill r16c24
        r16c24 = browser.find_element_by_name("r16c24")
        r16c24.clear()
        r16c24.send_keys("r16c24")

        # fill r16c25
        r16c25 = browser.find_element_by_name("r16c25")
        r16c25.clear()
        r16c25.send_keys("r16c25")

        # fill r16c26
        r16c26 = browser.find_element_by_name("r16c26")
        r16c26.clear()
        r16c26.send_keys("r16c26")

        # fill r16c27
        r16c27 = browser.find_element_by_name("r16c27")
        r16c27.clear()
        r16c27.send_keys("r16c27")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r17c10
        r17c10 = browser.find_element_by_name("r17c10")
        r17c10.clear()
        r17c10.send_keys("r17c10")

        # fill r17c11
        r17c11 = browser.find_element_by_name("r17c11")
        r17c11.clear()
        r17c11.send_keys("r17c11")

        # fill r17c12
        r17c12 = browser.find_element_by_name("r17c12")
        r17c12.clear()
        r17c12.send_keys("r17c12")

        # fill r17c13
        r17c13 = browser.find_element_by_name("r17c13")
        r17c13.clear()
        r17c13.send_keys("r17c13")

        # fill r17c14
        r17c14 = browser.find_element_by_name("r17c14")
        r17c14.clear()
        r17c14.send_keys("r17c14")

        # fill r17c15
        r17c15 = browser.find_element_by_name("r17c15")
        r17c15.clear()
        r17c15.send_keys("r17c15")

        # fill r17c16
        r17c16 = browser.find_element_by_name("r17c16")
        r17c16.clear()
        r17c16.send_keys("r17c16")

        # fill r17c17
        r17c17 = browser.find_element_by_name("r17c17")
        r17c17.clear()
        r17c17.send_keys("r17c17")

        # fill r17c18
        r17c18 = browser.find_element_by_name("r17c18")
        r17c18.clear()
        r17c18.send_keys("r17c18")

        # fill r17c19
        r17c19 = browser.find_element_by_name("r17c19")
        r17c19.clear()
        r17c19.send_keys("r17c19")

        # fill r17c20
        r17c20 = browser.find_element_by_name("r17c20")
        r17c20.clear()
        r17c20.send_keys("r17c20")

        # fill r17c21
        r17c21 = browser.find_element_by_name("r17c21")
        r17c21.clear()
        r17c21.send_keys("r17c21")

        # fill r17c22
        r17c22 = browser.find_element_by_name("r17c22")
        r17c22.clear()
        r17c22.send_keys("r17c22")

        # fill r17c23
        r17c23 = browser.find_element_by_name("r17c23")
        r17c23.clear()
        r17c23.send_keys("r17c23")

        # fill r17c24
        r17c24 = browser.find_element_by_name("r17c24")
        r17c24.clear()
        r17c24.send_keys("r17c24")

        # fill r17c25
        r17c25 = browser.find_element_by_name("r17c25")
        r17c25.clear()
        r17c25.send_keys("r17c25")

        # fill r17c26
        r17c26 = browser.find_element_by_name("r17c26")
        r17c26.clear()
        r17c26.send_keys("r17c26")

        # fill r17c27
        r17c27 = browser.find_element_by_name("r17c27")
        r17c27.clear()
        r17c27.send_keys("r17c27")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r18c10
        r18c10 = browser.find_element_by_name("r18c10")
        r18c10.clear()
        r18c10.send_keys("r18c10")

        # fill r18c11
        r18c11 = browser.find_element_by_name("r18c11")
        r18c11.clear()
        r18c11.send_keys("r18c11")

        # fill r18c12
        r18c12 = browser.find_element_by_name("r18c12")
        r18c12.clear()
        r18c12.send_keys("r18c12")

        # fill r18c13
        r18c13 = browser.find_element_by_name("r18c13")
        r18c13.clear()
        r18c13.send_keys("r18c13")

        # fill r18c14
        r18c14 = browser.find_element_by_name("r18c14")
        r18c14.clear()
        r18c14.send_keys("r18c14")

        # fill r18c15
        r18c15 = browser.find_element_by_name("r18c15")
        r18c15.clear()
        r18c15.send_keys("r18c15")

        # fill r18c16
        r18c16 = browser.find_element_by_name("r18c16")
        r18c16.clear()
        r18c16.send_keys("r18c16")

        # fill r18c17
        r18c17 = browser.find_element_by_name("r18c17")
        r18c17.clear()
        r18c17.send_keys("r18c17")

        # fill r18c18
        r18c18 = browser.find_element_by_name("r18c18")
        r18c18.clear()
        r18c18.send_keys("r18c18")

        # fill r18c19
        r18c19 = browser.find_element_by_name("r18c19")
        r18c19.clear()
        r18c19.send_keys("r18c19")

        # fill r18c20
        r18c20 = browser.find_element_by_name("r18c20")
        r18c20.clear()
        r18c20.send_keys("r18c20")

        # fill r18c21
        r18c21 = browser.find_element_by_name("r18c21")
        r18c21.clear()
        r18c21.send_keys("r18c21")

        # fill r18c22
        r18c22 = browser.find_element_by_name("r18c22")
        r18c22.clear()
        r18c22.send_keys("r18c22")

        # fill r18c23
        r18c23 = browser.find_element_by_name("r18c23")
        r18c23.clear()
        r18c23.send_keys("r18c23")

        # fill r18c24
        r18c24 = browser.find_element_by_name("r18c24")
        r18c24.clear()
        r18c24.send_keys("r18c24")

        # fill r18c25
        r18c25 = browser.find_element_by_name("r18c25")
        r18c25.clear()
        r18c25.send_keys("r18c25")

        # fill r18c26
        r18c26 = browser.find_element_by_name("r18c26")
        r18c26.clear()
        r18c26.send_keys("r18c26")

        # fill r18c27
        r18c27 = browser.find_element_by_name("r18c27")
        r18c27.clear()
        r18c27.send_keys("r18c27")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_twelve_month_marketing_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_twelve_month_marketing_budget(self):
        print("test_generate_html_to_pdf_twelve_month_marketing_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/twelve_month_marketing_budget')
        browser.get('https://holomorphe.com/reporting/twelve_month_marketing_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r11c13
        r11c13 = browser.find_element_by_name("r11c13")
        r11c13.clear()
        r11c13.send_keys("r11c13")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r12c13
        r12c13 = browser.find_element_by_name("r12c13")
        r12c13.clear()
        r12c13.send_keys("r12c13")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r13c13
        r13c13 = browser.find_element_by_name("r13c13")
        r13c13.clear()
        r13c13.send_keys("r13c13")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r14c13
        r14c13 = browser.find_element_by_name("r14c13")
        r14c13.clear()
        r14c13.send_keys("r14c13")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r15c13
        r15c13 = browser.find_element_by_name("r15c13")
        r15c13.clear()
        r15c13.send_keys("r15c13")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r16c13
        r16c13 = browser.find_element_by_name("r16c13")
        r16c13.clear()
        r16c13.send_keys("r16c13")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r17c10
        r17c10 = browser.find_element_by_name("r17c10")
        r17c10.clear()
        r17c10.send_keys("r17c10")

        # fill r17c11
        r17c11 = browser.find_element_by_name("r17c11")
        r17c11.clear()
        r17c11.send_keys("r17c11")

        # fill r17c12
        r17c12 = browser.find_element_by_name("r17c12")
        r17c12.clear()
        r17c12.send_keys("r17c12")

        # fill r17c13
        r17c13 = browser.find_element_by_name("r17c13")
        r17c13.clear()
        r17c13.send_keys("r17c13")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r18c10
        r18c10 = browser.find_element_by_name("r18c10")
        r18c10.clear()
        r18c10.send_keys("r18c10")

        # fill r18c11
        r18c11 = browser.find_element_by_name("r18c11")
        r18c11.clear()
        r18c11.send_keys("r18c11")

        # fill r18c12
        r18c12 = browser.find_element_by_name("r18c12")
        r18c12.clear()
        r18c12.send_keys("r18c12")

        # fill r18c13
        r18c13 = browser.find_element_by_name("r18c13")
        r18c13.clear()
        r18c13.send_keys("r18c13")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_twelve_month_marketing_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_flexible_static_budget_variance(self):
        print("test_generate_html_to_pdf_flexible_static_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/flexible_static_budget_variance')
        browser.get('https://holomorphe.com/reporting/flexible_static_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_flexible_static_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_start_up_budget_variance(self):
        print("test_generate_html_to_pdf_start_up_budget_variance")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/start_up_budget_variance')
        browser.get('https://holomorphe.com/reporting/start_up_budget_variance')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_start_up_budget_variance")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_twelve_month_budget_forecast(self):
        print("test_generate_html_to_pdf_twelve_month_budget_forecast")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/twelve_month_budget_forecast')
        browser.get('https://holomorphe.com/reporting/twelve_month_budget_forecast')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r9c13
        r9c13 = browser.find_element_by_name("r9c13")
        r9c13.clear()
        r9c13.send_keys("r9c13")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r10c13
        r10c13 = browser.find_element_by_name("r10c13")
        r10c13.clear()
        r10c13.send_keys("r10c13")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_twelve_month_budget_forecast")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_annual_budget(self):
        print("test_generate_html_to_pdf_annual_budget")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/annual_budget')
        browser.get('https://holomorphe.com/reporting/annual_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r1c13
        r1c13 = browser.find_element_by_name("r1c13")
        r1c13.clear()
        r1c13.send_keys("r1c13")

        # fill r1c14
        r1c14 = browser.find_element_by_name("r1c14")
        r1c14.clear()
        r1c14.send_keys("r1c14")

        # fill r1c15
        r1c15 = browser.find_element_by_name("r1c15")
        r1c15.clear()
        r1c15.send_keys("r1c15")

        # fill r1c16
        r1c16 = browser.find_element_by_name("r1c16")
        r1c16.clear()
        r1c16.send_keys("r1c16")

        # fill r1c17
        r1c17 = browser.find_element_by_name("r1c17")
        r1c17.clear()
        r1c17.send_keys("r1c17")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r2c13
        r2c13 = browser.find_element_by_name("r2c13")
        r2c13.clear()
        r2c13.send_keys("r2c13")

        # fill r2c14
        r2c14 = browser.find_element_by_name("r2c14")
        r2c14.clear()
        r2c14.send_keys("r2c14")

        # fill r2c15
        r2c15 = browser.find_element_by_name("r2c15")
        r2c15.clear()
        r2c15.send_keys("r2c15")

        # fill r2c16
        r2c16 = browser.find_element_by_name("r2c16")
        r2c16.clear()
        r2c16.send_keys("r2c16")

        # fill r2c17
        r2c17 = browser.find_element_by_name("r2c17")
        r2c17.clear()
        r2c17.send_keys("r2c17")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r3c13
        r3c13 = browser.find_element_by_name("r3c13")
        r3c13.clear()
        r3c13.send_keys("r3c13")

        # fill r3c14
        r3c14 = browser.find_element_by_name("r3c14")
        r3c14.clear()
        r3c14.send_keys("r3c14")

        # fill r3c15
        r3c15 = browser.find_element_by_name("r3c15")
        r3c15.clear()
        r3c15.send_keys("r3c15")

        # fill r3c16
        r3c16 = browser.find_element_by_name("r3c16")
        r3c16.clear()
        r3c16.send_keys("r3c16")

        # fill r3c17
        r3c17 = browser.find_element_by_name("r3c17")
        r3c17.clear()
        r3c17.send_keys("r3c17")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r4c13
        r4c13 = browser.find_element_by_name("r4c13")
        r4c13.clear()
        r4c13.send_keys("r4c13")

        # fill r4c14
        r4c14 = browser.find_element_by_name("r4c14")
        r4c14.clear()
        r4c14.send_keys("r4c14")

        # fill r4c15
        r4c15 = browser.find_element_by_name("r4c15")
        r4c15.clear()
        r4c15.send_keys("r4c15")

        # fill r4c16
        r4c16 = browser.find_element_by_name("r4c16")
        r4c16.clear()
        r4c16.send_keys("r4c16")

        # fill r4c17
        r4c17 = browser.find_element_by_name("r4c17")
        r4c17.clear()
        r4c17.send_keys("r4c17")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r5c13
        r5c13 = browser.find_element_by_name("r5c13")
        r5c13.clear()
        r5c13.send_keys("r5c13")

        # fill r5c14
        r5c14 = browser.find_element_by_name("r5c14")
        r5c14.clear()
        r5c14.send_keys("r5c14")

        # fill r5c15
        r5c15 = browser.find_element_by_name("r5c15")
        r5c15.clear()
        r5c15.send_keys("r5c15")

        # fill r5c16
        r5c16 = browser.find_element_by_name("r5c16")
        r5c16.clear()
        r5c16.send_keys("r5c16")

        # fill r5c17
        r5c17 = browser.find_element_by_name("r5c17")
        r5c17.clear()
        r5c17.send_keys("r5c17")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r6c13
        r6c13 = browser.find_element_by_name("r6c13")
        r6c13.clear()
        r6c13.send_keys("r6c13")

        # fill r6c14
        r6c14 = browser.find_element_by_name("r6c14")
        r6c14.clear()
        r6c14.send_keys("r6c14")

        # fill r6c15
        r6c15 = browser.find_element_by_name("r6c15")
        r6c15.clear()
        r6c15.send_keys("r6c15")

        # fill r6c16
        r6c16 = browser.find_element_by_name("r6c16")
        r6c16.clear()
        r6c16.send_keys("r6c16")

        # fill r6c17
        r6c17 = browser.find_element_by_name("r6c17")
        r6c17.clear()
        r6c17.send_keys("r6c17")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r7c13
        r7c13 = browser.find_element_by_name("r7c13")
        r7c13.clear()
        r7c13.send_keys("r7c13")

        # fill r7c14
        r7c14 = browser.find_element_by_name("r7c14")
        r7c14.clear()
        r7c14.send_keys("r7c14")

        # fill r7c15
        r7c15 = browser.find_element_by_name("r7c15")
        r7c15.clear()
        r7c15.send_keys("r7c15")

        # fill r7c16
        r7c16 = browser.find_element_by_name("r7c16")
        r7c16.clear()
        r7c16.send_keys("r7c16")

        # fill r7c17
        r7c17 = browser.find_element_by_name("r7c17")
        r7c17.clear()
        r7c17.send_keys("r7c17")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r8c13
        r8c13 = browser.find_element_by_name("r8c13")
        r8c13.clear()
        r8c13.send_keys("r8c13")

        # fill r8c14
        r8c14 = browser.find_element_by_name("r8c14")
        r8c14.clear()
        r8c14.send_keys("r8c14")

        # fill r8c15
        r8c15 = browser.find_element_by_name("r8c15")
        r8c15.clear()
        r8c15.send_keys("r8c15")

        # fill r8c16
        r8c16 = browser.find_element_by_name("r8c16")
        r8c16.clear()
        r8c16.send_keys("r8c16")

        # fill r8c17
        r8c17 = browser.find_element_by_name("r8c17")
        r8c17.clear()
        r8c17.send_keys("r8c17")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_annual_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_quarterly_budget(self):
        print("test_generate_html_to_pdf_quarterly_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/quarterly_budget')
        browser.get('https://holomorphe.com/reporting/quarterly_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        # fill r22c6
        r22c6 = browser.find_element_by_name("r22c6")
        r22c6.clear()
        r22c6.send_keys("r22c6")

        # fill r22c7
        r22c7 = browser.find_element_by_name("r22c7")
        r22c7.clear()
        r22c7.send_keys("r22c7")

        # fill r22c8
        r22c8 = browser.find_element_by_name("r22c8")
        r22c8.clear()
        r22c8.send_keys("r22c8")

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        # fill r23c6
        r23c6 = browser.find_element_by_name("r23c6")
        r23c6.clear()
        r23c6.send_keys("r23c6")

        # fill r23c7
        r23c7 = browser.find_element_by_name("r23c7")
        r23c7.clear()
        r23c7.send_keys("r23c7")

        # fill r23c8
        r23c8 = browser.find_element_by_name("r23c8")
        r23c8.clear()
        r23c8.send_keys("r23c8")

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        # fill r24c6
        r24c6 = browser.find_element_by_name("r24c6")
        r24c6.clear()
        r24c6.send_keys("r24c6")

        # fill r24c7
        r24c7 = browser.find_element_by_name("r24c7")
        r24c7.clear()
        r24c7.send_keys("r24c7")

        # fill r24c8
        r24c8 = browser.find_element_by_name("r24c8")
        r24c8.clear()
        r24c8.send_keys("r24c8")

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        # fill r25c4
        r25c4 = browser.find_element_by_name("r25c4")
        r25c4.clear()
        r25c4.send_keys("r25c4")

        # fill r25c5
        r25c5 = browser.find_element_by_name("r25c5")
        r25c5.clear()
        r25c5.send_keys("r25c5")

        # fill r25c6
        r25c6 = browser.find_element_by_name("r25c6")
        r25c6.clear()
        r25c6.send_keys("r25c6")

        # fill r25c7
        r25c7 = browser.find_element_by_name("r25c7")
        r25c7.clear()
        r25c7.send_keys("r25c7")

        # fill r25c8
        r25c8 = browser.find_element_by_name("r25c8")
        r25c8.clear()
        r25c8.send_keys("r25c8")

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        # fill r26c4
        r26c4 = browser.find_element_by_name("r26c4")
        r26c4.clear()
        r26c4.send_keys("r26c4")

        # fill r26c5
        r26c5 = browser.find_element_by_name("r26c5")
        r26c5.clear()
        r26c5.send_keys("r26c5")

        # fill r26c6
        r26c6 = browser.find_element_by_name("r26c6")
        r26c6.clear()
        r26c6.send_keys("r26c6")

        # fill r26c7
        r26c7 = browser.find_element_by_name("r26c7")
        r26c7.clear()
        r26c7.send_keys("r26c7")

        # fill r26c8
        r26c8 = browser.find_element_by_name("r26c8")
        r26c8.clear()
        r26c8.send_keys("r26c8")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_quarterly_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_project_budget(self):
        print("test_generate_html_to_pdf_project_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/project_budget')
        browser.get('https://holomorphe.com/reporting/project_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        # fill r19c9
        r19c9 = browser.find_element_by_name("r19c9")
        r19c9.clear()
        r19c9.send_keys("r19c9")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        # fill r20c9
        r20c9 = browser.find_element_by_name("r20c9")
        r20c9.clear()
        r20c9.send_keys("r20c9")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        # fill r21c9
        r21c9 = browser.find_element_by_name("r21c9")
        r21c9.clear()
        r21c9.send_keys("r21c9")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_project_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_monthly_budget(self):
        print("test_generate_html_to_pdf_monthly_budget")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/monthly_budget')
        browser.get('https://holomorphe.com/reporting/monthly_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        time.sleep(1)

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        time.sleep(1)

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        time.sleep(1)

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        time.sleep(1)

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        time.sleep(1)

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        time.sleep(1)

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        time.sleep(1)

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        time.sleep(1)

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        time.sleep(1)

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        time.sleep(1)

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        time.sleep(1)

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        time.sleep(1)

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        time.sleep(1)

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        time.sleep(1)

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        time.sleep(1)

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        time.sleep(1)

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        time.sleep(1)

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        time.sleep(1)

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        time.sleep(1)

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        time.sleep(1)

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        time.sleep(1)

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        time.sleep(1)

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        time.sleep(1)

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        time.sleep(1)

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        time.sleep(1)

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        time.sleep(1)

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        time.sleep(1)

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        time.sleep(1)

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        time.sleep(1)

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        time.sleep(1)

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        time.sleep(1)

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        time.sleep(1)

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        time.sleep(1)

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        time.sleep(1)

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        time.sleep(1)

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        time.sleep(1)

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        time.sleep(1)

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        time.sleep(1)

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        time.sleep(1)

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        time.sleep(1)

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        time.sleep(1)

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        time.sleep(1)

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        time.sleep(1)

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        time.sleep(1)

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        time.sleep(1)

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        time.sleep(1)

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        time.sleep(1)

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        time.sleep(1)

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        time.sleep(1)

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        time.sleep(1)

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        time.sleep(1)

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        time.sleep(1)

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        time.sleep(1)

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        time.sleep(1)

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        time.sleep(1)

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        time.sleep(1)

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        time.sleep(1)

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        time.sleep(1)

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        time.sleep(1)

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        time.sleep(1)

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        time.sleep(1)

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        time.sleep(1)

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        time.sleep(1)

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        time.sleep(1)

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        time.sleep(1)

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        time.sleep(1)

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        time.sleep(1)

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        time.sleep(1)

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        time.sleep(1)

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        time.sleep(1)

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        time.sleep(1)

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        time.sleep(1)

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        time.sleep(1)

        # fill r25c4
        r25c4 = browser.find_element_by_name("r25c4")
        r25c4.clear()
        r25c4.send_keys("r25c4")

        time.sleep(1)

        # fill r25c5
        r25c5 = browser.find_element_by_name("r25c5")
        r25c5.clear()
        r25c5.send_keys("r25c5")

        time.sleep(1)

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        time.sleep(1)

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        time.sleep(1)

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        time.sleep(1)

        # fill r26c4
        r26c4 = browser.find_element_by_name("r26c4")
        r26c4.clear()
        r26c4.send_keys("r26c4")

        time.sleep(1)

        # fill r26c5
        r26c5 = browser.find_element_by_name("r26c5")
        r26c5.clear()
        r26c5.send_keys("r26c5")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_monthly_budget")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_start_up_budget_calculator(self):
        print("test_generate_html_to_pdf_start_up_budget_calculator")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/start_up_budget_calculator')
        browser.get('https://holomorphe.com/reporting/start_up_budget_calculator')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        time.sleep(1)

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        time.sleep(1)

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        time.sleep(1)

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        time.sleep(1)

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        time.sleep(1)

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        time.sleep(1)

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        time.sleep(1)

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        time.sleep(1)

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        time.sleep(1)

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        time.sleep(1)

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        time.sleep(1)

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        time.sleep(1)

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        time.sleep(1)

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        time.sleep(1)

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        time.sleep(1)

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        time.sleep(1)

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        time.sleep(1)

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        time.sleep(1)

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        time.sleep(1)

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        time.sleep(1)

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        time.sleep(1)

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        time.sleep(1)

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        time.sleep(1)

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        time.sleep(1)

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        time.sleep(1)

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        time.sleep(1)

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        time.sleep(1)

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        time.sleep(1)

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        time.sleep(1)

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        time.sleep(1)

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        time.sleep(1)

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        time.sleep(1)

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        time.sleep(1)

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        time.sleep(1)

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        time.sleep(1)

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        time.sleep(1)

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        time.sleep(1)

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        time.sleep(1)

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        time.sleep(1)

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        time.sleep(1)

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        time.sleep(1)

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        time.sleep(1)

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        time.sleep(1)

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        time.sleep(1)

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        time.sleep(1)

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        time.sleep(1)

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        time.sleep(1)

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        time.sleep(1)

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        time.sleep(1)

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        time.sleep(1)

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        time.sleep(1)

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        time.sleep(1)

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        time.sleep(1)

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        time.sleep(1)

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        time.sleep(1)

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        time.sleep(1)

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        time.sleep(1)

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        time.sleep(1)

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        time.sleep(1)

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        time.sleep(1)

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        time.sleep(1)

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        time.sleep(1)

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        time.sleep(1)

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        time.sleep(1)

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        time.sleep(1)

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        time.sleep(1)

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        time.sleep(1)

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        time.sleep(1)

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        time.sleep(1)

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        time.sleep(1)

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        time.sleep(1)

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        time.sleep(1)

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        time.sleep(1)

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        time.sleep(1)

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        time.sleep(1)

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        time.sleep(1)

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        time.sleep(1)

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        time.sleep(1)

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        time.sleep(1)

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        time.sleep(1)

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        time.sleep(1)

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        time.sleep(1)

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        time.sleep(1)

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        time.sleep(1)

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        time.sleep(1)

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        time.sleep(1)

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        time.sleep(1)

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        time.sleep(1)

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        time.sleep(1)

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        time.sleep(1)

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        time.sleep(1)

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        time.sleep(1)

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        time.sleep(1)

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        time.sleep(1)

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        time.sleep(1)

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        time.sleep(1)

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        time.sleep(1)

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        time.sleep(1)

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        time.sleep(1)

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        time.sleep(1)

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        time.sleep(1)

        # fill r19c9
        r19c9 = browser.find_element_by_name("r19c9")
        r19c9.clear()
        r19c9.send_keys("r19c9")

        time.sleep(1)

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        time.sleep(1)

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        time.sleep(1)

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        time.sleep(1)

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        time.sleep(1)

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        time.sleep(1)

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        time.sleep(1)

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        time.sleep(1)

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        time.sleep(1)

        # fill r20c9
        r20c9 = browser.find_element_by_name("r20c9")
        r20c9.clear()
        r20c9.send_keys("r20c9")

        time.sleep(1)

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        time.sleep(1)

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        time.sleep(1)

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        time.sleep(1)

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        time.sleep(1)

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        time.sleep(1)

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        time.sleep(1)

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        time.sleep(1)

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        time.sleep(1)

        # fill r21c9
        r21c9 = browser.find_element_by_name("r21c9")
        r21c9.clear()
        r21c9.send_keys("r21c9")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_start_up_budget_calculator")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_vendor_service_pricing_sheet(self):
        print("test_generate_html_to_pdf_vendor_service_pricing_sheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/vendor_service_pricing_sheet')
        browser.get('https://holomorphe.com/reporting/vendor_service_pricing_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        time.sleep(1)

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        time.sleep(1)

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        time.sleep(1)

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        time.sleep(1)

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        time.sleep(1)

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        time.sleep(1)

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        time.sleep(1)

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        time.sleep(1)

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        time.sleep(1)

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        time.sleep(1)

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        time.sleep(1)

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        time.sleep(1)

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        time.sleep(1)

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        time.sleep(1)

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        time.sleep(1)

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        time.sleep(1)

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        time.sleep(1)

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        time.sleep(1)

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        time.sleep(1)

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        time.sleep(1)

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        time.sleep(1)

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        time.sleep(1)

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        time.sleep(1)

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        time.sleep(1)

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        time.sleep(1)

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        time.sleep(1)

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        time.sleep(1)

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        time.sleep(1)

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        time.sleep(1)

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        time.sleep(1)

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_vendor_service_pricing_sheet")
        submit.click()

        time.sleep(5)

        browser.quit()
    
    def test_generate_html_to_pdf_management_plan(self):
        print("test_generate_html_to_pdf_management_plan")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/management_plan')
        browser.get('https://holomorphe.com/reporting/management_plan')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_management_plan")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_employee_log_sheet(self):
        print("test_generate_html_to_pdf_employee_log_sheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/employee_log_sheet')
        browser.get('https://holomorphe.com/reporting/employee_log_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_employee_log_sheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_daily_business_log_sheet(self):
        print("test_generate_html_to_pdf_daily_business_log_sheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/daily_business_log_sheet')
        browser.get('https://holomorphe.com/reporting/daily_business_log_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_daily_business_log_sheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_business_goals_worksheet(self):
        print("test_generate_html_to_pdf_business_goals_worksheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/business_goals_worksheet')
        browser.get('https://holomorphe.com/reporting/business_goals_worksheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_business_goals_worksheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_vendor_comparison_worksheet(self):
        print("test_generate_html_to_pdf_vendor_comparison_worksheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/vendor_comparison_worksheet')
        browser.get('https://holomorphe.com/reporting/vendor_comparison_worksheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        time.sleep(1)

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        time.sleep(1)

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        time.sleep(1)

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        time.sleep(1)

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        time.sleep(1)

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        time.sleep(1)

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        time.sleep(1)

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        time.sleep(1)

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        time.sleep(1)

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        time.sleep(1)

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        time.sleep(1)

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        time.sleep(1)

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        time.sleep(1)

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        time.sleep(1)

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        time.sleep(1)

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        time.sleep(1)

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        time.sleep(1)

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        time.sleep(1)

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        time.sleep(1)

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        time.sleep(1)

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        time.sleep(1)

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        time.sleep(1)

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        time.sleep(1)

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        time.sleep(1)

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        time.sleep(1)

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        time.sleep(1)

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_vendor_comparison_worksheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_vendor_product_pricing_sheet(self):
        print("test_generate_html_to_pdf_vendor_product_pricing_sheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/vendor_product_pricing_sheet')
        browser.get('https://holomorphe.com/reporting/vendor_product_pricing_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_vendor_product_pricing_sheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_petty_cash_journal(self):
        print("test_generate_html_to_pdf_petty_cash_journal")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/petty_cash_journal')
        browser.get('https://holomorphe.com/reporting/petty_cash_journal')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_petty_cash_journal")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_vendor_contact_sheet(self):
        print("test_generate_html_to_pdf_vendor_contact_sheet")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/vendor_contact_sheet')
        browser.get('https://holomorphe.com/reporting/vendor_contact_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(1)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(1)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(1)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(1)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(1)

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        time.sleep(1)

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        time.sleep(1)

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        time.sleep(1)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(1)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(1)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(1)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(1)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(1)

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        time.sleep(1)

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        time.sleep(1)

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        time.sleep(1)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(1)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(1)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(1)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(1)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(1)

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        time.sleep(1)

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        time.sleep(1)

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        time.sleep(1)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(1)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(1)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(1)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(1)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(1)

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        time.sleep(1)

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        time.sleep(1)

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        time.sleep(1)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(1)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(1)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(1)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(1)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(1)

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        time.sleep(1)

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        time.sleep(1)

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        time.sleep(1)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(1)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(1)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(1)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(1)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(1)

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        time.sleep(1)

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        time.sleep(1)

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        time.sleep(1)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(1)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(1)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(1)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(1)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(1)

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        time.sleep(1)

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        time.sleep(1)

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        time.sleep(1)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(1)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(1)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(1)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(1)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(1)

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        time.sleep(1)

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        time.sleep(1)

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        time.sleep(1)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(1)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(1)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(1)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(1)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(1)

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        time.sleep(1)

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        time.sleep(1)

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        time.sleep(1)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(1)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(1)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(1)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(1)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(1)

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        time.sleep(1)

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        time.sleep(1)

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        time.sleep(1)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_vendor_contact_sheet")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_operational_budget(self):
        print("test_generate_html_to_pdf_operational_budget")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/operational_budget')
        browser.get('https://holomorphe.com/reporting/operational_budget')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(5)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(5)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(5)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(5)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(5)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(5)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(5)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(5)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(5)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(5)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(5)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(5)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(5)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(5)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(5)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(5)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(5)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(5)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(5)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(5)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(5)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(5)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(5)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(5)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(5)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(5)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(5)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(5)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(5)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(5)

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        time.sleep(5)

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        time.sleep(5)

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        time.sleep(5)

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        time.sleep(5)

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        time.sleep(5)

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        time.sleep(5)

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        time.sleep(5)

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        time.sleep(5)

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        time.sleep(5)

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        time.sleep(5)

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        time.sleep(5)

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        time.sleep(5)

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        time.sleep(5)

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        time.sleep(5)

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        time.sleep(5)

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        time.sleep(5)

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        time.sleep(5)

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        time.sleep(5)

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        time.sleep(5)

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        time.sleep(5)

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        time.sleep(5)

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        time.sleep(5)

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        time.sleep(5)

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        time.sleep(5)

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        time.sleep(5)

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        time.sleep(5)

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        time.sleep(5)

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        time.sleep(5)

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        time.sleep(5)

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        time.sleep(5)

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        time.sleep(5)

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        time.sleep(5)

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        time.sleep(5)

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        time.sleep(5)

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        time.sleep(5)

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        time.sleep(5)

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        time.sleep(5)

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        time.sleep(5)

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        time.sleep(5)

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        time.sleep(5)

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        time.sleep(5)

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        time.sleep(5)

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        time.sleep(5)

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        time.sleep(5)

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        time.sleep(5)

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        time.sleep(5)

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        time.sleep(5)

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        time.sleep(5)

        # fill r27c1
        r27c1 = browser.find_element_by_name("r27c1")
        r27c1.clear()
        r27c1.send_keys("r27c1")

        time.sleep(5)

        # fill r27c2
        r27c2 = browser.find_element_by_name("r27c2")
        r27c2.clear()
        r27c2.send_keys("r27c2")

        time.sleep(5)

        # fill r27c3
        r27c3 = browser.find_element_by_name("r27c3")
        r27c3.clear()
        r27c3.send_keys("r27c3")

        time.sleep(5)

        # fill r28c1
        r28c1 = browser.find_element_by_name("r28c1")
        r28c1.clear()
        r28c1.send_keys("r28c1")

        time.sleep(5)

        # fill r28c2
        r28c2 = browser.find_element_by_name("r28c2")
        r28c2.clear()
        r28c2.send_keys("r28c2")

        time.sleep(5)

        # fill r28c3
        r28c3 = browser.find_element_by_name("r28c3")
        r28c3.clear()
        r28c3.send_keys("r28c3")

        time.sleep(5)

        # fill r29c1
        r29c1 = browser.find_element_by_name("r29c1")
        r29c1.clear()
        r29c1.send_keys("r29c1")

        time.sleep(5)

        # fill r29c2
        r29c2 = browser.find_element_by_name("r29c2")
        r29c2.clear()
        r29c2.send_keys("r29c2")

        time.sleep(5)

        # fill r29c3
        r29c3 = browser.find_element_by_name("r29c3")
        r29c3.clear()
        r29c3.send_keys("r29c3")

        time.sleep(5)

        # fill r30c1
        r30c1 = browser.find_element_by_name("r30c1")
        r30c1.clear()
        r30c1.send_keys("r30c1")

        time.sleep(5)

        # fill r30c2
        r30c2 = browser.find_element_by_name("r30c2")
        r30c2.clear()
        r30c2.send_keys("r30c2")

        time.sleep(5)

        # fill r30c3
        r30c3 = browser.find_element_by_name("r30c3")
        r30c3.clear()
        r30c3.send_keys("r30c3")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_operational_budget")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_physical_inventory_count_sheet(self):
        print("test_generate_html_to_pdf_physical_inventory_count_sheet")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/physical_inventory_count_sheet')
        browser.get('https://holomorphe.com/reporting/physical_inventory_count_sheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        time.sleep(5)

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        time.sleep(5)

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        time.sleep(5)

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        time.sleep(5)

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        time.sleep(5)

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        time.sleep(5)

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        time.sleep(5)

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        time.sleep(5)

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        time.sleep(5)

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        time.sleep(5)

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        time.sleep(5)

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        time.sleep(5)

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        time.sleep(5)

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        time.sleep(5)

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        time.sleep(5)

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        time.sleep(5)

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        time.sleep(5)

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        time.sleep(5)

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        time.sleep(5)

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        time.sleep(5)

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        time.sleep(5)

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        time.sleep(5)

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        time.sleep(5)

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        time.sleep(5)

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        time.sleep(5)

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        time.sleep(5)

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        time.sleep(5)

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        time.sleep(5)

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        time.sleep(5)

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        time.sleep(5)

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        time.sleep(5)

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        time.sleep(5)

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        time.sleep(5)

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        time.sleep(5)

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        time.sleep(5)

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        time.sleep(5)

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        time.sleep(5)

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        time.sleep(5)

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        time.sleep(5)

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        time.sleep(5)

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        time.sleep(5)

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        time.sleep(5)

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        time.sleep(5)

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        time.sleep(5)

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        time.sleep(5)

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        time.sleep(5)

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        time.sleep(5)

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        time.sleep(5)

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        time.sleep(5)

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        time.sleep(5)

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        time.sleep(5)

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        time.sleep(5)

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        time.sleep(5)

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        time.sleep(5)

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        time.sleep(5)

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        time.sleep(5)

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        time.sleep(5)

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        time.sleep(5)

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        time.sleep(5)

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        time.sleep(5)

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        time.sleep(5)

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        time.sleep(5)

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        time.sleep(5)

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        time.sleep(5)

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        time.sleep(5)

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        time.sleep(5)

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        time.sleep(5)

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        time.sleep(5)

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        time.sleep(5)

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        time.sleep(5)

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        time.sleep(5)

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        time.sleep(5)

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        time.sleep(5)

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        time.sleep(5)

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        time.sleep(5)

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        time.sleep(5)

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        time.sleep(5)

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        time.sleep(5)

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        time.sleep(5)

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        time.sleep(5)

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        time.sleep(5)

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        time.sleep(5)

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        time.sleep(5)

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        time.sleep(5)

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        time.sleep(5)

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        time.sleep(5)

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        time.sleep(5)

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        time.sleep(5)

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        time.sleep(5)

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        time.sleep(5)

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        time.sleep(5)

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        time.sleep(5)

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        time.sleep(5)

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        time.sleep(5)

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        time.sleep(5)

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        time.sleep(5)

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        time.sleep(5)

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        time.sleep(5)

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        time.sleep(5)

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        time.sleep(5)

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        time.sleep(5)

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        time.sleep(5)

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        time.sleep(5)

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        time.sleep(5)

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        time.sleep(5)

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        time.sleep(5)

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        time.sleep(5)

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        time.sleep(5)

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        time.sleep(5)

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        time.sleep(5)

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        time.sleep(5)

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        time.sleep(5)

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        time.sleep(5)

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        time.sleep(5)

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        time.sleep(5)

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        time.sleep(5)

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        time.sleep(5)

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        time.sleep(5)

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        time.sleep(5)

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        time.sleep(5)

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        time.sleep(5)

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        time.sleep(5)

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        time.sleep(5)

        # fill r25c4
        r25c4 = browser.find_element_by_name("r25c4")
        r25c4.clear()
        r25c4.send_keys("r25c4")

        time.sleep(5)

        # fill r25c5
        r25c5 = browser.find_element_by_name("r25c5")
        r25c5.clear()
        r25c5.send_keys("r25c5")

        time.sleep(5)

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        time.sleep(5)

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        time.sleep(5)

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        time.sleep(5)

        # fill r26c4
        r26c4 = browser.find_element_by_name("r26c4")
        r26c4.clear()
        r26c4.send_keys("r26c4")

        time.sleep(5)

        # fill r26c5
        r26c5 = browser.find_element_by_name("r26c5")
        r26c5.clear()
        r26c5.send_keys("r26c5")

        time.sleep(5)

        # fill r27c1
        r27c1 = browser.find_element_by_name("r27c1")
        r27c1.clear()
        r27c1.send_keys("r27c1")

        time.sleep(5)

        # fill r27c2
        r27c2 = browser.find_element_by_name("r27c2")
        r27c2.clear()
        r27c2.send_keys("r27c2")

        time.sleep(5)

        # fill r27c3
        r27c3 = browser.find_element_by_name("r27c3")
        r27c3.clear()
        r27c3.send_keys("r27c3")

        time.sleep(5)

        # fill r27c4
        r27c4 = browser.find_element_by_name("r27c4")
        r27c4.clear()
        r27c4.send_keys("r27c4")

        time.sleep(5)

        # fill r27c5
        r27c5 = browser.find_element_by_name("r27c5")
        r27c5.clear()
        r27c5.send_keys("r27c5")

        time.sleep(5)

        # fill r28c1
        r28c1 = browser.find_element_by_name("r28c1")
        r28c1.clear()
        r28c1.send_keys("r28c1")

        time.sleep(5)

        # fill r28c2
        r28c2 = browser.find_element_by_name("r28c2")
        r28c2.clear()
        r28c2.send_keys("r28c2")

        time.sleep(5)

        # fill r28c3
        r28c3 = browser.find_element_by_name("r28c3")
        r28c3.clear()
        r28c3.send_keys("r28c3")

        time.sleep(5)

        # fill r28c4
        r28c4 = browser.find_element_by_name("r28c4")
        r28c4.clear()
        r28c4.send_keys("r28c4")

        time.sleep(5)

        # fill r28c5
        r28c5 = browser.find_element_by_name("r28c5")
        r28c5.clear()
        r28c5.send_keys("r28c5")

        time.sleep(5)

        # fill r29c1
        r29c1 = browser.find_element_by_name("r29c1")
        r29c1.clear()
        r29c1.send_keys("r29c1")

        time.sleep(5)

        # fill r29c2
        r29c2 = browser.find_element_by_name("r29c2")
        r29c2.clear()
        r29c2.send_keys("r29c2")

        time.sleep(5)

        # fill r29c3
        r29c3 = browser.find_element_by_name("r29c3")
        r29c3.clear()
        r29c3.send_keys("r29c3")

        time.sleep(5)

        # fill r29c4
        r29c4 = browser.find_element_by_name("r29c4")
        r29c4.clear()
        r29c4.send_keys("r29c4")

        time.sleep(5)

        # fill r29c5
        r29c5 = browser.find_element_by_name("r29c5")
        r29c5.clear()
        r29c5.send_keys("r29c5")

        time.sleep(5)

        # fill r30c1
        r30c1 = browser.find_element_by_name("r30c1")
        r30c1.clear()
        r30c1.send_keys("r30c1")

        time.sleep(5)

        # fill r30c2
        r30c2 = browser.find_element_by_name("r30c2")
        r30c2.clear()
        r30c2.send_keys("r30c2")

        time.sleep(5)

        # fill r30c3
        r30c3 = browser.find_element_by_name("r30c3")
        r30c3.clear()
        r30c3.send_keys("r30c3")

        time.sleep(5)

        # fill r30c4
        r30c4 = browser.find_element_by_name("r30c4")
        r30c4.clear()
        r30c4.send_keys("r30c4")

        time.sleep(5)

        # fill r30c5
        r30c5 = browser.find_element_by_name("r30c5")
        r30c5.clear()
        r30c5.send_keys("r30c5")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_physical_inventory_count_sheet")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_fund_sources_and_uses(self):
        print("test_generate_html_to_pdf_fund_sources_and_uses")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/fund_sources_and_uses')
        browser.get('https://holomorphe.com/reporting/fund_sources_and_uses')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill line_of_credit
        line_of_credit = browser.find_element_by_name("line_of_credit")
        line_of_credit.clear()
        line_of_credit.send_keys("line_of_credit")

        time.sleep(5)

        # fill outside_equity
        outside_equity = browser.find_element_by_name("outside_equity")
        outside_equity.clear()
        outside_equity.send_keys("outside_equity")

        time.sleep(5)

        # fill personal_equity
        personal_equity = browser.find_element_by_name("personal_equity")
        personal_equity.clear()
        personal_equity.send_keys("personal_equity")

        time.sleep(5)

        # fill term_loan
        term_loan = browser.find_element_by_name("term_loan")
        term_loan.clear()
        term_loan.send_keys("term_loan")

        time.sleep(5)

        # fill other
        other = browser.find_element_by_name("other")
        other.clear()
        other.send_keys("other")

        time.sleep(5)

        # fill total_sources
        total_sources = browser.find_element_by_name("total_sources")
        total_sources.clear()
        total_sources.send_keys("total_sources")

        time.sleep(5)

        # fill cash_reserve
        cash_reserve = browser.find_element_by_name("cash_reserve")
        cash_reserve.clear()
        cash_reserve.send_keys("cash_reserve")

        time.sleep(5)

        # fill inventory
        inventory = browser.find_element_by_name("inventory")
        inventory.clear()
        inventory.send_keys("inventory")

        time.sleep(5)

        # fill purchase_building
        purchase_building = browser.find_element_by_name("purchase_building")
        purchase_building.clear()
        purchase_building.send_keys("purchase_building")

        time.sleep(5)

        # fill purchase_equipment
        purchase_equipment = browser.find_element_by_name("purchase_equipment")
        purchase_equipment.clear()
        purchase_equipment.send_keys("purchase_equipment")

        time.sleep(5)

        # fill renovations
        renovations = browser.find_element_by_name("renovations")
        renovations.clear()
        renovations.send_keys("renovations")

        time.sleep(5)

        # fill working_capital
        working_capital = browser.find_element_by_name("working_capital")
        working_capital.clear()
        working_capital.send_keys("working_capital")

        time.sleep(5)

        # fill other
        other = browser.find_element_by_name("other")
        other.clear()
        other.send_keys("other")

        time.sleep(5)

        # fill total_uses
        total_uses = browser.find_element_by_name("total_uses")
        total_uses.clear()
        total_uses.send_keys("total_uses")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_fund_sources_and_uses")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_marketing_plan(self):
        print("test_generate_html_to_pdf_marketing_plan")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/marketing_plan')
        browser.get('https://holomorphe.com/reporting/marketing_plan')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill program_or_activity
        program_or_activity = browser.find_element_by_name("program_or_activity")
        program_or_activity.clear()
        program_or_activity.send_keys("program_or_activity")

        time.sleep(5)

        # fill month
        month = browser.find_element_by_name("month")
        month.clear()
        month.send_keys("month")

        time.sleep(5)

        # fill budget
        budget = browser.find_element_by_name("budget")
        budget.clear()
        budget.send_keys("budget")

        time.sleep(5)

        # fill deadline
        deadline = browser.find_element_by_name("deadline")
        deadline.clear()
        deadline.send_keys("deadline")

        time.sleep(5)

        # fill response
        response = browser.find_element_by_name("response")
        response.clear()
        response.send_keys("response")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_marketing_plan")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_product_service_worksheet(self):
        print("test_generate_html_to_pdf_product_service_worksheet")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/product_service_worksheet')
        # browser.get('https://holomorphe.com/reporting/product_service_worksheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill product_or_service
        product_or_service = browser.find_element_by_name("product_or_service")
        product_or_service.clear()
        product_or_service.send_keys("product_or_service")

        time.sleep(5)

        # fill description
        description = browser.find_element_by_name("description")
        description.clear()
        description.send_keys("description")

        time.sleep(5)

        # fill marketing_period_or_season
        marketing_period_or_season = browser.find_element_by_name("marketing_period_or_season")
        marketing_period_or_season.clear()
        marketing_period_or_season.send_keys("marketing_period_or_season")

        time.sleep(5)

        # fill target_demographic
        target_demographic = browser.find_element_by_name("target_demographic")
        target_demographic.clear()
        target_demographic.send_keys("target_demographic")

        time.sleep(5)

        # fill materials
        materials = browser.find_element_by_name("materials")
        materials.clear()
        materials.send_keys("materials")

        time.sleep(5)

        # fill productions_steps
        productions_steps = browser.find_element_by_name("productions_steps")
        productions_steps.clear()
        productions_steps.send_keys("productions_steps")

        time.sleep(5)

        # fill variations
        variations = browser.find_element_by_name("variations")
        variations.clear()
        variations.send_keys("variations")

        time.sleep(5)

        # fill quality
        quality = browser.find_element_by_name("quality")
        quality.clear()
        quality.send_keys("quality")

        time.sleep(5)

        # fill cost
        cost = browser.find_element_by_name("cost")
        cost.clear()
        cost.send_keys("cost")

        time.sleep(5)

        # fill price
        price = browser.find_element_by_name("price")
        price.clear()
        price.send_keys("price")

        time.sleep(5)

        # fill instructions
        instructions = browser.find_element_by_name("instructions")
        instructions.clear()
        instructions.send_keys("instructions")

        time.sleep(5)

        # fill packaging
        packaging = browser.find_element_by_name("packaging")
        packaging.clear()
        packaging.send_keys("packaging")

        time.sleep(5)

        # fill shipment
        shipment = browser.find_element_by_name("shipment")
        shipment.clear()
        shipment.send_keys("shipment")

        time.sleep(5)

        # fill staff_required
        staff_required = browser.find_element_by_name("staff_required")
        staff_required.clear()
        staff_required.send_keys("staff_required")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_product_service_worksheet")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_target_market_worksheet(self):
        print("test_generate_html_to_pdf_target_market_worksheet")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        # browser.get('http://127.0.0.1:8000/reporting/target_market_worksheet')
        browser.get('https://holomorphe.com/reporting/target_market_worksheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill concept
        concept = browser.find_element_by_name("concept")
        concept.clear()
        concept.send_keys("concept")

        time.sleep(5)

        # fill concept_use
        concept_use = browser.find_element_by_name("concept_use")
        concept_use.clear()
        concept_use.send_keys("concept_use")

        time.sleep(5)

        # fill projected_demographic
        projected_demographic = browser.find_element_by_name("projected_demographic")
        projected_demographic.clear()
        projected_demographic.send_keys("projected_demographic")

        time.sleep(5)

        # fill recreation_location
        recreation_location = browser.find_element_by_name("recreation_location")
        recreation_location.clear()
        recreation_location.send_keys("recreation_location")

        time.sleep(5)

        # fill shopping_location
        shopping_location = browser.find_element_by_name("shopping_location")
        shopping_location.clear()
        shopping_location.send_keys("shopping_location")

        time.sleep(5)

        # fill residential_location
        residential_location = browser.find_element_by_name("residential_location")
        residential_location.clear()
        residential_location.send_keys("residential_location")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_target_market_worksheet")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_business_requirement_document(self):
        print("test_generate_html_to_pdf_business_requirement_document")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/business_requirement_document')
        # browser.get('https://holomorphe.com/reporting/business_requirement_document')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill objectives
        objectives = browser.find_element_by_name("objectives")
        objectives.clear()
        objectives.send_keys("objectives")

        time.sleep(5)

        # fill scope
        scope = browser.find_element_by_name("scope")
        scope.clear()
        scope.send_keys("scope")

        time.sleep(5)

        # fill features
        features = browser.find_element_by_name("features")
        features.clear()
        features.send_keys("features")

        time.sleep(5)

        # fill requirements
        requirements = browser.find_element_by_name("requirements")
        requirements.clear()
        requirements.send_keys("requirements")

        time.sleep(5)

        # fill personnel
        personnel = browser.find_element_by_name("personnel")
        personnel.clear()
        personnel.send_keys("personnel")

        time.sleep(5)

        # fill quality_control
        quality_control = browser.find_element_by_name("quality_control")
        quality_control.clear()
        quality_control.send_keys("quality_control")

        time.sleep(5)

        # fill timeline
        timeline = browser.find_element_by_name("timeline")
        timeline.clear()
        timeline.send_keys("timeline")

        time.sleep(5)

        # fill other
        other = browser.find_element_by_name("other")
        other.clear()
        other.send_keys("other")

        time.sleep(5)

        # fill assumptions
        assumptions = browser.find_element_by_name("assumptions")
        assumptions.clear()
        assumptions.send_keys("assumptions")

        time.sleep(5)

        # fill limitations
        limitations = browser.find_element_by_name("limitations")
        limitations.clear()
        limitations.send_keys("limitations")

        time.sleep(5)

        # fill risks
        risks = browser.find_element_by_name("risks")
        risks.clear()
        risks.send_keys("risks")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_business_requirement_document")
        submit.click()

        # browser.quit()

    def test_generate_html_to_pdf_swot_analysis(self):
        print("test_generate_html_to_pdf_swot_analysis")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/swot_analysis')
        # browser.get('https://holomorphe.com/reporting/swot_analysis')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill good_internal_strengths
        good_internal_strengths = browser.find_element_by_name("good_internal_strengths")
        good_internal_strengths.clear()
        good_internal_strengths.send_keys("good_internal_strengths")

        time.sleep(5)

        # fill bad_internal_weaknesses
        bad_internal_weaknesses = browser.find_element_by_name("bad_internal_weaknesses")
        bad_internal_weaknesses.clear()
        bad_internal_weaknesses.send_keys("bad_internal_weaknesses")

        time.sleep(5)

        # fill external_opportunities
        external_opportunities = browser.find_element_by_name("external_opportunities")
        external_opportunities.clear()
        external_opportunities.send_keys("external_opportunities")

        time.sleep(5)

        # fill external_threats
        external_threats = browser.find_element_by_name("external_threats")
        external_threats.clear()
        external_threats.send_keys("external_threats")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_swot_analysis")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_operational_plan(self):
        print("test_generate_html_to_pdf_operational_plan")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/operational_plan')
        # browser.get('https://holomorphe.com/reporting/operational_plan')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill goals
        goals = browser.find_element_by_name("goals")
        goals.clear()
        goals.send_keys("goals")

        time.sleep(5)

        # fill strategy
        strategy = browser.find_element_by_name("strategy")
        strategy.clear()
        strategy.send_keys("strategy")

        time.sleep(5)

        # fill program_activity
        program_activity = browser.find_element_by_name("program_activity")
        program_activity.clear()
        program_activity.send_keys("program_activity")

        time.sleep(5)

        # fill start_time_frame
        start_time_frame = browser.find_element_by_name("start_time_frame")
        start_time_frame.clear()
        start_time_frame.send_keys("start_time_frame")

        time.sleep(5)

        # fill end_time_frame
        end_time_frame = browser.find_element_by_name("end_time_frame")
        end_time_frame.clear()
        end_time_frame.send_keys("end_time_frame")

        time.sleep(5)

        # fill teams
        teams = browser.find_element_by_name("teams")
        teams.clear()
        teams.send_keys("teams")

        time.sleep(5)

        # fill internal_partners
        internal_partners = browser.find_element_by_name("internal_partners")
        internal_partners.clear()
        internal_partners.send_keys("internal_partners")

        time.sleep(5)

        # fill external_partners
        external_partners = browser.find_element_by_name("external_partners")
        external_partners.clear()
        external_partners.send_keys("external_partners")

        time.sleep(5)

        # fill required_resources
        required_resources = browser.find_element_by_name("required_resources")
        required_resources.clear()
        required_resources.send_keys("required_resources")

        time.sleep(5)

        # fill actual_resources
        actual_resources = browser.find_element_by_name("actual_resources")
        actual_resources.clear()
        actual_resources.send_keys("actual_resources")

        time.sleep(5)

        # fill targets
        targets = browser.find_element_by_name("targets")
        targets.clear()
        targets.send_keys("targets")

        time.sleep(5)

        # fill immediate_impact
        immediate_impact = browser.find_element_by_name("immediate_impact")
        immediate_impact.clear()
        immediate_impact.send_keys("immediate_impact")

        time.sleep(5)

        # fill data_sources
        data_sources = browser.find_element_by_name("data_sources")
        data_sources.clear()
        data_sources.send_keys("data_sources")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_operational_plan")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_competitor_worksheet(self):
        print("test_generate_html_to_pdf_competitor_worksheet")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/competitor_worksheet')
        # browser.get('https://holomorphe.com/reporting/competitor_worksheet')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill name_of_competitors
        name_of_competitors = browser.find_element_by_name("name_of_competitors")
        name_of_competitors.clear()
        name_of_competitors.send_keys("name_of_competitors")

        time.sleep(5)

        # fill location
        location = browser.find_element_by_name("location")
        location.clear()
        location.send_keys("location")

        time.sleep(5)

        # fill products_or_services_offered
        products_or_services_offered = browser.find_element_by_name("products_or_services_offered")
        products_or_services_offered.clear()
        products_or_services_offered.send_keys("products_or_services_offered")

        time.sleep(5)

        # fill methods_of_distribution
        methods_of_distribution = browser.find_element_by_name("methods_of_distribution")
        methods_of_distribution.clear()
        methods_of_distribution.send_keys("methods_of_distribution")

        time.sleep(5)

        # fill packaging
        packaging = browser.find_element_by_name("packaging")
        packaging.clear()
        packaging.send_keys("packaging")

        time.sleep(5)

        # fill promotional_materials
        promotional_materials = browser.find_element_by_name("promotional_materials")
        promotional_materials.clear()
        promotional_materials.send_keys("promotional_materials")

        time.sleep(5)

        # fill methods_of_advertising
        methods_of_advertising = browser.find_element_by_name("methods_of_advertising")
        methods_of_advertising.clear()
        methods_of_advertising.send_keys("methods_of_advertising")

        time.sleep(5)

        # fill positioning
        positioning = browser.find_element_by_name("positioning")
        positioning.clear()
        positioning.send_keys("positioning")

        time.sleep(5)

        # fill pricing_structure
        pricing_structure = browser.find_element_by_name("pricing_structure")
        pricing_structure.clear()
        pricing_structure.send_keys("pricing_structure")

        time.sleep(5)

        # fill performance
        performance = browser.find_element_by_name("performance")
        performance.clear()
        performance.send_keys("performance")

        time.sleep(5)

        # fill market_share
        market_share = browser.find_element_by_name("market_share")
        market_share.clear()
        market_share.send_keys("market_share")

        time.sleep(5)

        # fill strengths
        strengths = browser.find_element_by_name("strengths")
        strengths.clear()
        strengths.send_keys("strengths")

        time.sleep(5)

        # fill weaknesses
        weaknesses = browser.find_element_by_name("weaknesses")
        weaknesses.clear()
        weaknesses.send_keys("weaknesses")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_competitor_worksheet")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_business_plan_cleaning_services(self):
        print("test_generate_html_to_pdf_business_plan_cleaning_services")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('http://127.0.0.1:8000/reporting/business_plan_cleaning_services')
        # browser.get('https://holomorphe.com/reporting/business_plan_cleaning_services')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill executive_summary
        executive_summary = browser.find_element_by_name("executive_summary")
        executive_summary.clear()
        executive_summary.send_keys("executive_summary")

        time.sleep(5)

        # fill objectives
        objectives = browser.find_element_by_name("objectives")
        objectives.clear()
        objectives.send_keys("objectives")

        time.sleep(5)

        # fill mission
        mission = browser.find_element_by_name("mission")
        mission.clear()
        mission.send_keys("mission")

        time.sleep(5)

        # fill keys_to_success
        keys_to_success = browser.find_element_by_name("keys_to_success")
        keys_to_success.clear()
        keys_to_success.send_keys("keys_to_success")

        time.sleep(5)

        # fill company_summary
        company_summary = browser.find_element_by_name("company_summary")
        company_summary.clear()
        company_summary.send_keys("company_summary")

        time.sleep(5)

        # fill company_ownership
        company_ownership = browser.find_element_by_name("company_ownership")
        company_ownership.clear()
        company_ownership.send_keys("company_ownership")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_business_plan_cleaning_services")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_value_proposition_canvas(self):
        print("test_generate_html_to_pdf_value_proposition_canvas")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://holomorphe.com/reporting/value_proposition_canvas')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill gain_creators
        gain_creators = browser.find_element_by_name("gain_creators")
        gain_creators.clear()
        gain_creators.send_keys("gain_creators")

        time.sleep(5)

        # fill pain_relievers
        pain_relievers = browser.find_element_by_name("pain_relievers")
        pain_relievers.clear()
        pain_relievers.send_keys("pain_relievers")

        time.sleep(5)

        # fill product_and_services
        product_and_services = browser.find_element_by_name("product_and_services")
        product_and_services.clear()
        product_and_services.send_keys("product_and_services")

        time.sleep(5)

        # fill gains
        gains = browser.find_element_by_name("gains")
        gains.clear()
        gains.send_keys("gains")

        time.sleep(5)

        # fill pains
        pains = browser.find_element_by_name("pains")
        pains.clear()
        pains.send_keys("pains")

        time.sleep(5)

        # fill customer_jobs
        customer_jobs = browser.find_element_by_name("customer_jobs")
        customer_jobs.clear()
        customer_jobs.send_keys("customer_jobs")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_value_proposition_canvas")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_business_model_canvas(self):
        print("test_generate_html_to_pdf_business_model_canvas")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open business model canvas report
        browser.get('https://www.holomorphe.com/reporting/business_model_canvas')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")

        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")

        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")

        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")

        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")

        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")

        time.sleep(5)

        # fill key_partners
        key_partners = browser.find_element_by_name("key_partners")
        key_partners.clear()
        key_partners.send_keys("key_partners")

        time.sleep(5)

        # fill key_activities
        key_activities = browser.find_element_by_name("key_activities")
        key_activities.clear()
        key_activities.send_keys("key_activities")

        time.sleep(5)

        # fill key_resources
        key_resources = browser.find_element_by_name("key_resources")
        key_resources.clear()
        key_resources.send_keys("key_resources")

        time.sleep(5)

        # fill value_propositions
        value_propositions = browser.find_element_by_name("value_propositions")
        value_propositions.clear()
        value_propositions.send_keys("value_propositions")

        time.sleep(5)

        # fill customer_relationships
        customer_relationships = browser.find_element_by_name("customer_relationships")
        customer_relationships.clear()
        customer_relationships.send_keys("customer_relationships")

        time.sleep(5)

        # fill channels
        channels = browser.find_element_by_name("channels")
        channels.clear()
        channels.send_keys("channels")

        time.sleep(5)

        # fill customer_segments
        customer_segments = browser.find_element_by_name("customer_segments")
        customer_segments.clear()
        customer_segments.send_keys("customer_segments")

        time.sleep(5)

        # fill cost_structure
        cost_structure = browser.find_element_by_name("cost_structure")
        cost_structure.clear()
        cost_structure.send_keys("cost_structure")

        time.sleep(5)

        # fill revenue_streams
        revenue_streams = browser.find_element_by_name("revenue_streams")
        revenue_streams.clear()
        revenue_streams.send_keys("revenue_streams")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_business_model_canvas")
        submit.click()

        time.sleep(10)

    def test_generate_html_to_pdf_business_plan(self):
        print("test_generate_html_to_pdf_business_plan")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/business_plan')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")

        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill executive_summary
        executive_summary = browser.find_element_by_name("executive_summary")
        executive_summary.clear()
        executive_summary.send_keys("executive_summary")
        time.sleep(5)

        # fill mission_statement
        mission_statement = browser.find_element_by_name("mission_statement")
        mission_statement.clear()
        mission_statement.send_keys("mission_statement")
        time.sleep(5)

        # fill business_description
        business_description = browser.find_element_by_name("business_description")
        business_description.clear()
        business_description.send_keys("business_description")
        time.sleep(5)

        # fill business_environment_analysis
        business_environment_analysis = browser.find_element_by_name("business_environment_analysis")
        business_environment_analysis.clear()
        business_environment_analysis.send_keys("business_environment_analysis")
        time.sleep(5)

        # fill swot_analysis
        swot_analysis = browser.find_element_by_name("swot_analysis")
        swot_analysis.clear()
        swot_analysis.send_keys("swot_analysis")
        time.sleep(5)

        # fill industry_background
        industry_background = browser.find_element_by_name("industry_background")
        industry_background.clear()
        industry_background.send_keys("industry_background")
        time.sleep(5)

        # fill competitor_analysis
        competitor_analysis = browser.find_element_by_name("competitor_analysis")
        competitor_analysis.clear()
        competitor_analysis.send_keys("competitor_analysis")
        time.sleep(5)

        # fill market_analysis
        market_analysis = browser.find_element_by_name("market_analysis")
        market_analysis.clear()
        market_analysis.send_keys("market_analysis")
        time.sleep(5)

        # fill marketing_plan
        marketing_plan = browser.find_element_by_name("marketing_plan")
        marketing_plan.clear()
        marketing_plan.send_keys("marketing_plan")
        time.sleep(5)

        # fill operations_plan
        operations_plan = browser.find_element_by_name("operations_plan")
        operations_plan.clear()
        operations_plan.send_keys("operations_plan")
        time.sleep(5)

        # fill management_summary
        management_summary = browser.find_element_by_name("management_summary")
        management_summary.clear()
        management_summary.send_keys("management_summary")
        time.sleep(5)

        # fill financial_plan
        financial_plan = browser.find_element_by_name("financial_plan")
        financial_plan.clear()
        financial_plan.send_keys("financial_plan")
        time.sleep(5)

        # fill achievements_and_milestones
        achievements_and_milestones = browser.find_element_by_name("achievements_and_milestones")
        achievements_and_milestones.clear()
        achievements_and_milestones.send_keys("achievements_and_milestones")
        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_business_plan")
        submit.click()
        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_use_case_form(self):
        print("test_generate_html_to_pdf_use_case_form")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/use_case_form')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill use_case_id
        use_case_id = browser.find_element_by_name("use_case_id")
        use_case_id.clear()
        use_case_id.send_keys("use_case_id")

        time.sleep(5)

        # fill use_case
        use_case = browser.find_element_by_name("use_case")
        use_case.clear()
        use_case.send_keys("use_case")

        time.sleep(5)

        # fill elaboration_phase
        elaboration_phase = browser.find_element_by_name("elaboration_phase")
        elaboration_phase.clear()
        elaboration_phase.send_keys("elaboration_phase")

        time.sleep(5)

        # fill actors
        actors = browser.find_element_by_name("actors")
        actors.clear()
        actors.send_keys("actors")

        time.sleep(5)

        # fill description
        description = browser.find_element_by_name("description")
        description.clear()
        description.send_keys("description")

        time.sleep(5)

        # fill priority
        priority = browser.find_element_by_name("priority")
        priority.clear()
        priority.send_keys("priority")

        time.sleep(5)

        # fill non_functional_requirements
        non_functional_requirements = browser.find_element_by_name("non_functional_requirements")
        non_functional_requirements.clear()
        non_functional_requirements.send_keys("non_functional_requirements")

        time.sleep(5)

        # fill assumptions
        assumptions = browser.find_element_by_name("assumptions")
        assumptions.clear()
        assumptions.send_keys("assumptions")

        time.sleep(5)

        # fill source
        source = browser.find_element_by_name("source")
        source.clear()
        source.send_keys("source")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_use_case_form")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_kanban_board(self):
        print("test_generate_html_to_pdf_kanban_board")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/kanban_board')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill backlog
        backlog = browser.find_element_by_name("backlog")
        backlog.clear()
        backlog.send_keys("backlog")

        time.sleep(5)

        # fill to_do
        to_do = browser.find_element_by_name("to_do")
        to_do.clear()
        to_do.send_keys("to_do")

        time.sleep(5)

        # fill in_progress
        in_progress = browser.find_element_by_name("in_progress")
        in_progress.clear()
        in_progress.send_keys("in_progress")

        time.sleep(5)

        # fill done
        done = browser.find_element_by_name("done")
        done.clear()
        done.send_keys("done")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_kanban_board")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_gap_analysis(self):
        print("test_generate_html_to_pdf_gap_analysis")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/gap_analysis')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill category
        category = browser.find_element_by_name("category")
        category.clear()
        category.send_keys("category")

        time.sleep(5)

        # fill current_state
        current_state = browser.find_element_by_name("current_state")
        current_state.clear()
        current_state.send_keys("current_state")

        time.sleep(5)

        # fill goal_state
        goal_state = browser.find_element_by_name("goal_state")
        goal_state.clear()
        goal_state.send_keys("goal_state")

        time.sleep(5)

        # fill gap
        gap = browser.find_element_by_name("gap")
        gap.clear()
        gap.send_keys("gap")

        time.sleep(5)

        # fill action_plan
        action_plan = browser.find_element_by_name("action_plan")
        action_plan.clear()
        action_plan.send_keys("action_plan")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_gap_analysis")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_job_analysis(self):
        print("test_generate_html_to_pdf_job_analysis")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/job_analysis')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill title
        title = browser.find_element_by_name("title")
        title.clear()
        title.send_keys("title")

        time.sleep(5)

        # fill position
        position = browser.find_element_by_name("position")
        position.clear()
        position.send_keys("position")

        time.sleep(5)

        # fill supervisor
        supervisor = browser.find_element_by_name("supervisor")
        supervisor.clear()
        supervisor.send_keys("supervisor")

        time.sleep(5)

        # fill employee
        employee = browser.find_element_by_name("employee")
        employee.clear()
        employee.send_keys("employee")

        time.sleep(5)

        # fill frequent_major_duties
        frequent_major_duties = browser.find_element_by_name("frequent_major_duties")
        frequent_major_duties.clear()
        frequent_major_duties.send_keys("frequent_major_duties")

        time.sleep(5)

        # fill infrequent_major_duties
        infrequent_major_duties = browser.find_element_by_name("infrequent_major_duties")
        infrequent_major_duties.clear()
        infrequent_major_duties.send_keys("infrequent_major_duties")

        time.sleep(5)

        # fill essential_responsibilities
        essential_responsibilities = browser.find_element_by_name("essential_responsibilities")
        essential_responsibilities.clear()
        essential_responsibilities.send_keys("essential_responsibilities")

        time.sleep(5)

        # fill non_essential_responsibilities
        non_essential_responsibilities = browser.find_element_by_name("non_essential_responsibilities")
        non_essential_responsibilities.clear()
        non_essential_responsibilities.send_keys("non_essential_responsibilities")

        time.sleep(5)

        # fill school_type
        school_type = browser.find_element_by_name("school_type")
        school_type.clear()
        school_type.send_keys("school_type")

        time.sleep(5)

        # fill degree
        degree = browser.find_element_by_name("degree")
        degree.clear()
        degree.send_keys("degree")

        time.sleep(5)

        # fill classes
        classes = browser.find_element_by_name("classes")
        classes.clear()
        classes.send_keys("classes")

        time.sleep(5)

        # fill workshops
        workshops = browser.find_element_by_name("workshops")
        workshops.clear()
        workshops.send_keys("workshops")

        time.sleep(5)

        # fill technical_skills
        technical_skills = browser.find_element_by_name("technical_skills")
        technical_skills.clear()
        technical_skills.send_keys("technical_skills")

        time.sleep(5)

        # fill tool_skills
        tool_skills = browser.find_element_by_name("tool_skills")
        tool_skills.clear()
        tool_skills.send_keys("tool_skills")

        time.sleep(5)

        # fill equipment_skills
        equipment_skills = browser.find_element_by_name("equipment_skills")
        equipment_skills.clear()
        equipment_skills.send_keys("equipment_skills")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_job_analysis")
        submit.click()

        time.sleep(10)

        browser.quit()

    def test_generate_html_to_pdf_pricing_strategy(self):
        print("test_generate_html_to_pdf_pricing_strategy")

        time.sleep(5)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(5)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(5)

        # maximize window
        browser.maximize_window()

        time.sleep(5)

        # open the report
        browser.get('https://www.holomorphe.com/reporting/pricing_strategy')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(5)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(5)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(5)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(5)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(5)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(5)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(5)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(5)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(5)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(5)

        # fill item_cost
        item_cost = browser.find_element_by_name("item_cost")
        item_cost.clear()
        item_cost.send_keys("item_cost")

        time.sleep(5)

        # fill labor
        labor = browser.find_element_by_name("labor")
        labor.clear()
        labor.send_keys("labor")

        time.sleep(5)

        # fill materials
        materials = browser.find_element_by_name("materials")
        materials.clear()
        materials.send_keys("materials")

        time.sleep(5)

        # fill utilities
        utilities = browser.find_element_by_name("utilities")
        utilities.clear()
        utilities.send_keys("utilities")

        time.sleep(5)

        # fill equipment_depreciation
        equipment_depreciation = browser.find_element_by_name("equipment_depreciation")
        equipment_depreciation.clear()
        equipment_depreciation.send_keys("equipment_depreciation")

        time.sleep(5)

        # fill advertising
        advertising = browser.find_element_by_name("advertising")
        advertising.clear()
        advertising.send_keys("advertising")

        time.sleep(5)

        # fill packaging
        packaging = browser.find_element_by_name("packaging")
        packaging.clear()
        packaging.send_keys("packaging")

        time.sleep(5)

        # fill insurance
        insurance = browser.find_element_by_name("insurance")
        insurance.clear()
        insurance.send_keys("insurance")

        time.sleep(5)

        # fill postage
        postage = browser.find_element_by_name("postage")
        postage.clear()
        postage.send_keys("postage")

        time.sleep(5)

        # fill wholesale_total
        wholesale_total = browser.find_element_by_name("wholesale_total")
        wholesale_total.clear()
        wholesale_total.send_keys("wholesale_total")

        time.sleep(5)

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_pricing_strategy")
        submit.click()

        time.sleep(20)

        browser.quit()

    def test_generate_html_to_pdf_projected_income_statement(self):
        print("test_generate_html_to_pdf_projected_income_statement")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        browser.get('https://holomorphe.com/reporting/projected_income_statement')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r1c3
        r1c3 = browser.find_element_by_name("r1c3")
        r1c3.clear()
        r1c3.send_keys("r1c3")

        # fill r1c4
        r1c4 = browser.find_element_by_name("r1c4")
        r1c4.clear()
        r1c4.send_keys("r1c4")

        # fill r1c5
        r1c5 = browser.find_element_by_name("r1c5")
        r1c5.clear()
        r1c5.send_keys("r1c5")

        # fill r1c6
        r1c6 = browser.find_element_by_name("r1c6")
        r1c6.clear()
        r1c6.send_keys("r1c6")

        # fill r1c7
        r1c7 = browser.find_element_by_name("r1c7")
        r1c7.clear()
        r1c7.send_keys("r1c7")

        # fill r1c8
        r1c8 = browser.find_element_by_name("r1c8")
        r1c8.clear()
        r1c8.send_keys("r1c8")

        # fill r1c9
        r1c9 = browser.find_element_by_name("r1c9")
        r1c9.clear()
        r1c9.send_keys("r1c9")

        # fill r1c10
        r1c10 = browser.find_element_by_name("r1c10")
        r1c10.clear()
        r1c10.send_keys("r1c10")

        # fill r1c11
        r1c11 = browser.find_element_by_name("r1c11")
        r1c11.clear()
        r1c11.send_keys("r1c11")

        # fill r1c12
        r1c12 = browser.find_element_by_name("r1c12")
        r1c12.clear()
        r1c12.send_keys("r1c12")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r2c3
        r2c3 = browser.find_element_by_name("r2c3")
        r2c3.clear()
        r2c3.send_keys("r2c3")

        # fill r2c4
        r2c4 = browser.find_element_by_name("r2c4")
        r2c4.clear()
        r2c4.send_keys("r2c4")

        # fill r2c5
        r2c5 = browser.find_element_by_name("r2c5")
        r2c5.clear()
        r2c5.send_keys("r2c5")

        # fill r2c6
        r2c6 = browser.find_element_by_name("r2c6")
        r2c6.clear()
        r2c6.send_keys("r2c6")

        # fill r2c7
        r2c7 = browser.find_element_by_name("r2c7")
        r2c7.clear()
        r2c7.send_keys("r2c7")

        # fill r2c8
        r2c8 = browser.find_element_by_name("r2c8")
        r2c8.clear()
        r2c8.send_keys("r2c8")

        # fill r2c9
        r2c9 = browser.find_element_by_name("r2c9")
        r2c9.clear()
        r2c9.send_keys("r2c9")

        # fill r2c10
        r2c10 = browser.find_element_by_name("r2c10")
        r2c10.clear()
        r2c10.send_keys("r2c10")

        # fill r2c11
        r2c11 = browser.find_element_by_name("r2c11")
        r2c11.clear()
        r2c11.send_keys("r2c11")

        # fill r2c12
        r2c12 = browser.find_element_by_name("r2c12")
        r2c12.clear()
        r2c12.send_keys("r2c12")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r3c3
        r3c3 = browser.find_element_by_name("r3c3")
        r3c3.clear()
        r3c3.send_keys("r3c3")

        # fill r3c4
        r3c4 = browser.find_element_by_name("r3c4")
        r3c4.clear()
        r3c4.send_keys("r3c4")

        # fill r3c5
        r3c5 = browser.find_element_by_name("r3c5")
        r3c5.clear()
        r3c5.send_keys("r3c5")

        # fill r3c6
        r3c6 = browser.find_element_by_name("r3c6")
        r3c6.clear()
        r3c6.send_keys("r3c6")

        # fill r3c7
        r3c7 = browser.find_element_by_name("r3c7")
        r3c7.clear()
        r3c7.send_keys("r3c7")

        # fill r3c8
        r3c8 = browser.find_element_by_name("r3c8")
        r3c8.clear()
        r3c8.send_keys("r3c8")

        # fill r3c9
        r3c9 = browser.find_element_by_name("r3c9")
        r3c9.clear()
        r3c9.send_keys("r3c9")

        # fill r3c10
        r3c10 = browser.find_element_by_name("r3c10")
        r3c10.clear()
        r3c10.send_keys("r3c10")

        # fill r3c11
        r3c11 = browser.find_element_by_name("r3c11")
        r3c11.clear()
        r3c11.send_keys("r3c11")

        # fill r3c12
        r3c12 = browser.find_element_by_name("r3c12")
        r3c12.clear()
        r3c12.send_keys("r3c12")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r4c3
        r4c3 = browser.find_element_by_name("r4c3")
        r4c3.clear()
        r4c3.send_keys("r4c3")

        # fill r4c4
        r4c4 = browser.find_element_by_name("r4c4")
        r4c4.clear()
        r4c4.send_keys("r4c4")

        # fill r4c5
        r4c5 = browser.find_element_by_name("r4c5")
        r4c5.clear()
        r4c5.send_keys("r4c5")

        # fill r4c6
        r4c6 = browser.find_element_by_name("r4c6")
        r4c6.clear()
        r4c6.send_keys("r4c6")

        # fill r4c7
        r4c7 = browser.find_element_by_name("r4c7")
        r4c7.clear()
        r4c7.send_keys("r4c7")

        # fill r4c8
        r4c8 = browser.find_element_by_name("r4c8")
        r4c8.clear()
        r4c8.send_keys("r4c8")

        # fill r4c9
        r4c9 = browser.find_element_by_name("r4c9")
        r4c9.clear()
        r4c9.send_keys("r4c9")

        # fill r4c10
        r4c10 = browser.find_element_by_name("r4c10")
        r4c10.clear()
        r4c10.send_keys("r4c10")

        # fill r4c11
        r4c11 = browser.find_element_by_name("r4c11")
        r4c11.clear()
        r4c11.send_keys("r4c11")

        # fill r4c12
        r4c12 = browser.find_element_by_name("r4c12")
        r4c12.clear()
        r4c12.send_keys("r4c12")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r5c3
        r5c3 = browser.find_element_by_name("r5c3")
        r5c3.clear()
        r5c3.send_keys("r5c3")

        # fill r5c4
        r5c4 = browser.find_element_by_name("r5c4")
        r5c4.clear()
        r5c4.send_keys("r5c4")

        # fill r5c5
        r5c5 = browser.find_element_by_name("r5c5")
        r5c5.clear()
        r5c5.send_keys("r5c5")

        # fill r5c6
        r5c6 = browser.find_element_by_name("r5c6")
        r5c6.clear()
        r5c6.send_keys("r5c6")

        # fill r5c7
        r5c7 = browser.find_element_by_name("r5c7")
        r5c7.clear()
        r5c7.send_keys("r5c7")

        # fill r5c8
        r5c8 = browser.find_element_by_name("r5c8")
        r5c8.clear()
        r5c8.send_keys("r5c8")

        # fill r5c9
        r5c9 = browser.find_element_by_name("r5c9")
        r5c9.clear()
        r5c9.send_keys("r5c9")

        # fill r5c10
        r5c10 = browser.find_element_by_name("r5c10")
        r5c10.clear()
        r5c10.send_keys("r5c10")

        # fill r5c11
        r5c11 = browser.find_element_by_name("r5c11")
        r5c11.clear()
        r5c11.send_keys("r5c11")

        # fill r5c12
        r5c12 = browser.find_element_by_name("r5c12")
        r5c12.clear()
        r5c12.send_keys("r5c12")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r6c3
        r6c3 = browser.find_element_by_name("r6c3")
        r6c3.clear()
        r6c3.send_keys("r6c3")

        # fill r6c4
        r6c4 = browser.find_element_by_name("r6c4")
        r6c4.clear()
        r6c4.send_keys("r6c4")

        # fill r6c5
        r6c5 = browser.find_element_by_name("r6c5")
        r6c5.clear()
        r6c5.send_keys("r6c5")

        # fill r6c6
        r6c6 = browser.find_element_by_name("r6c6")
        r6c6.clear()
        r6c6.send_keys("r6c6")

        # fill r6c7
        r6c7 = browser.find_element_by_name("r6c7")
        r6c7.clear()
        r6c7.send_keys("r6c7")

        # fill r6c8
        r6c8 = browser.find_element_by_name("r6c8")
        r6c8.clear()
        r6c8.send_keys("r6c8")

        # fill r6c9
        r6c9 = browser.find_element_by_name("r6c9")
        r6c9.clear()
        r6c9.send_keys("r6c9")

        # fill r6c10
        r6c10 = browser.find_element_by_name("r6c10")
        r6c10.clear()
        r6c10.send_keys("r6c10")

        # fill r6c11
        r6c11 = browser.find_element_by_name("r6c11")
        r6c11.clear()
        r6c11.send_keys("r6c11")

        # fill r6c12
        r6c12 = browser.find_element_by_name("r6c12")
        r6c12.clear()
        r6c12.send_keys("r6c12")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r7c3
        r7c3 = browser.find_element_by_name("r7c3")
        r7c3.clear()
        r7c3.send_keys("r7c3")

        # fill r7c4
        r7c4 = browser.find_element_by_name("r7c4")
        r7c4.clear()
        r7c4.send_keys("r7c4")

        # fill r7c5
        r7c5 = browser.find_element_by_name("r7c5")
        r7c5.clear()
        r7c5.send_keys("r7c5")

        # fill r7c6
        r7c6 = browser.find_element_by_name("r7c6")
        r7c6.clear()
        r7c6.send_keys("r7c6")

        # fill r7c7
        r7c7 = browser.find_element_by_name("r7c7")
        r7c7.clear()
        r7c7.send_keys("r7c7")

        # fill r7c8
        r7c8 = browser.find_element_by_name("r7c8")
        r7c8.clear()
        r7c8.send_keys("r7c8")

        # fill r7c9
        r7c9 = browser.find_element_by_name("r7c9")
        r7c9.clear()
        r7c9.send_keys("r7c9")

        # fill r7c10
        r7c10 = browser.find_element_by_name("r7c10")
        r7c10.clear()
        r7c10.send_keys("r7c10")

        # fill r7c11
        r7c11 = browser.find_element_by_name("r7c11")
        r7c11.clear()
        r7c11.send_keys("r7c11")

        # fill r7c12
        r7c12 = browser.find_element_by_name("r7c12")
        r7c12.clear()
        r7c12.send_keys("r7c12")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r8c3
        r8c3 = browser.find_element_by_name("r8c3")
        r8c3.clear()
        r8c3.send_keys("r8c3")

        # fill r8c4
        r8c4 = browser.find_element_by_name("r8c4")
        r8c4.clear()
        r8c4.send_keys("r8c4")

        # fill r8c5
        r8c5 = browser.find_element_by_name("r8c5")
        r8c5.clear()
        r8c5.send_keys("r8c5")

        # fill r8c6
        r8c6 = browser.find_element_by_name("r8c6")
        r8c6.clear()
        r8c6.send_keys("r8c6")

        # fill r8c7
        r8c7 = browser.find_element_by_name("r8c7")
        r8c7.clear()
        r8c7.send_keys("r8c7")

        # fill r8c8
        r8c8 = browser.find_element_by_name("r8c8")
        r8c8.clear()
        r8c8.send_keys("r8c8")

        # fill r8c9
        r8c9 = browser.find_element_by_name("r8c9")
        r8c9.clear()
        r8c9.send_keys("r8c9")

        # fill r8c10
        r8c10 = browser.find_element_by_name("r8c10")
        r8c10.clear()
        r8c10.send_keys("r8c10")

        # fill r8c11
        r8c11 = browser.find_element_by_name("r8c11")
        r8c11.clear()
        r8c11.send_keys("r8c11")

        # fill r8c12
        r8c12 = browser.find_element_by_name("r8c12")
        r8c12.clear()
        r8c12.send_keys("r8c12")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r9c3
        r9c3 = browser.find_element_by_name("r9c3")
        r9c3.clear()
        r9c3.send_keys("r9c3")

        # fill r9c4
        r9c4 = browser.find_element_by_name("r9c4")
        r9c4.clear()
        r9c4.send_keys("r9c4")

        # fill r9c5
        r9c5 = browser.find_element_by_name("r9c5")
        r9c5.clear()
        r9c5.send_keys("r9c5")

        # fill r9c6
        r9c6 = browser.find_element_by_name("r9c6")
        r9c6.clear()
        r9c6.send_keys("r9c6")

        # fill r9c7
        r9c7 = browser.find_element_by_name("r9c7")
        r9c7.clear()
        r9c7.send_keys("r9c7")

        # fill r9c8
        r9c8 = browser.find_element_by_name("r9c8")
        r9c8.clear()
        r9c8.send_keys("r9c8")

        # fill r9c9
        r9c9 = browser.find_element_by_name("r9c9")
        r9c9.clear()
        r9c9.send_keys("r9c9")

        # fill r9c10
        r9c10 = browser.find_element_by_name("r9c10")
        r9c10.clear()
        r9c10.send_keys("r9c10")

        # fill r9c11
        r9c11 = browser.find_element_by_name("r9c11")
        r9c11.clear()
        r9c11.send_keys("r9c11")

        # fill r9c12
        r9c12 = browser.find_element_by_name("r9c12")
        r9c12.clear()
        r9c12.send_keys("r9c12")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r10c3
        r10c3 = browser.find_element_by_name("r10c3")
        r10c3.clear()
        r10c3.send_keys("r10c3")

        # fill r10c4
        r10c4 = browser.find_element_by_name("r10c4")
        r10c4.clear()
        r10c4.send_keys("r10c4")

        # fill r10c5
        r10c5 = browser.find_element_by_name("r10c5")
        r10c5.clear()
        r10c5.send_keys("r10c5")

        # fill r10c6
        r10c6 = browser.find_element_by_name("r10c6")
        r10c6.clear()
        r10c6.send_keys("r10c6")

        # fill r10c7
        r10c7 = browser.find_element_by_name("r10c7")
        r10c7.clear()
        r10c7.send_keys("r10c7")

        # fill r10c8
        r10c8 = browser.find_element_by_name("r10c8")
        r10c8.clear()
        r10c8.send_keys("r10c8")

        # fill r10c9
        r10c9 = browser.find_element_by_name("r10c9")
        r10c9.clear()
        r10c9.send_keys("r10c9")

        # fill r10c10
        r10c10 = browser.find_element_by_name("r10c10")
        r10c10.clear()
        r10c10.send_keys("r10c10")

        # fill r10c11
        r10c11 = browser.find_element_by_name("r10c11")
        r10c11.clear()
        r10c11.send_keys("r10c11")

        # fill r10c12
        r10c12 = browser.find_element_by_name("r10c12")
        r10c12.clear()
        r10c12.send_keys("r10c12")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r11c3
        r11c3 = browser.find_element_by_name("r11c3")
        r11c3.clear()
        r11c3.send_keys("r11c3")

        # fill r11c4
        r11c4 = browser.find_element_by_name("r11c4")
        r11c4.clear()
        r11c4.send_keys("r11c4")

        # fill r11c5
        r11c5 = browser.find_element_by_name("r11c5")
        r11c5.clear()
        r11c5.send_keys("r11c5")

        # fill r11c6
        r11c6 = browser.find_element_by_name("r11c6")
        r11c6.clear()
        r11c6.send_keys("r11c6")

        # fill r11c7
        r11c7 = browser.find_element_by_name("r11c7")
        r11c7.clear()
        r11c7.send_keys("r11c7")

        # fill r11c8
        r11c8 = browser.find_element_by_name("r11c8")
        r11c8.clear()
        r11c8.send_keys("r11c8")

        # fill r11c9
        r11c9 = browser.find_element_by_name("r11c9")
        r11c9.clear()
        r11c9.send_keys("r11c9")

        # fill r11c10
        r11c10 = browser.find_element_by_name("r11c10")
        r11c10.clear()
        r11c10.send_keys("r11c10")

        # fill r11c11
        r11c11 = browser.find_element_by_name("r11c11")
        r11c11.clear()
        r11c11.send_keys("r11c11")

        # fill r11c12
        r11c12 = browser.find_element_by_name("r11c12")
        r11c12.clear()
        r11c12.send_keys("r11c12")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r12c3
        r12c3 = browser.find_element_by_name("r12c3")
        r12c3.clear()
        r12c3.send_keys("r12c3")

        # fill r12c4
        r12c4 = browser.find_element_by_name("r12c4")
        r12c4.clear()
        r12c4.send_keys("r12c4")

        # fill r12c5
        r12c5 = browser.find_element_by_name("r12c5")
        r12c5.clear()
        r12c5.send_keys("r12c5")

        # fill r12c6
        r12c6 = browser.find_element_by_name("r12c6")
        r12c6.clear()
        r12c6.send_keys("r12c6")

        # fill r12c7
        r12c7 = browser.find_element_by_name("r12c7")
        r12c7.clear()
        r12c7.send_keys("r12c7")

        # fill r12c8
        r12c8 = browser.find_element_by_name("r12c8")
        r12c8.clear()
        r12c8.send_keys("r12c8")

        # fill r12c9
        r12c9 = browser.find_element_by_name("r12c9")
        r12c9.clear()
        r12c9.send_keys("r12c9")

        # fill r12c10
        r12c10 = browser.find_element_by_name("r12c10")
        r12c10.clear()
        r12c10.send_keys("r12c10")

        # fill r12c11
        r12c11 = browser.find_element_by_name("r12c11")
        r12c11.clear()
        r12c11.send_keys("r12c11")

        # fill r12c12
        r12c12 = browser.find_element_by_name("r12c12")
        r12c12.clear()
        r12c12.send_keys("r12c12")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # fill r13c3
        r13c3 = browser.find_element_by_name("r13c3")
        r13c3.clear()
        r13c3.send_keys("r13c3")

        # fill r13c4
        r13c4 = browser.find_element_by_name("r13c4")
        r13c4.clear()
        r13c4.send_keys("r13c4")

        # fill r13c5
        r13c5 = browser.find_element_by_name("r13c5")
        r13c5.clear()
        r13c5.send_keys("r13c5")

        # fill r13c6
        r13c6 = browser.find_element_by_name("r13c6")
        r13c6.clear()
        r13c6.send_keys("r13c6")

        # fill r13c7
        r13c7 = browser.find_element_by_name("r13c7")
        r13c7.clear()
        r13c7.send_keys("r13c7")

        # fill r13c8
        r13c8 = browser.find_element_by_name("r13c8")
        r13c8.clear()
        r13c8.send_keys("r13c8")

        # fill r13c9
        r13c9 = browser.find_element_by_name("r13c9")
        r13c9.clear()
        r13c9.send_keys("r13c9")

        # fill r13c10
        r13c10 = browser.find_element_by_name("r13c10")
        r13c10.clear()
        r13c10.send_keys("r13c10")

        # fill r13c11
        r13c11 = browser.find_element_by_name("r13c11")
        r13c11.clear()
        r13c11.send_keys("r13c11")

        # fill r13c12
        r13c12 = browser.find_element_by_name("r13c12")
        r13c12.clear()
        r13c12.send_keys("r13c12")

        # fill r14c1
        r14c1 = browser.find_element_by_name("r14c1")
        r14c1.clear()
        r14c1.send_keys("r14c1")

        # fill r14c2
        r14c2 = browser.find_element_by_name("r14c2")
        r14c2.clear()
        r14c2.send_keys("r14c2")

        # fill r14c3
        r14c3 = browser.find_element_by_name("r14c3")
        r14c3.clear()
        r14c3.send_keys("r14c3")

        # fill r14c4
        r14c4 = browser.find_element_by_name("r14c4")
        r14c4.clear()
        r14c4.send_keys("r14c4")

        # fill r14c5
        r14c5 = browser.find_element_by_name("r14c5")
        r14c5.clear()
        r14c5.send_keys("r14c5")

        # fill r14c6
        r14c6 = browser.find_element_by_name("r14c6")
        r14c6.clear()
        r14c6.send_keys("r14c6")

        # fill r14c7
        r14c7 = browser.find_element_by_name("r14c7")
        r14c7.clear()
        r14c7.send_keys("r14c7")

        # fill r14c8
        r14c8 = browser.find_element_by_name("r14c8")
        r14c8.clear()
        r14c8.send_keys("r14c8")

        # fill r14c9
        r14c9 = browser.find_element_by_name("r14c9")
        r14c9.clear()
        r14c9.send_keys("r14c9")

        # fill r14c10
        r14c10 = browser.find_element_by_name("r14c10")
        r14c10.clear()
        r14c10.send_keys("r14c10")

        # fill r14c11
        r14c11 = browser.find_element_by_name("r14c11")
        r14c11.clear()
        r14c11.send_keys("r14c11")

        # fill r14c12
        r14c12 = browser.find_element_by_name("r14c12")
        r14c12.clear()
        r14c12.send_keys("r14c12")

        # fill r15c1
        r15c1 = browser.find_element_by_name("r15c1")
        r15c1.clear()
        r15c1.send_keys("r15c1")

        # fill r15c2
        r15c2 = browser.find_element_by_name("r15c2")
        r15c2.clear()
        r15c2.send_keys("r15c2")

        # fill r15c3
        r15c3 = browser.find_element_by_name("r15c3")
        r15c3.clear()
        r15c3.send_keys("r15c3")

        # fill r15c4
        r15c4 = browser.find_element_by_name("r15c4")
        r15c4.clear()
        r15c4.send_keys("r15c4")

        # fill r15c5
        r15c5 = browser.find_element_by_name("r15c5")
        r15c5.clear()
        r15c5.send_keys("r15c5")

        # fill r15c6
        r15c6 = browser.find_element_by_name("r15c6")
        r15c6.clear()
        r15c6.send_keys("r15c6")

        # fill r15c7
        r15c7 = browser.find_element_by_name("r15c7")
        r15c7.clear()
        r15c7.send_keys("r15c7")

        # fill r15c8
        r15c8 = browser.find_element_by_name("r15c8")
        r15c8.clear()
        r15c8.send_keys("r15c8")

        # fill r15c9
        r15c9 = browser.find_element_by_name("r15c9")
        r15c9.clear()
        r15c9.send_keys("r15c9")

        # fill r15c10
        r15c10 = browser.find_element_by_name("r15c10")
        r15c10.clear()
        r15c10.send_keys("r15c10")

        # fill r15c11
        r15c11 = browser.find_element_by_name("r15c11")
        r15c11.clear()
        r15c11.send_keys("r15c11")

        # fill r15c12
        r15c12 = browser.find_element_by_name("r15c12")
        r15c12.clear()
        r15c12.send_keys("r15c12")

        # fill r16c1
        r16c1 = browser.find_element_by_name("r16c1")
        r16c1.clear()
        r16c1.send_keys("r16c1")

        # fill r16c2
        r16c2 = browser.find_element_by_name("r16c2")
        r16c2.clear()
        r16c2.send_keys("r16c2")

        # fill r16c3
        r16c3 = browser.find_element_by_name("r16c3")
        r16c3.clear()
        r16c3.send_keys("r16c3")

        # fill r16c4
        r16c4 = browser.find_element_by_name("r16c4")
        r16c4.clear()
        r16c4.send_keys("r16c4")

        # fill r16c5
        r16c5 = browser.find_element_by_name("r16c5")
        r16c5.clear()
        r16c5.send_keys("r16c5")

        # fill r16c6
        r16c6 = browser.find_element_by_name("r16c6")
        r16c6.clear()
        r16c6.send_keys("r16c6")

        # fill r16c7
        r16c7 = browser.find_element_by_name("r16c7")
        r16c7.clear()
        r16c7.send_keys("r16c7")

        # fill r16c8
        r16c8 = browser.find_element_by_name("r16c8")
        r16c8.clear()
        r16c8.send_keys("r16c8")

        # fill r16c9
        r16c9 = browser.find_element_by_name("r16c9")
        r16c9.clear()
        r16c9.send_keys("r16c9")

        # fill r16c10
        r16c10 = browser.find_element_by_name("r16c10")
        r16c10.clear()
        r16c10.send_keys("r16c10")

        # fill r16c11
        r16c11 = browser.find_element_by_name("r16c11")
        r16c11.clear()
        r16c11.send_keys("r16c11")

        # fill r16c12
        r16c12 = browser.find_element_by_name("r16c12")
        r16c12.clear()
        r16c12.send_keys("r16c12")

        # fill r17c1
        r17c1 = browser.find_element_by_name("r17c1")
        r17c1.clear()
        r17c1.send_keys("r17c1")

        # fill r17c2
        r17c2 = browser.find_element_by_name("r17c2")
        r17c2.clear()
        r17c2.send_keys("r17c2")

        # fill r17c3
        r17c3 = browser.find_element_by_name("r17c3")
        r17c3.clear()
        r17c3.send_keys("r17c3")

        # fill r17c4
        r17c4 = browser.find_element_by_name("r17c4")
        r17c4.clear()
        r17c4.send_keys("r17c4")

        # fill r17c5
        r17c5 = browser.find_element_by_name("r17c5")
        r17c5.clear()
        r17c5.send_keys("r17c5")

        # fill r17c6
        r17c6 = browser.find_element_by_name("r17c6")
        r17c6.clear()
        r17c6.send_keys("r17c6")

        # fill r17c7
        r17c7 = browser.find_element_by_name("r17c7")
        r17c7.clear()
        r17c7.send_keys("r17c7")

        # fill r17c8
        r17c8 = browser.find_element_by_name("r17c8")
        r17c8.clear()
        r17c8.send_keys("r17c8")

        # fill r17c9
        r17c9 = browser.find_element_by_name("r17c9")
        r17c9.clear()
        r17c9.send_keys("r17c9")

        # fill r17c10
        r17c10 = browser.find_element_by_name("r17c10")
        r17c10.clear()
        r17c10.send_keys("r17c10")

        # fill r17c11
        r17c11 = browser.find_element_by_name("r17c11")
        r17c11.clear()
        r17c11.send_keys("r17c11")

        # fill r17c12
        r17c12 = browser.find_element_by_name("r17c12")
        r17c12.clear()
        r17c12.send_keys("r17c12")

        # fill r18c1
        r18c1 = browser.find_element_by_name("r18c1")
        r18c1.clear()
        r18c1.send_keys("r18c1")

        # fill r18c2
        r18c2 = browser.find_element_by_name("r18c2")
        r18c2.clear()
        r18c2.send_keys("r18c2")

        # fill r18c3
        r18c3 = browser.find_element_by_name("r18c3")
        r18c3.clear()
        r18c3.send_keys("r18c3")

        # fill r18c4
        r18c4 = browser.find_element_by_name("r18c4")
        r18c4.clear()
        r18c4.send_keys("r18c4")

        # fill r18c5
        r18c5 = browser.find_element_by_name("r18c5")
        r18c5.clear()
        r18c5.send_keys("r18c5")

        # fill r18c6
        r18c6 = browser.find_element_by_name("r18c6")
        r18c6.clear()
        r18c6.send_keys("r18c6")

        # fill r18c7
        r18c7 = browser.find_element_by_name("r18c7")
        r18c7.clear()
        r18c7.send_keys("r18c7")

        # fill r18c8
        r18c8 = browser.find_element_by_name("r18c8")
        r18c8.clear()
        r18c8.send_keys("r18c8")

        # fill r18c9
        r18c9 = browser.find_element_by_name("r18c9")
        r18c9.clear()
        r18c9.send_keys("r18c9")

        # fill r18c10
        r18c10 = browser.find_element_by_name("r18c10")
        r18c10.clear()
        r18c10.send_keys("r18c10")

        # fill r18c11
        r18c11 = browser.find_element_by_name("r18c11")
        r18c11.clear()
        r18c11.send_keys("r18c11")

        # fill r18c12
        r18c12 = browser.find_element_by_name("r18c12")
        r18c12.clear()
        r18c12.send_keys("r18c12")

        # fill r19c1
        r19c1 = browser.find_element_by_name("r19c1")
        r19c1.clear()
        r19c1.send_keys("r19c1")

        # fill r19c2
        r19c2 = browser.find_element_by_name("r19c2")
        r19c2.clear()
        r19c2.send_keys("r19c2")

        # fill r19c3
        r19c3 = browser.find_element_by_name("r19c3")
        r19c3.clear()
        r19c3.send_keys("r19c3")

        # fill r19c4
        r19c4 = browser.find_element_by_name("r19c4")
        r19c4.clear()
        r19c4.send_keys("r19c4")

        # fill r19c5
        r19c5 = browser.find_element_by_name("r19c5")
        r19c5.clear()
        r19c5.send_keys("r19c5")

        # fill r19c6
        r19c6 = browser.find_element_by_name("r19c6")
        r19c6.clear()
        r19c6.send_keys("r19c6")

        # fill r19c7
        r19c7 = browser.find_element_by_name("r19c7")
        r19c7.clear()
        r19c7.send_keys("r19c7")

        # fill r19c8
        r19c8 = browser.find_element_by_name("r19c8")
        r19c8.clear()
        r19c8.send_keys("r19c8")

        # fill r19c9
        r19c9 = browser.find_element_by_name("r19c9")
        r19c9.clear()
        r19c9.send_keys("r19c9")

        # fill r19c10
        r19c10 = browser.find_element_by_name("r19c10")
        r19c10.clear()
        r19c10.send_keys("r19c10")

        # fill r19c11
        r19c11 = browser.find_element_by_name("r19c11")
        r19c11.clear()
        r19c11.send_keys("r19c11")

        # fill r19c12
        r19c12 = browser.find_element_by_name("r19c12")
        r19c12.clear()
        r19c12.send_keys("r19c12")

        # fill r20c1
        r20c1 = browser.find_element_by_name("r20c1")
        r20c1.clear()
        r20c1.send_keys("r20c1")

        # fill r20c2
        r20c2 = browser.find_element_by_name("r20c2")
        r20c2.clear()
        r20c2.send_keys("r20c2")

        # fill r20c3
        r20c3 = browser.find_element_by_name("r20c3")
        r20c3.clear()
        r20c3.send_keys("r20c3")

        # fill r20c4
        r20c4 = browser.find_element_by_name("r20c4")
        r20c4.clear()
        r20c4.send_keys("r20c4")

        # fill r20c5
        r20c5 = browser.find_element_by_name("r20c5")
        r20c5.clear()
        r20c5.send_keys("r20c5")

        # fill r20c6
        r20c6 = browser.find_element_by_name("r20c6")
        r20c6.clear()
        r20c6.send_keys("r20c6")

        # fill r20c7
        r20c7 = browser.find_element_by_name("r20c7")
        r20c7.clear()
        r20c7.send_keys("r20c7")

        # fill r20c8
        r20c8 = browser.find_element_by_name("r20c8")
        r20c8.clear()
        r20c8.send_keys("r20c8")

        # fill r20c9
        r20c9 = browser.find_element_by_name("r20c9")
        r20c9.clear()
        r20c9.send_keys("r20c9")

        # fill r20c10
        r20c10 = browser.find_element_by_name("r20c10")
        r20c10.clear()
        r20c10.send_keys("r20c10")

        # fill r20c11
        r20c11 = browser.find_element_by_name("r20c11")
        r20c11.clear()
        r20c11.send_keys("r20c11")

        # fill r20c12
        r20c12 = browser.find_element_by_name("r20c12")
        r20c12.clear()
        r20c12.send_keys("r20c12")

        # fill r21c1
        r21c1 = browser.find_element_by_name("r21c1")
        r21c1.clear()
        r21c1.send_keys("r21c1")

        # fill r21c2
        r21c2 = browser.find_element_by_name("r21c2")
        r21c2.clear()
        r21c2.send_keys("r21c2")

        # fill r21c3
        r21c3 = browser.find_element_by_name("r21c3")
        r21c3.clear()
        r21c3.send_keys("r21c3")

        # fill r21c4
        r21c4 = browser.find_element_by_name("r21c4")
        r21c4.clear()
        r21c4.send_keys("r21c4")

        # fill r21c5
        r21c5 = browser.find_element_by_name("r21c5")
        r21c5.clear()
        r21c5.send_keys("r21c5")

        # fill r21c6
        r21c6 = browser.find_element_by_name("r21c6")
        r21c6.clear()
        r21c6.send_keys("r21c6")

        # fill r21c7
        r21c7 = browser.find_element_by_name("r21c7")
        r21c7.clear()
        r21c7.send_keys("r21c7")

        # fill r21c8
        r21c8 = browser.find_element_by_name("r21c8")
        r21c8.clear()
        r21c8.send_keys("r21c8")

        # fill r21c9
        r21c9 = browser.find_element_by_name("r21c9")
        r21c9.clear()
        r21c9.send_keys("r21c9")

        # fill r21c10
        r21c10 = browser.find_element_by_name("r21c10")
        r21c10.clear()
        r21c10.send_keys("r21c10")

        # fill r21c11
        r21c11 = browser.find_element_by_name("r21c11")
        r21c11.clear()
        r21c11.send_keys("r21c11")

        # fill r21c12
        r21c12 = browser.find_element_by_name("r21c12")
        r21c12.clear()
        r21c12.send_keys("r21c12")

        # fill r22c1
        r22c1 = browser.find_element_by_name("r22c1")
        r22c1.clear()
        r22c1.send_keys("r22c1")

        # fill r22c2
        r22c2 = browser.find_element_by_name("r22c2")
        r22c2.clear()
        r22c2.send_keys("r22c2")

        # fill r22c3
        r22c3 = browser.find_element_by_name("r22c3")
        r22c3.clear()
        r22c3.send_keys("r22c3")

        # fill r22c4
        r22c4 = browser.find_element_by_name("r22c4")
        r22c4.clear()
        r22c4.send_keys("r22c4")

        # fill r22c5
        r22c5 = browser.find_element_by_name("r22c5")
        r22c5.clear()
        r22c5.send_keys("r22c5")

        # fill r22c6
        r22c6 = browser.find_element_by_name("r22c6")
        r22c6.clear()
        r22c6.send_keys("r22c6")

        # fill r22c7
        r22c7 = browser.find_element_by_name("r22c7")
        r22c7.clear()
        r22c7.send_keys("r22c7")

        # fill r22c8
        r22c8 = browser.find_element_by_name("r22c8")
        r22c8.clear()
        r22c8.send_keys("r22c8")

        # fill r22c9
        r22c9 = browser.find_element_by_name("r22c9")
        r22c9.clear()
        r22c9.send_keys("r22c9")

        # fill r22c10
        r22c10 = browser.find_element_by_name("r22c10")
        r22c10.clear()
        r22c10.send_keys("r22c10")

        # fill r22c11
        r22c11 = browser.find_element_by_name("r22c11")
        r22c11.clear()
        r22c11.send_keys("r22c11")

        # fill r22c12
        r22c12 = browser.find_element_by_name("r22c12")
        r22c12.clear()
        r22c12.send_keys("r22c12")

        # fill r23c1
        r23c1 = browser.find_element_by_name("r23c1")
        r23c1.clear()
        r23c1.send_keys("r23c1")

        # fill r23c2
        r23c2 = browser.find_element_by_name("r23c2")
        r23c2.clear()
        r23c2.send_keys("r23c2")

        # fill r23c3
        r23c3 = browser.find_element_by_name("r23c3")
        r23c3.clear()
        r23c3.send_keys("r23c3")

        # fill r23c4
        r23c4 = browser.find_element_by_name("r23c4")
        r23c4.clear()
        r23c4.send_keys("r23c4")

        # fill r23c5
        r23c5 = browser.find_element_by_name("r23c5")
        r23c5.clear()
        r23c5.send_keys("r23c5")

        # fill r23c6
        r23c6 = browser.find_element_by_name("r23c6")
        r23c6.clear()
        r23c6.send_keys("r23c6")

        # fill r23c7
        r23c7 = browser.find_element_by_name("r23c7")
        r23c7.clear()
        r23c7.send_keys("r23c7")

        # fill r23c8
        r23c8 = browser.find_element_by_name("r23c8")
        r23c8.clear()
        r23c8.send_keys("r23c8")

        # fill r23c9
        r23c9 = browser.find_element_by_name("r23c9")
        r23c9.clear()
        r23c9.send_keys("r23c9")

        # fill r23c10
        r23c10 = browser.find_element_by_name("r23c10")
        r23c10.clear()
        r23c10.send_keys("r23c10")

        # fill r23c11
        r23c11 = browser.find_element_by_name("r23c11")
        r23c11.clear()
        r23c11.send_keys("r23c11")

        # fill r23c12
        r23c12 = browser.find_element_by_name("r23c12")
        r23c12.clear()
        r23c12.send_keys("r23c12")

        # fill r24c1
        r24c1 = browser.find_element_by_name("r24c1")
        r24c1.clear()
        r24c1.send_keys("r24c1")

        # fill r24c2
        r24c2 = browser.find_element_by_name("r24c2")
        r24c2.clear()
        r24c2.send_keys("r24c2")

        # fill r24c3
        r24c3 = browser.find_element_by_name("r24c3")
        r24c3.clear()
        r24c3.send_keys("r24c3")

        # fill r24c4
        r24c4 = browser.find_element_by_name("r24c4")
        r24c4.clear()
        r24c4.send_keys("r24c4")

        # fill r24c5
        r24c5 = browser.find_element_by_name("r24c5")
        r24c5.clear()
        r24c5.send_keys("r24c5")

        # fill r24c6
        r24c6 = browser.find_element_by_name("r24c6")
        r24c6.clear()
        r24c6.send_keys("r24c6")

        # fill r24c7
        r24c7 = browser.find_element_by_name("r24c7")
        r24c7.clear()
        r24c7.send_keys("r24c7")

        # fill r24c8
        r24c8 = browser.find_element_by_name("r24c8")
        r24c8.clear()
        r24c8.send_keys("r24c8")

        # fill r24c9
        r24c9 = browser.find_element_by_name("r24c9")
        r24c9.clear()
        r24c9.send_keys("r24c9")

        # fill r24c10
        r24c10 = browser.find_element_by_name("r24c10")
        r24c10.clear()
        r24c10.send_keys("r24c10")

        # fill r24c11
        r24c11 = browser.find_element_by_name("r24c11")
        r24c11.clear()
        r24c11.send_keys("r24c11")

        # fill r24c12
        r24c12 = browser.find_element_by_name("r24c12")
        r24c12.clear()
        r24c12.send_keys("r24c12")

        # fill r25c1
        r25c1 = browser.find_element_by_name("r25c1")
        r25c1.clear()
        r25c1.send_keys("r25c1")

        # fill r25c2
        r25c2 = browser.find_element_by_name("r25c2")
        r25c2.clear()
        r25c2.send_keys("r25c2")

        # fill r25c3
        r25c3 = browser.find_element_by_name("r25c3")
        r25c3.clear()
        r25c3.send_keys("r25c3")

        # fill r25c4
        r25c4 = browser.find_element_by_name("r25c4")
        r25c4.clear()
        r25c4.send_keys("r25c4")

        # fill r25c5
        r25c5 = browser.find_element_by_name("r25c5")
        r25c5.clear()
        r25c5.send_keys("r25c5")

        # fill r25c6
        r25c6 = browser.find_element_by_name("r25c6")
        r25c6.clear()
        r25c6.send_keys("r25c6")

        # fill r25c7
        r25c7 = browser.find_element_by_name("r25c7")
        r25c7.clear()
        r25c7.send_keys("r25c7")

        # fill r25c8
        r25c8 = browser.find_element_by_name("r25c8")
        r25c8.clear()
        r25c8.send_keys("r25c8")

        # fill r25c9
        r25c9 = browser.find_element_by_name("r25c9")
        r25c9.clear()
        r25c9.send_keys("r25c9")

        # fill r25c10
        r25c10 = browser.find_element_by_name("r25c10")
        r25c10.clear()
        r25c10.send_keys("r25c10")

        # fill r25c11
        r25c11 = browser.find_element_by_name("r25c11")
        r25c11.clear()
        r25c11.send_keys("r25c11")

        # fill r25c12
        r25c12 = browser.find_element_by_name("r25c12")
        r25c12.clear()
        r25c12.send_keys("r25c12")

        # fill r26c1
        r26c1 = browser.find_element_by_name("r26c1")
        r26c1.clear()
        r26c1.send_keys("r26c1")

        # fill r26c2
        r26c2 = browser.find_element_by_name("r26c2")
        r26c2.clear()
        r26c2.send_keys("r26c2")

        # fill r26c3
        r26c3 = browser.find_element_by_name("r26c3")
        r26c3.clear()
        r26c3.send_keys("r26c3")

        # fill r26c4
        r26c4 = browser.find_element_by_name("r26c4")
        r26c4.clear()
        r26c4.send_keys("r26c4")

        # fill r26c5
        r26c5 = browser.find_element_by_name("r26c5")
        r26c5.clear()
        r26c5.send_keys("r26c5")

        # fill r26c6
        r26c6 = browser.find_element_by_name("r26c6")
        r26c6.clear()
        r26c6.send_keys("r26c6")

        # fill r26c7
        r26c7 = browser.find_element_by_name("r26c7")
        r26c7.clear()
        r26c7.send_keys("r26c7")

        # fill r26c8
        r26c8 = browser.find_element_by_name("r26c8")
        r26c8.clear()
        r26c8.send_keys("r26c8")

        # fill r26c9
        r26c9 = browser.find_element_by_name("r26c9")
        r26c9.clear()
        r26c9.send_keys("r26c9")

        # fill r26c10
        r26c10 = browser.find_element_by_name("r26c10")
        r26c10.clear()
        r26c10.send_keys("r26c10")

        # fill r26c11
        r26c11 = browser.find_element_by_name("r26c11")
        r26c11.clear()
        r26c11.send_keys("r26c11")

        # fill r26c12
        r26c12 = browser.find_element_by_name("r26c12")
        r26c12.clear()
        r26c12.send_keys("r26c12")

        # fill r27c1
        r27c1 = browser.find_element_by_name("r27c1")
        r27c1.clear()
        r27c1.send_keys("r27c1")

        # fill r27c2
        r27c2 = browser.find_element_by_name("r27c2")
        r27c2.clear()
        r27c2.send_keys("r27c2")

        # fill r27c3
        r27c3 = browser.find_element_by_name("r27c3")
        r27c3.clear()
        r27c3.send_keys("r27c3")

        # fill r27c4
        r27c4 = browser.find_element_by_name("r27c4")
        r27c4.clear()
        r27c4.send_keys("r27c4")

        # fill r27c5
        r27c5 = browser.find_element_by_name("r27c5")
        r27c5.clear()
        r27c5.send_keys("r27c5")

        # fill r27c6
        r27c6 = browser.find_element_by_name("r27c6")
        r27c6.clear()
        r27c6.send_keys("r27c6")

        # fill r27c7
        r27c7 = browser.find_element_by_name("r27c7")
        r27c7.clear()
        r27c7.send_keys("r27c7")

        # fill r27c8
        r27c8 = browser.find_element_by_name("r27c8")
        r27c8.clear()
        r27c8.send_keys("r27c8")

        # fill r27c9
        r27c9 = browser.find_element_by_name("r27c9")
        r27c9.clear()
        r27c9.send_keys("r27c9")

        # fill r27c10
        r27c10 = browser.find_element_by_name("r27c10")
        r27c10.clear()
        r27c10.send_keys("r27c10")

        # fill r27c11
        r27c11 = browser.find_element_by_name("r27c11")
        r27c11.clear()
        r27c11.send_keys("r27c11")

        # fill r27c12
        r27c12 = browser.find_element_by_name("r27c12")
        r27c12.clear()
        r27c12.send_keys("r27c12")

        # fill r28c1
        r28c1 = browser.find_element_by_name("r28c1")
        r28c1.clear()
        r28c1.send_keys("r28c1")

        # fill r28c2
        r28c2 = browser.find_element_by_name("r28c2")
        r28c2.clear()
        r28c2.send_keys("r28c2")

        # fill r28c3
        r28c3 = browser.find_element_by_name("r28c3")
        r28c3.clear()
        r28c3.send_keys("r28c3")

        # fill r28c4
        r28c4 = browser.find_element_by_name("r28c4")
        r28c4.clear()
        r28c4.send_keys("r28c4")

        # fill r28c5
        r28c5 = browser.find_element_by_name("r28c5")
        r28c5.clear()
        r28c5.send_keys("r28c5")

        # fill r28c6
        r28c6 = browser.find_element_by_name("r28c6")
        r28c6.clear()
        r28c6.send_keys("r28c6")

        # fill r28c7
        r28c7 = browser.find_element_by_name("r28c7")
        r28c7.clear()
        r28c7.send_keys("r28c7")

        # fill r28c8
        r28c8 = browser.find_element_by_name("r28c8")
        r28c8.clear()
        r28c8.send_keys("r28c8")

        # fill r28c9
        r28c9 = browser.find_element_by_name("r28c9")
        r28c9.clear()
        r28c9.send_keys("r28c9")

        # fill r28c10
        r28c10 = browser.find_element_by_name("r28c10")
        r28c10.clear()
        r28c10.send_keys("r28c10")

        # fill r28c11
        r28c11 = browser.find_element_by_name("r28c11")
        r28c11.clear()
        r28c11.send_keys("r28c11")

        # fill r28c12
        r28c12 = browser.find_element_by_name("r28c12")
        r28c12.clear()
        r28c12.send_keys("r28c12")

        # fill r29c1
        r29c1 = browser.find_element_by_name("r29c1")
        r29c1.clear()
        r29c1.send_keys("r29c1")

        # fill r29c2
        r29c2 = browser.find_element_by_name("r29c2")
        r29c2.clear()
        r29c2.send_keys("r29c2")

        # fill r29c3
        r29c3 = browser.find_element_by_name("r29c3")
        r29c3.clear()
        r29c3.send_keys("r29c3")

        # fill r29c4
        r29c4 = browser.find_element_by_name("r29c4")
        r29c4.clear()
        r29c4.send_keys("r29c4")

        # fill r29c5
        r29c5 = browser.find_element_by_name("r29c5")
        r29c5.clear()
        r29c5.send_keys("r29c5")

        # fill r29c6
        r29c6 = browser.find_element_by_name("r29c6")
        r29c6.clear()
        r29c6.send_keys("r29c6")

        # fill r29c7
        r29c7 = browser.find_element_by_name("r29c7")
        r29c7.clear()
        r29c7.send_keys("r29c7")

        # fill r29c8
        r29c8 = browser.find_element_by_name("r29c8")
        r29c8.clear()
        r29c8.send_keys("r29c8")

        # fill r29c9
        r29c9 = browser.find_element_by_name("r29c9")
        r29c9.clear()
        r29c9.send_keys("r29c9")

        # fill r29c10
        r29c10 = browser.find_element_by_name("r29c10")
        r29c10.clear()
        r29c10.send_keys("r29c10")

        # fill r29c11
        r29c11 = browser.find_element_by_name("r29c11")
        r29c11.clear()
        r29c11.send_keys("r29c11")

        # fill r29c12
        r29c12 = browser.find_element_by_name("r29c12")
        r29c12.clear()
        r29c12.send_keys("r29c12")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_projected_income_statement")
        submit.click()

        time.sleep(5)

        browser.quit()

    def test_generate_html_to_pdf_start_up_expenses(self):
        print("test_generate_html_to_pdf_start_up_expenses")

        time.sleep(1)

        warnings.filterwarnings(action="ignore", message="unclosed", category=ResourceWarning)

        time.sleep(1)

        # with Firefox
        browser = webdriver.Firefox(executable_path='geckodriver.exe')

        time.sleep(1)

        # maximize window
        browser.maximize_window()

        time.sleep(1)

        # open the report
        browser.get('https://holomorphe.com/reporting/start_up_expenses')

        time.sleep(5)

        # fill company name
        company_name = browser.find_element_by_name("company_name")
        company_name.clear()
        company_name.send_keys("company_name")

        time.sleep(1)

        # fill share_capital
        share_capital = browser.find_element_by_name("share_capital")
        share_capital.clear()
        share_capital.send_keys("share_capital")
        time.sleep(1)

        # fill head_office_address
        head_office_address = browser.find_element_by_name("head_office_address")
        head_office_address.clear()
        head_office_address.send_keys("head_office_address")

        time.sleep(1)

        # fill establishment_number
        establishment_number = browser.find_element_by_name("establishment_number")
        establishment_number.clear()
        establishment_number.send_keys("establishment_number")

        time.sleep(1)

        # fill register_of_trade_and_companies
        register_of_trade_and_companies = browser.find_element_by_name("register_of_trade_and_companies")
        register_of_trade_and_companies.clear()
        register_of_trade_and_companies.send_keys("register_of_trade_and_companies")
        time.sleep(1)

        # fill main_activities
        main_activities = browser.find_element_by_name("main_activities")
        main_activities.clear()
        main_activities.send_keys("main_activities")
        time.sleep(1)

        # fill activity_number
        activity_number = browser.find_element_by_name("activity_number")
        activity_number.clear()
        activity_number.send_keys("activity_number")

        time.sleep(1)

        # fill intra_community_vat_number
        intra_community_vat_number = browser.find_element_by_name("intra_community_vat_number")
        intra_community_vat_number.clear()
        intra_community_vat_number.send_keys("intra_community_vat_number")
        time.sleep(1)

        # fill president
        president = browser.find_element_by_name("president")
        president.clear()
        president.send_keys("president")
        time.sleep(1)

        # fill registration_date
        registration_date = browser.find_element_by_name("registration_date")
        registration_date.clear()
        registration_date.send_keys("registration_date")
        time.sleep(1)

        # fill r1c1
        r1c1 = browser.find_element_by_name("r1c1")
        r1c1.clear()
        r1c1.send_keys("r1c1")

        # fill r1c2
        r1c2 = browser.find_element_by_name("r1c2")
        r1c2.clear()
        r1c2.send_keys("r1c2")

        # fill r2c1
        r2c1 = browser.find_element_by_name("r2c1")
        r2c1.clear()
        r2c1.send_keys("r2c1")

        # fill r2c2
        r2c2 = browser.find_element_by_name("r2c2")
        r2c2.clear()
        r2c2.send_keys("r2c2")

        # fill r3c1
        r3c1 = browser.find_element_by_name("r3c1")
        r3c1.clear()
        r3c1.send_keys("r3c1")

        # fill r3c2
        r3c2 = browser.find_element_by_name("r3c2")
        r3c2.clear()
        r3c2.send_keys("r3c2")

        # fill r4c1
        r4c1 = browser.find_element_by_name("r4c1")
        r4c1.clear()
        r4c1.send_keys("r4c1")

        # fill r4c2
        r4c2 = browser.find_element_by_name("r4c2")
        r4c2.clear()
        r4c2.send_keys("r4c2")

        # fill r5c1
        r5c1 = browser.find_element_by_name("r5c1")
        r5c1.clear()
        r5c1.send_keys("r5c1")

        # fill r5c2
        r5c2 = browser.find_element_by_name("r5c2")
        r5c2.clear()
        r5c2.send_keys("r5c2")

        # fill r6c1
        r6c1 = browser.find_element_by_name("r6c1")
        r6c1.clear()
        r6c1.send_keys("r6c1")

        # fill r6c2
        r6c2 = browser.find_element_by_name("r6c2")
        r6c2.clear()
        r6c2.send_keys("r6c2")

        # fill r7c1
        r7c1 = browser.find_element_by_name("r7c1")
        r7c1.clear()
        r7c1.send_keys("r7c1")

        # fill r7c2
        r7c2 = browser.find_element_by_name("r7c2")
        r7c2.clear()
        r7c2.send_keys("r7c2")

        # fill r8c1
        r8c1 = browser.find_element_by_name("r8c1")
        r8c1.clear()
        r8c1.send_keys("r8c1")

        # fill r8c2
        r8c2 = browser.find_element_by_name("r8c2")
        r8c2.clear()
        r8c2.send_keys("r8c2")

        # fill r9c1
        r9c1 = browser.find_element_by_name("r9c1")
        r9c1.clear()
        r9c1.send_keys("r9c1")

        # fill r9c2
        r9c2 = browser.find_element_by_name("r9c2")
        r9c2.clear()
        r9c2.send_keys("r9c2")

        # fill r10c1
        r10c1 = browser.find_element_by_name("r10c1")
        r10c1.clear()
        r10c1.send_keys("r10c1")

        # fill r10c2
        r10c2 = browser.find_element_by_name("r10c2")
        r10c2.clear()
        r10c2.send_keys("r10c2")

        # fill r11c1
        r11c1 = browser.find_element_by_name("r11c1")
        r11c1.clear()
        r11c1.send_keys("r11c1")

        # fill r11c2
        r11c2 = browser.find_element_by_name("r11c2")
        r11c2.clear()
        r11c2.send_keys("r11c2")

        # fill r12c1
        r12c1 = browser.find_element_by_name("r12c1")
        r12c1.clear()
        r12c1.send_keys("r12c1")

        # fill r12c2
        r12c2 = browser.find_element_by_name("r12c2")
        r12c2.clear()
        r12c2.send_keys("r12c2")

        # fill r13c1
        r13c1 = browser.find_element_by_name("r13c1")
        r13c1.clear()
        r13c1.send_keys("r13c1")

        # fill r13c2
        r13c2 = browser.find_element_by_name("r13c2")
        r13c2.clear()
        r13c2.send_keys("r13c2")

        # submit
        submit = browser.find_element_by_name("button_generate_html_to_pdf_start_up_expenses")
        submit.click()

        time.sleep(5)

        browser.quit()


if __name__ == '__main__':
    unittest.main()
