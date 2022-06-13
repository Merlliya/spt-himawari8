#подключение библиотек
import requests
import ctypes
import os
from PIL import Image
from win32api import GetSystemMetrics


def req(link, name): #фунция отправки запросов
    answer = requests.get(link).content #ответ от запроса
    with open(name, 'wb') as handler:
        handler.write(answer) #сохранение изображения получаемого в ответе запроса

req("https://anzu.sinc.ad.jp/himawari/img/FULL_24h/BlueMarble/1d/770/BlueMarble_0_0.png", "1.png") #вызов функции для получения первого изображения
req("https://jh170034-2.kudpc.kyoto-u.ac.jp/img/FULL_24h/B13/1d/550/2022/06/12/092000_0_0.png", "2.png") #вызов функции для получения второго изображения
image1 = Image.open('1.png').convert('RGBA') #конвертация изображения в прозрачный RGB
image2 = Image.open('2.png').convert('RGBA').resize((image1.size[0], image1.size[1])) #конвертация изображения в прозрачный RGB и изменение размера