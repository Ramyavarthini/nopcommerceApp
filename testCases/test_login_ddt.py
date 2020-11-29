import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_001_Login:

    # base_url = ReadConfig.getApplicationUrl()
    file_path = ".//TestData/LoginData.xlsx"
    logger = LogGen.loggen()

    def test_login(self,setup):
        self.logger.info('****Verify login page******')
        # self.driver = setup
        # self.driver.get(self.base_url)
        self.rowcount = XLUtils.getRowCount(self.file_path,'Sheet1')
        print('RowCount====',self.rowcount)
        lp_status = []

        for r in range(2,self.rowcount):
            base_url = ReadConfig.getApplicationUrl()
            self.driver = setup
            self.driver.get(base_url)
            user = XLUtils.readData(self.file_path,'Sheet1',r,1)
            pwd = XLUtils.readData(self.file_path, 'Sheet1', r, 2)
            result = XLUtils.readData(self.file_path, 'Sheet1', r, 3)

            self.lp = LoginPage(self.driver)
            self.lp.setusername(user)
            self.lp.setpassword(pwd)
            self.lp.clicklogin()
            time.sleep(5)

            act_title = self.driver.title
            if act_title == "Dashboard / nopCommerce administration":
                if result == 'Pass':
                    # self.logger.info('*****Login DDT verification passed*****')
                    self.lp.clicklogout()
                    lp_status.append("passed")
                    self.driver.close()
                elif self.result == 'Fail':
                    # self.logger.info('*****Login DDT verification failed*****')
                    self.lp.clicklogout()
                    lp_status.append('failed')
                    self.driver.close()
            elif act_title != "Dashboard / nopCommerce administration":
                if self.result == 'Pass':
                    # self.logger.info('*****Login DDT verification passed*****')
                    self.lp.clicklogout()
                    lp_status.append("failed")
                    self.driver.close()
                elif self.result == 'Fail':
                    # self.logger.info('*****Login DDT verification passed*****')
                    self.lp.clicklogout()
                    lp_status.append('passed')
                    self.driver.close()
            if 'failed' not in lp_status:
                # self.logger.info("Login DDT testcase Pass")
                # self.driver.close()
                assert True
            else:
                # self.logger.info("Login DDT testcase Fail")
                # self.driver.close()
                assert False
        print('List Status===',lp_status)
        self.logger.info('******END OF DDT TESTCASE*******')