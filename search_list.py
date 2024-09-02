from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


op = webdriver.ChromeOptions()
op.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=op)
driver.get('https://google.com')

driver.maximize_window()

# Location = "C:/Users/hp/Desktop/images"


Search_Tab = WebDriverWait(driver, 5).until(

    EC.presence_of_element_located((By.CLASS_NAME, 'nDcEnd'))
)



def Search_Image():

    Search_Tab.click()
    Search_Image_in = driver.find_element(By.CLASS_NAME, "DV7the")
    print(Search_Image_in.is_displayed())
    Search_Image_in.click()


def main():
    Search_Image()


main()







