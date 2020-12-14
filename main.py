import views

from framework.templates import render_
from framework import Application



routes = {
    '/': views.index_view,
    '/black/': views.black_view,
    '/red/': views.red_view,
    '/white/': views.white_view,
    '/other/': views.Other(),
    '/about/': views.about_view,
    '/contact/': views.contact_view,
    '/random/': views.random_view
}


# Front controllers
def opposite_color_front(request):
    request['opposite_color'] = 'opposite color'


def similar_color_front(request):
    request['similar_color'] = 'similar color'

fronts = [opposite_color_front, similar_color_front]
application = Application(routes, fronts)

# uwsgi --http :8000 --wsgi-file fwsgi.py
