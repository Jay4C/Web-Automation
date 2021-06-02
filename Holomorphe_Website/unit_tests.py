import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationHolomorpheWebsite(unittest.TestCase):
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

if __name__ == '__main__':
    unittest.main()
