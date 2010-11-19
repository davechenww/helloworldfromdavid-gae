import os

from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class Index(webapp.RequestHandler):
    def get(self):
        greetings_query = Greeting.all().order('-date')
        latest_greetings = greetings_query[:5]
        more_greetings = greetings_query[5:greetings_query.count()]

        if users.get_current_user():
            current_user = users.get_current_user()
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            current_user = ''
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'latest_greetings': latest_greetings,
            'more_greetings': more_greetings,
            'current_user': current_user,
            'url': url,
            'url_linktext': url_linktext,
            }

        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class Sign(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        if greeting.content:
            greeting.put()
        self.redirect('/')
