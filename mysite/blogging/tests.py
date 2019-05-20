from django.test import TestCase

# another import
from blogging.models import Category

# and the test case and test
class CategoryTestCase(TestCase):

    def test_string_representation(self):
        expected = "A Category"
        c1 = Category(name=expected)
        actual = str(c1)
        self.assertEqual(expected, actual)