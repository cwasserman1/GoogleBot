from selenium import webdriver
import sys
print("Create GoogleBot")
print(sys.argv)


class googlebot:
    def __init__(self,firstname,lastname,username,password,phonenumber):
        self.firstname = firstname
        self.lastname = lastname
        self.username = username
        self.password = password
        self.phonenumber = phonenumber
    def createAccount(self):
        css_dict = {'firstName':'#firstName',''}
        browser = webdriver.Firefox(executable_path = r'C:\Users\colew\OneDrive\Desktop\GeckoDriver\geckodriver.exe')
        browser.get('https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp')
        first_name_button = browser.find_element_by_css_selector('#firstName')
        first_name_button.click()
        first_name_button.send_keys(self.firstname)
        last_name_button = browser.find_element_by_css_selector('#lastName')
        last_name_button.send_keys(self.lastname)
        username_button = browser.find_element_by_css_selector('#username')
        username_button.send_keys(self.username)
        password_button = browser.find_element_by_css_selector('#passwd > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        password_button.send_keys(self.password)
        confirm_button = browser.find_element_by_css_selector('#confirm-passwd > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > input:nth-child(1)')
        confirm_button.send_keys(self.password)
        current = browser.find_element_by_css_selector('.RveJvd')
        current.click()
        current = browser.find_element_by_css_selector('#phoneNumberId')
        current.send_keys(self.phonenumber)
        current = browser.find_element_by_css_selector('.RveJvd')
        current.click()
NewUser = googlebot([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]])
NewUser.createAccount()
print([sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4]])
