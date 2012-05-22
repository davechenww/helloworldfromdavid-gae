import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.3')

from django.conf import settings

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from index import views as index
from guestbook import views as guestbook
from android import views as android


def main():
    application = webapp.WSGIApplication(
        [
            (r'^/guestbook/$', guestbook.Index),
            (r'^/guestbook/sign/$', guestbook.Sign),

            (r'^/android/(.*)$', android.Fetch),

            (r'^/proxy/?.*$', index.Proxy),
            (r'^/roadmap/?$', index.Roadmap),
            (r'^/?$', index.Index),

            (r'^.*$', index.Http404),
        ],
        debug=settings.DEBUG,
    )
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
