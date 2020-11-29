from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.SearchCustomerPage import SearchCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
import time
import pytest

class Test_004_SearchCustomer:
    base_url =  ReadConfig.getApplicationUrl()
    user_name = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regresssion
    def test_searchcustomer(self,setup):
        # self.logger.info("******Test_004_SearchCustomer Started*******")
        # self.logger.info("*****Login Home Page*****")

        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.user_name)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()

        # self.logger.info("*****Login HomePage Successfully*****")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()

        # self.logger.info("*****Search Customer Started******")
        self.search_cust = SearchCustomer(self.driver)
        self.search_cust.setemail("james_pan@nopCommerce.com")
        self.search_cust.clickonsearch()
        time.sleep(5)
        status = self.search_cust.searchbyemail("james_pan@nopCommerce.com")
        assert True == status
        self.logger.info("******Test_004_SearchCustomer End*******")
        self.driver.close()




