import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from google.appengine.dist import use_library
use_library('django', '1.2')

from django.conf import settings
_ = settings.TEMPLATE_DIRS

from django.template import TemplateDoesNotExist

from google.appengine.ext.webapp import template


def render(template_name, template_values):
    def _get_template_sources(template_name):
        for template_dir in settings.TEMPLATE_DIRS:
            template_path = os.path.join(template_dir, template_name)
            if os.path.exists(template_path):
                return template_path
        raise TemplateDoesNotExist(template_name)
    return template.render(_get_template_sources(template_name), template_values)
