import pytest
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from pageObjects.LoginPage import LoginPage
from pageObjects.AddCustomerPage import AddCustomer
import string
import random
import time

class Test_003_AddCustomer:
    base_url = ReadConfig.getApplicationUrl()
    username = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addcustomer(self,setup):
        # self.logger.info("*****test_AddCustomer started*****")
        # self.logger.info("*****Login Home Page******")
        self.driver = setup
        self.driver.get(self.base_url)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        # self.logger.info("*****Login HomePage Successfully*****")

        # self.logger.info("*****Add Customer Page started*********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItem()
        self.addcust.clickOnAddNew()

        self.logger.info("*****Adding Customer Info******")
        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("admin")
        self.addcust.setFirstName("Ramya")
        self.addcust.setLastName("Logamuthu")
        self.addcust.clickOnGender("Female")
        self.addcust.setDob("7/10/90")
        self.addcust.setCompanyName("BigCompany")
        # self.addcust.clickOnTaxExempt()
        # time.sleep(5)
        # self.addcust.setNewsLetter("This is todays news")
        # self.addcust.setCustomerRole("Administrators")
        # self.addcust.setManagerOfVendor("1")
        # self.addcust.setAdminComment("This comment is for testing")
        self.addcust.clickOnSavebtn()

        # self.logger.info("****End of Saving of saving information*******")
        # self.logger.info("*****Add customer validation*******")

        self.msg = self.driver.find_element_by_tag_name('body').text
        if "The new customer has been added successfully." in self.msg:
            assert True
            # self.logger.info("*******Test_003_AddCustomer Pass*******")
        else:
            assert False
            self.driver.save_screenshot(".\\Screenshots\\"+"text_add_customer.png")
            # self.logger.info("**********Test_003_AddCustomer Fail*******")

        self.driver.close()
        self.logger.info("*******Ending Test_003_AddCustomer*******")


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for c in range(size))




