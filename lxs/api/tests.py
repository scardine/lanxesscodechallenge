from django.utils.datastructures import MultiValueDict
from rest_framework.test import APITransactionTestCase
from .models import *


DATA_PHILIPP_SARAH = MultiValueDict([
    ('id', [1, 2]),
])

DATA_PHILIPP_SARAH_CARL = MultiValueDict([
    ('id', [1, 2, 3]),
])

class AvailabilityTestCase(APITransactionTestCase):
    fixtures = [
        'api/fixtures/sample_data.json',
    ]
    def test_availabily_Philipp_Sarah(self):
        result = self.client.get('/api/availability/', data=DATA_PHILIPP_SARAH)
        self.assertEquals(result.data, [
            ("monday", 12),
            ("monday", 13),
            ("monday", 14),
            ("monday", 15),
            ("thursday", 9),
            ("thursday", 10),
            ("thursday", 11),
            ("tuesday", 9),
            ("tuesday", 10),
            ("tuesday", 11),
            ("wednesday", 12),
            ("wednesday", 13),
            ("wednesday", 14),
            ("wednesday", 15),
        ])

    def test_availabily_Philipp_Sarah_Carl(self):
        result = self.client.get('/api/availability/', data=DATA_PHILIPP_SARAH_CARL)
        self.assertEquals(result.data, [
            ('thursday', 9),
            ('tuesday', 9),
        ])
