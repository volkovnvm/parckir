from requests import get # импортируем requests для возможности отправки запросов по http
from requests.utils import unquote, quote #расшифровываем имя файла
from bs4 import BeautifulSoup # импортируем пакет для анализа документов html и xml
#запускаем цикл для парсинга ссылок на необходимые нам файлы на странице
page = input('Введите ссылку страницы с которой необходимо скачать файлы\n')
for link in BeautifulSoup(get(page).text, 'html.parser').find_all('a'): 
    tag = link.get('href') #href - тег с ссылками на файлы
    try:
        download_link = page + quote(tag) #получаем собственно ссылки на скачивание         
        open(unquote(tag), 'wb').write(get(page + quote(tag)).content) #записываем файл в папку с скриптом
    except Exception as E:
        print('Error: cant get file!\n', E)
