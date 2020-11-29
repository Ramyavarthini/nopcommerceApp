import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test_001_Login:

    base_url = ReadConfig.getApplicationUrl()
    useremail = ReadConfig.getuseremail()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homepagetitle(self,setup):
        self.logger.info('*****Test_001_Login*****')
        self.logger.info('*****verifying homepage title*****')
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        act_title = self.driver.title
        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info('****** Home page title test is passed')
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepagetitle.png")
            self.driver.close()
            assert False
            self.logger.error('****** Home page title test is failed')

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info('****Verify login page******')
        self.driver = setup
        self.driver.get(self.base_url)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.useremail)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        print('ACTUAL TITLE===', act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info('*****Login verification passed*****')
            self.driver.close()

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            self.logger.error('*****Login verification failed*****')
            assert False


