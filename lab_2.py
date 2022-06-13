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