class SearchCustomer:
    txt_searchemail_xpath = "//input[@id='SearchEmail']"
    txt_firstname_xpath = "//input[@id='SearchFirstName']"
    txt_lastname_xpath = "//input[@id='SearchLastName']"
    btn_search_xpath = "//button[@id='search-customers']"
    table_xpath = "//table[@id='customers-grid']"
    tablerows_xpath = "//table[@id='customers-grid']//tbody//tr"
    tablecolumn_xpath = "//table[@id='customers-grid']/tbody/tr[1]/td"

    def __init__(self,driver):
        self.driver = driver

    def setemail(self,email):
        self.driver.find_element_by_xpath(self.txt_searchemail_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_searchemail_xpath).send_keys(email)

    def setfirstname(self,firstname):
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_firstname_xpath).send_keys(firstname)

    def setlastname(self,lastname):
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.txt_lastname_xpath).send_keys(lastname)

    def clickonsearch(self):
         self.driver.find_element_by_xpath(self.btn_search_xpath).click()

    def getRowCount(self):
        return len(self.driver.find_elements_by_xpath(self.tablerows_xpath))

    def getColumnCount(self):
        return len(self.driver.find_elements_by_xpath(self.tablecolumn_xpath))

    def searchbyemail(self,email):
        flag = False
        for r in range(1,self.getRowCount()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            email_cell = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr['+str(r)+']/td[2]").text
            if email_cell == email:
                flag = True
                break
        return flag

    def searchbyname(self,name):
        flag = False
        for r in range(1,self.getColumnCount()+1):
            table = self.driver.find_element_by_xpath(self.table_xpath)
            name_cell = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr['+str(r)+']/td[3]").text
            if name_cell == name:
                flag = True
                break
        return flag