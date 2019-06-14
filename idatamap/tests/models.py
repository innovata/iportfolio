
from django.test import TestCase
from datamap.models import Keyword

# Create your tests here.


class KeywordTestCase(TestCase):
    def setUp(self):
        Keyword.objects.create(keyword="lion", freq='100')
        Keyword.objects.create(keyword="cat", freq='50')

    def test__init(self):
        lion = Keyword.objects.get(keyword='lion')
        print(lion.__str__)
