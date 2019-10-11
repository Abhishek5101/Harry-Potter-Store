from unittest import TestCase, main as unittest_main, mock
from bson.objectid import ObjectId
from app import app


class contractorTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """ to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True

    def test_index(self):
        """Test the contractor homepage."""
        result = self.client.get('/')
        self.assertEqual(result.status, '200 OK')

    def test_about(self):
        result = self.client.get('/about')
        self.assertEqual(result.status, '200 OK')

    def test_new(self):
        """Test the new creation page."""
        result = self.client.get('/magics/new')
        self.assertEqual(result.status, '200 OK')
    
    def test_magic(self):
        result = self.client.get('/magics')
        self.assertEqual(result.status, '200 OK')


if __name__ == '__main__':
    unittest_main()
