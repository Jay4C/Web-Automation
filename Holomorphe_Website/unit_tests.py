import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationHolomorpheWebsite(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
