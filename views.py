import datetime

from framework import render_
from logging_mod import Logger, debug

logger = Logger('main')


def about_view(request):
    return '200 OK', render_('about.html')


@debug
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
    return '200 OK', render_('index.html')


@debug
class Other:
    def __call__(self, request):
        return '404 WHAT', render_('page_404.html')

