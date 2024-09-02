from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


# Login id 

User_name_input = "session_key"
User_pass_input = "session_password"



option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=option)

driver.get('https://www.linkedin.com/jobs/')


def Login(Email="rihog12211@facais.com", Password="LousyLinkedIn1@"):

    User_Ele = driver.find_element(By.ID, User_name_input)
    Pass_Ele = driver.find_element(By.ID, User_pass_input)
    Login_btn = driver.find_element(By.CLASS_NAME, "btn-md.btn-primary.flex-shrink-0.cursor-pointer.sign-in-form__submit-btn--full-width")

    User_Ele.send_keys(Email)
    Pass_Ele.send_keys(Password)

    Login_btn.click()



def Job_Search():

    Show_btn = driver.find_element(By.CLASS_NAME, "discovery-templates-vertical-list__footer")
    Show_btn.click()

    


def main():
    Login()


main()