from framework import render_
import json
import requests
import datetime

def about_view(request):
    # Просто возвращаем текст
    return '200 OK', render_('about.html')


def contact_view(request):
    # Проверка метода запроса
    if request['method'] == 'POST':
        now = datetime.datetime.now()
        data = request['data']
        title = data['title']
        text = data['text']
        email = data['email']
        print(f'Нам пришло сообщение от {email} с темой {title} и текстом {text}')
        with open(f'messages/message_{now.strftime("%d%m%Y")}_{now.strftime("%H.%M.%S")}.txt', 'w') as message_file:
            message_file.write(f'Нам пришло сообщение от {email} с темой \n {title} \n и текстом \n {text}')
        return '200 OK', render_('contacts.html')
    else:
        return '200 OK', render_('contacts.html')

def index_view(request):
    print(request)
    return '200 OK', render_('index.html')


def black_view(request):
    print(request)
    return '200 OK', render_('color.html', color_name='black')

def red_view(request):
    print(request)
    return '200 OK', render_('color.html', color_name='red')

def white_view(request):
    print(request)
    return '200 OK', render_('color.html', color_name='white')

# def not_found_404_view(request):
#     print(request)
#     return '404 WHAT', [b'404 UNKNOWN COLOR!!!!!!1']

def random_view(request):
    print(request)
    answer = requests.get('http://www.colr.org/json/color/random')
    color_name = answer.json()['colors'][0]['tags'][0]['name']
    return '200 OK', render_('color.html', color_name=color_name)

class Other:
    def __call__(self, request):
        return '200 OK', render_('color.html', color_name='Что-то другое')

