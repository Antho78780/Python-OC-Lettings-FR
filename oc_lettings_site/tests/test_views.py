from django.test import TestCase, Client


class TestViews(TestCase):
    cient = Client()

    # def test_dummy():
    #     assert 1

    def test_view_index(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'index.html')
        self.assertEqual(response.status_code, 200)

    def test_error_404_view(self):
        pass
