import os

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class Index(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'index.html')
        self.response.out.write(template.render(path, template_values))

class Roadmap(webapp.RequestHandler):
    def get(self):
        template_values = {}
        path = os.path.join(os.path.dirname(__file__), 'roadmap.html')
        self.response.out.write(template.render(path, template_values))
