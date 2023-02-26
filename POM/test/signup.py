import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from pages.login_page import LoginPage
from pages.home_page import HomePage
from pages.setup_page import SetupPage
from pages.membership_page import MembershipPage
from pages.ticket_page import TicketPage
from pages.discount_page import DiscountPage
from pages.create_page import CreatePage
from pages.publish_page import PublishPage
from pages.mybusses_page import MyBussesPage


class ShareBusTest(unittest.TestCase):

    driver = None

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://test.sharebus.co/")
        self.wait = WebDriverWait(self.driver, 10)

    def test_share_bus(self):
        login_page = LoginPage(self.driver)
        login_page.click_sign_in_button()
        login_page.login("brainstation23@yopmail.com", "Pass@1234")

        home_page = HomePage(self.driver)
        home_page.select_user("Sharelead")
        home_page.click_set_up_sharebus_button()

        setup_page = SetupPage(self.driver)
        setup_page.enter_trip_details("Oslo, Norway", "Kolbotn, Norway")
        setup_page.click_continue_button()

        membership_page = MembershipPage(self.driver)
        membership_page.click_yes_button()
        membership_page.select_club("NTNUI")
        membership_page.click_continue_button()

        ticket_page = TicketPage(self.driver)
        ticket_page.click_no_button()

        discount_page = DiscountPage(self.driver)
        discount_page.click_no_button()

        create_page = CreatePage(self.driver)
        create_page.click_create_sharebus_button()

        publish_page = PublishPage(self.driver)
        publish_page.click_publish_button()

        create_page.enter_data_on_required_fields()
        create_page.click_review_and_publish_button()

        publish_page.click_publish_button()

        home_page.click_my_busses_link()

        mybusses_page = MyBussesPage(self.driver)
        self.assertTrue(mybusses_page.is_trip_displayed(), "New trip is not displayed on the 'My busses' page")

# if __name__ == '__main__':
#     unittest.main()


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


  # driver = None
    #
    # @classmethod
    # def setUpClass(cls, webdriver=None):
    #     # Visit the URL
    #     url = "https://test.sharebus.co/"
    #     cls.driver = webdriver.Chrome(executable_path=Global.CHROME_DRIVER)
    #     cls.driver.get(url)
    #     cls.driver.implicitly_wait(10)
    #     cls.driver.maximize_window()
    #