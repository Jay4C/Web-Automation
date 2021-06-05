import unittest
import time
import warnings
from selenium import webdriver


class UnitTestsWebAutomationHolomorpheWebsite(unittest.TestCase):
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
