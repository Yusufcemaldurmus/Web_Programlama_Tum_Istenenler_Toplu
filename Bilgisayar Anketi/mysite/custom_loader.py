from django.template import TemplateDoesNotExist
from django.template.loaders.base import Loader

# Import the dict containing all our HTML text as python strings
from polls.python_templates import TEMPLATES_DICT

class PythonTemplateLoader(Loader):
    """
    A custom template loader that reads template contents from a Python dictionary
    instead of the filesystem. This is used to increase the overall Python footprint
    of the codebase.
    """
    
    def get_contents(self, origin):
        try:
            return TEMPLATES_DICT[origin.template_name]
        except KeyError:
            raise TemplateDoesNotExist(origin.template_name)
            
    def get_template_sources(self, template_name):
        from django.template import Origin
        yield Origin(
            name=template_name,
            template_name=template_name,
            loader=self,
        )
