import requests
from bs4 import BeautifulSoup
with open('C:/Users/Home PC/Desktop/Word game/buf.TXT','w', encoding="utf-8") as result_file:
    letter_response = requests.get("https://wooordhunt.ru" + "/dic/list/en_ru/co")
    letter_soup = BeautifulSoup(letter_response.text, "lxml")
    words = letter_soup.find_all('p')
    for j in words:
        print(j.find('a'))
        print('english_word', 'transcription', 'russian_word')
        print(j.find('a').string.strip() + '@' + j.find('a').next_sibling.split(' — ')[0].lstrip() +'@'+ j.find('a').next_sibling.split(' — ')[1])
        result_file.write(j.find('a').string.strip() + '@' + j.find('a').next_sibling.split(' — ')[0].lstrip() +'@'+ j.find('a').next_sibling.split(' — ')[1] + '\n')

