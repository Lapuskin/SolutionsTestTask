import os

import django
from django.contrib.auth.models import User

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'apitask.settings')

django.setup()

from announcement_api.models import Announcement
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient


class TestMyAPI(TestCase):
    def setUp(self):
        user = User.objects.create(username='root')
        user.set_password('11111111')
        user.save()

        self.client = APIClient()
        self.client.login(username='root', password='11111111')

    def test_get_data_with_nothing_to_get(self):
        response = self.client.get(reverse('announcement', args=[1]))

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.data, {'detail': 'No Announcement matches the given query.'})
        self.assertEqual(response['Content-Type'], 'application/json')

    def test_get_data_by_id(self):
        obj = Announcement.objects.create(
            header='Установка Видеонаблюдение шлагбаум сигнализация обслуживание домофон',
            author='100 камер',
            views_count=100,
            position=1,
        )

        response = self.client.get(reverse('announcement', args=[1]))

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {
            'header': obj.header,
            'author': obj.author,
            'views_count': obj.views_count,
            'position': obj.position,
            'id': 1,
        }
                         )
        self.assertEqual(response['Content-Type'], 'application/json')


class TestAPIPermissions(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_is_authenticated_permission(self):
        response = self.client.get(reverse('announcement', args=[1]))

        self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})
        self.assertEqual(response.status_code, 403)
