import time

from bs4 import BeautifulSoup
import requests

while True:
    LIST = {}
    url = 'http://ratingcheck.ru/itmo_Infokommunikatsionnyetehnologiiisistemysvjazi.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allabits = soup.findAll('tr', class_='table__row table__row-slider')
    for abit in allabits:
        snils = abit.find('td', class_='table__data_slider-elem').text.strip()
        orig = abit.find('td', class_='table__head_narrow').text.strip()
        LIST[snils] = orig

    url = 'https://abit.itmo.ru/ranking/bachelor/budget/1808'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    allabits = soup.findAll('div', class_='RatingPage_table__FbzTn')
    abiturients = []
    zelenix = 0
    mogut_pomeshat = 0
    for abit in allabits[4]:
        abit = abit.find('div', class_='RatingPage_table__item__qMY0F')
        color = abit.get('class')
        if len(color) == 2:
            if color[1][-5:] == 'QR1Ww':
                color = 'сер'
            elif color[1][-5:] == 'InEVk':
                color = 'зел'
            else:
                color = 'жел'
        else:
            color = 'бел'
        num_v_list, snils = abit.find('p', class_='RatingPage_table__position__uYWvi').text.split()
        num_v_list, snils = int(num_v_list), snils[1:]
        if snils == '16226236445':
            break
        if 'F' in snils:
            snils = snils.replace('F', '').replace('-', '')
        if color not in ['сер', 'зел']:
            orig = LIST[snils]
            if orig != 'Нет, Другойуниверситет':
                print(num_v_list, snils)
                mogut_pomeshat += 1
        elif color == 'зел':
            orig = 'итмо'
            zelenix += 1

    TOKEN = "5482242421:AAEuN-wuEryNH-oyime_Fw0roQ7WZeutFVc"
    chat_id = "481317616"
    message = f'зелёных - {zelenix}\nмогут помешать - {mogut_pomeshat}\nосталось мест:{65-8-7-zelenix}'
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    print(requests.get(url).json())
    time.sleep(60*60)
