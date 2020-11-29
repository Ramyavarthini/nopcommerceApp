import time
from selenium.webdriver.support.ui import Select

class AddCustomer:
    lnk_customermenu_xpath = "//a[@href='#']//span[text()='Customers']"
    link_customer_menuitem_xpath = "//span[@class='menu-item-title' and text()='Customers']"
    btn_addnew_xpath = "//a[@href='/Admin/Customer/Create']"

    txt_email_name = "Email"
    txt_password_id = "Password"
    txt_firstname_id = "FirstName"
    txt_lastname_id = "LastName"
    rd_male_id = "Gender_Male"
    rd_female_id = "Gender_Female"
    txt_dob_xpath = "//input[@id='DateOfBirth']"
    txt_company_id = "Company"
    chk_istaxexempt_id = "IsTaxExempt"
    txt_newsletter_xpath = "//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']//parent::div[@class='k-multiselect-wrap k-floatwrap']"
    txt_customerroles_xpath = "//ul[@id='SelectedCustomerRoleIds_taglist']//parent::div[@class='k-multiselect-wrap k-floatwrap']"
    lstitem_administrators_xpath = "//li[text()='Administrators']"
    lstitem_forummoderators_xpath = "//li[text()='Forum Moderators']"
    lstitem_guest_xpath = "//li[text()='Guests']"
    lstitem_registered_xpath = "//li[text()='Registered']"
    lstitem_vendors_xpath = "//li[text()='Vendors']"
    menu_mgrofvendor_id = "VendorId"
    txtarea_admincomment_id = "#AdminComment"

    btn_save_xpath = "//button[@name='save']"

    def __init__(self,driver):
        self.driver = driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.lnk_customermenu_xpath).click()

    def clickOnCustomersMenuItem(self):
        self.driver.find_element_by_xpath(self.link_customer_menuitem_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element_by_xpath(self.btn_addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_name(self.txt_email_name).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_id(self.txt_password_id).send_keys(password)

    def setFirstName(self,fname):
        self.driver.find_element_by_id(self.txt_firstname_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element_by_id(self.txt_lastname_id).send_keys(lname)

    def clickOnGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.rd_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.rd_female_id).click()
        else:
            self.driver.find_element_by_id(self.rd_male_id).click()

    def setDob(self,dob):
        self.driver.find_element_by_xpath(self.txt_dob_xpath).send_keys(dob)

    def setCompanyName(self,companyname):
        self.driver.find_element_by_id(self.txt_company_id).send_keys(companyname)

    def clickOnTaxExempt(self):
         self.driver.find_element_by_id(self.chk_istaxexempt_id).click()

    def setNewsLetter(self,newsletter):
        self.driver.find_element_by_xpath(self.txt_newsletter_xpath).send_keys(newsletter)

    def setCustomerRole(self,role):
        self.driver.find_element_by_xpath(self.txt_customerroles_xpath).click()
        time.sleep(5)
        if role == "Administrators":
            self.driver.find_element_by_xpath(self.lstitem_administrators_xpath).click()
        elif role == "Forum Moderators":
            self.driver.find_element_by_xpath(self.lstitem_forummoderators_xpath).click()
        elif role == "Vendors":
            self.driver.find_element_by_xpath(self.lstitem_vendors_xpath).click()
        elif role == "Guests":
            self.driver.find_element_by_xpath("//span[text()='Registered' and @unselectable='on']").click()
            time.sleep(5)
            self.driver.find_element_by_xpath(self.lstitem_guest_xpath).click()
        elif role == "Registered":
            self.driver.find_element_by_xpath(self.lstitem_registered_xpath).click()

    def setManagerOfVendor(self,value):
            sel = Select(self.driver.find_element_by_id(self.menu_mgrofvendor_id))
            sel.select_by_value(value)

    def setAdminComment(self,comment):
            self.driver.find_element_by_id(self.txtarea_admincomment_id).send_keys(comment)

    def clickOnSavebtn(self):
            self.driver.find_element_by_xpath(self.btn_save_xpath).click()