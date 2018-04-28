from django.test import TestCase
from .models import Person, Group


# Create your tests here.

class PersionGroupTest(TestCase):
    def testPersionAdd(self):
        # p = Person(name="张三")
        # p.save()
        persons = Person.objects.all()
        print(persons)

