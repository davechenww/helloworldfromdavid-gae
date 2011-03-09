from google.appengine.api import users
from google.appengine.ext import db
from google.appengine.ext import webapp

from util import template


class Greeting(db.Model):
    author = db.UserProperty()
    content = db.StringProperty(multiline=True)
    date = db.DateTimeProperty(auto_now_add=True)

class Index(webapp.RequestHandler):
    def get(self):
        greetings = Greeting.all().order('-date')[:5]

        if users.get_current_user():
            current_user = users.get_current_user()
            url = users.create_logout_url(self.request.uri)
            url_linktext = 'Logout'
        else:
            current_user = ''
            url = users.create_login_url(self.request.uri)
            url_linktext = 'Login'

        template_values = {
            'greetings': greetings,
            'current_user': current_user,
            'url': url,
            'url_linktext': url_linktext,
        }
        self.response.out.write(template.render('guestbook_index.html', template_values))

class Sign(webapp.RequestHandler):
    def post(self):
        greeting = Greeting()

        if users.get_current_user():
            greeting.author = users.get_current_user()

        greeting.content = self.request.get('content')
        if greeting.content:
            greeting.put()
        self.redirect('/guestbook/')
