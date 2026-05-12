import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from django.template.loader import render_to_string

try:
    content = render_to_string('polls/index.html')
    print("SUCCESS: length is", len(content))
except Exception as e:
    print("FAILED:", str(e))
