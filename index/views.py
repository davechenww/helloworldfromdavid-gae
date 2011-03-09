from google.appengine.ext import webapp

from util import template


class Http404(webapp.RequestHandler):
    def get(self):
        request_url = self.request.path
        if self.request.query_string:
            request_url += '?' + self.request.query_string
        template_values = {
            'request_url': request_url,
        }
        self.response.set_status(404)
        self.response.out.write(template.render('index_404.html', template_values))

class Index(webapp.RequestHandler):
    def get(self):
        template_values = {
            'is_index_page': True,
        }
        self.response.out.write(template.render('index_index.html', template_values))

class Roadmap(webapp.RequestHandler):
    def get(self):
        template_values = {}
        self.response.out.write(template.render('index_roadmap.html', template_values))
