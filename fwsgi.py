from wavy.templates import render_

# page controller
def index_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='none')


def black_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='black')

def red_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='red')

def white_view(request):
    print(request)
    return '200 OK', render_('index.html', color_name='white')

def not_found_404_view(request):
    print(request)
    return '404 WHAT', [b'404 UNKNOWN COLOR!!!!!!1']


class Other:
    def __call__(self, request):
        return '200 OK', render_('index.html', color_name='other color')


routes = {
    '/': index_view,
    '/black/': black_view,
    '/red/': red_view,
    '/white/': white_view,
    '/other/': Other()
}


# Front controllers
def opposite_color_front(request):
    request['opposite_color'] = 'opposite color'


def similar_color_front(request):
    request['similar_color'] = 'similar color'


fronts = [opposite_color_front, similar_color_front]


class Application:

    def __init__(self, routes, fronts):
        self.routes = routes
        self.fronts = fronts

    def __call__(self, environ, start_response):
        """
            :param environ: словарь данных от сервера
            :param start_response: функция для ответа серверу
        """
        # сначала в функцию start_response передаем код ответа и заголовки
        # print(type(environ))
        # print(environ)
        print('working...')
        path = environ['PATH_INFO']
        view = not_found_404_view
        if path in self.routes:
            view = self.routes[path]
        request = {}
        # front controller
        for front in self.fronts:
            front(request)

        code, body = view(request)
        start_response(code, [('Content-Type', 'text/html')])
        # возвращаем тело ответа в виде списка из bite
        return body.encode('utf-8')


application = Application(routes, fronts)

# uwsgi --http :8000 --wsgi-file fwsgi.py
