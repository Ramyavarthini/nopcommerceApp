# import configparser
from configparser import ConfigParser

# config = configparser.RawConfigParser()
config = ConfigParser()
config.read("C:/Users/ramya/PycharmProjects/nopcommerceApp/Configurations/config.ini")


class ReadConfig:

    @staticmethod
    def getApplicationUrl():
        url = config['common info'].get('baseurl')
        #url = config.get('common info','baseurl')
        return url

    @staticmethod
    def getuseremail():
        useremail = config.get('common info','useremail')
        return useremail

    @staticmethod
    def getpassword():
        password = config.get('common info','password')
        return password


