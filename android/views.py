import re
import urlparse

from google.appengine.api import urlfetch
from google.appengine.ext import webapp

BASE_URL = 'http://developer.android.com/'

def _url_filter(content, path, link_re):
    def _url_sub(m):
        link = m.group(2).strip()
        if link.startswith('/'):
            if not link.startswith('//'):
                link = '/android' + link
        elif not link.startswith('http'):
            link = urlparse.urljoin('/android/' + path, link)
        return m.group(1) + link + m.group(3)
    return link_re.sub(_url_sub, content)

class Fetch(webapp.RequestHandler):
    def get(self, path):
        if not path:
            path = '/'
        url = urlparse.urljoin(BASE_URL, path)
        try:
            result = urlfetch.fetch(url)
            for key in result.headers:
                self.response.headers[key] = result.headers[key]
            if 'content-type' in result.headers:
                if result.headers['content-type'].find('text/html') >= 0:
                    link_re = re.compile(r'(href=[^"]*"|src=[^"]*")([^"]*)(")', re.S)
                    result = _url_filter(result.content, path, link_re)
                elif result.headers['content-type'].find('text/css') >= 0:
                    link_re = re.compile(r'''(url\(['"]?)([^'")]*)(['"]?\))''', re.S)
                    result = _url_filter(result.content, path, link_re)
                else:
                    result = result.content
            else:
                result = result.content
        except Exception, e:
            result = str(e)
            self.response.set_status(500)
        self.response.out.write(result)
