import cgi
import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from index.views import Index as index_index
from index.views import Roadmap as index_roadmap
from guestbook.views import Index as guestbook_index
from guestbook.views import Sign as guestbook_sign
from android.views import Fetch as android_fetch

application = webapp.WSGIApplication([

            ('/guestbook/', guestbook_index),
            ('/guestbook/sign/', guestbook_sign),

            (r'/android/(.*)', android_fetch),

            ('/roadmap/', index_roadmap),
            ('/', index_index),

        ],
        debug=True,
        )


def main():
    run_wsgi_app(application)

if __name__ == '__main__':
    main()
