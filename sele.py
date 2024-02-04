
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup


def toSoup(html):
    soup = BeautifulSoup(html.get_attribute('outerHTML'), 'html.parser')
    print(soup.prettify())

option = Options()
option.add_experimental_option('detach', True)


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

driver.get('https://igetintopc.com/software-categories/')
driver.maximize_window()

search_bar = driver.find_element(by='name', value='s')
search_bar.send_keys('after effect')
search_bar.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
main_div = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'posts.clear-block')))

All_Post = main_div[0].find_elements(By.CLASS_NAME, value='post-details')

for post in All_Post:
    title = post.find_element(By.CLASS_NAME, value='title')
    Desc = post.find_element(By.CLASS_NAME, value='post-content')
    with open('software_Title_Desc.txt', 'w') as f:
        f.write(title.text)
        f.write(Desc.text)
        f.write('\n\n')
          


