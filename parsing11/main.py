from itertools import count
from tkinter.font import names

import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []  #формируем список

headers = {"User Agent":	"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36"} #юзер агента найти на сайте 2ip во вкладке инфо о браузере

for count in range(1,7):        # для переменной count подставляем значения от 1 до 7, номера страниц
    sleep(3) #установили задержку в 3 сек, что быть менее похожим на робот
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}" #сделали Ф строку в {значение страницы} указывается ссылка на парсируемую страницу

    response = requests.get(url, headers=headers) # создали переменную headers в нее помещаем информацию юзер агента, то что мы даем браузеру

    soup = BeautifulSoup(response.text,"lxml") #html.parser переключить если один из двух не сработает lxml html.parser

    data = soup.find_all("div", class_= "w-full rounded border") # в переменной data инициализируется либрери bs4 командой soup, find_all вытаскивает все карточки товара у которых класс=
for i in data:
    card_url = "https://scrapingclub.com" + i.find("a").get("href") #при использовании find прога обращает внимание на первый искомый тег, метод get берет информацию из href
    #также добавили базовый домен сайта, что бы ссылка выдаваемая в переменной card_list стала обсалютной
    list_card_url.append(card_url) #Метод append() в Python добавляет в конец списка элемент, переданный ему в качестве аргумента.
#Этот метод позволяет добавлять элементы в список, при этом не создавая новый список и не изменяя его текущие элементы и их индексы.


    #name = i.find("div", class_="p-4").text.replace("$24.99","") #вывод всего кроме 24бакса
    #price = i.find("h5").text
    #url_img= "https://scrapingclub.com" + i.find("img",class_="card-img-top img-fluid").get("src") #сложение двух строк корневая ссылка сайта и относительная картинки
    #print(name + "\n" + price + "\n" + url_img +"\n\n")
for card_url in list_card_url:
    response = requests.get(url, headers=headers)  # создали переменную headers в нее помещаем информацию юзер агента, то что мы даем браузеру

    soup = BeautifulSoup(response.text,"lxml")  # html.parser переключить если один из двух не сработает lxml html.parser

    data = soup.find("div", class_="w-full rounded border")  # в переменной data инициализируется либрери bs4 командой soup, find_all вытаскивает все карточки товара у которых класс=
    print (data)