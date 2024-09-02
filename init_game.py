from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=options)



Cookie_Count = None



driver.get('https://orteil.dashnet.org/cookieclicker/')


Lang_Select_Ele = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "langSelect-EN"))
)


Lang_Select_Ele.click()


Cookie_Clicker = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "bigCookie")))


def Get_Cookie_Count():
    Cookie_count_Ele = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cookies")))
    Cookie_Count = Cookie_count_Ele.text
    Cookie_Count = int(Cookie_Count.split(" ")[0])
    return Cookie_Count


def Buy_Shit():

    Product_price = "productPrice"
    Product_Name = "product"
    for i in range(4):
        product_price = driver.find_element(By.ID, Product_price + str(i)).text.replace(",", "")
       
        if not product_price.isdigit():
            continue    

        if Cookie_Count >= int(product_price):
            driver.find_element(By.ID, Product_Name + str(i)).click()
            break;



while True:
    Cookie_Clicker.click()
    Cookie_Count = Get_Cookie_Count()
    Buy_Shit()
