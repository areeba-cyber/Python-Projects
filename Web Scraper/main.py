from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
   content =  html_file.read()

   soup = BeautifulSoup(content, 'lxml')
   # tags = soup.find('h5')
   courses_html_tags = soup.find_all('h5')