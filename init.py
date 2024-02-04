import requests
from bs4 import BeautifulSoup

url = 'https://www.codewithharry.com/'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# course_tab = soup.find_all(class_=['max-w-sm', 'rounded-2xl', 'overflow-hidden', 'shadow-lg', 'dark:bg-slate-800'])
# target_elements = soup.find(class_='title-font flex text-lg font-medium text-gray-900 mb-3 dark:text-white')


# course_titles = soup.select('.title-font.flex.text-lg.font-medium.text-gray-900.mb-3.dark\\:text-white')

# print(course_titles[0].prettify())

course_desc = soup.select('.text-gray-700.text-base.dark\\:text-gray-400')

for all_desc in course_desc:
    print('------------')
    print(all_desc.getText())