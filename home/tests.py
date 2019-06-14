
from idatamap import PJT_PATH
import sys
sys.path.append(f"{PJT_PATH}/env/lib/python3.7/site-packages")
import django
from django.test import TestCase
from django.core.wsgi import get_wsgi_application
import os
os.environ["DJANGO_SETTINGS_MODULE"] = "iportfolio.settings"
application = get_wsgi_application()

# Create your tests here.

from home.models import Category

class CategoryTestCase(TestCase):
    def setUp(self):
        Category.objects.create(name="Tech", description="technology")
        Category.objects.create(name="Lang", description="language")

    def test__init(self):
        tech = Category.objects.get(name='Tech')
        print(tech.description)

c = CategoryTestCase()
c.setUp()
c.test__init()
