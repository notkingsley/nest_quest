from django.test import TestCase
from users.models import User
from django.urls import reverse
from rest_framework import status
from .serializers import LandlordSerializer, PhoneNumberSerializer
from rest_framework.test import APITestCase

from .models import Landlord

class LandlordTests(APITestCase):
    
    def setUp(self):
        # test to create a user
        self.user = User.objects.create(username='user1', email='@12fasdlkjh')
        self.client.force_authenticate(user=self.user)

    def test_create(self):
        url = reverse("create_landlord")
        landlord = Landlord.objects.create(
            user = self.user,
            phone_number = "07062617961",
            address = "oau",
            )
        data = {
            "user": self.user,
            "phone_number": "07062617961",
            "address": "oau",
        }
        response = self.client.post(url, data, json=format)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Landlord.objects.count(), 1)
        self.assertEqual(Landlord.objects.get().address, "oau")

    def test_get_landlord(self):
        landlord = Landlord.objects.create(
            user = self.user,
            phone_number = "07062617961",
            address = "oau",
            )
        url = reverse("landlord_info")
        response = self.client.get(url)
        serializer = LandlordSerializer(landlord)
        self.assertEqual(response.data,serializer.data)

    def test_update_landlord(self):
        url = reverse("landlord_info")
        landlord = Landlord.objects.create(
            user = self.user,
            phone_number = "07062617961",
            address = "oau",
            )
        data = {
            'email': 'janedoe@exampldfd.com' 
            }
        response = self.client.patch(url, data)
        serializer = LandlordSerializer(landlord, data=data, partial=True)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(response.data, serializer.data)

    def test_validate_phone_number(self):
        phone_number = '08012345678'
        validated_phone_number = PhoneNumberSerializer().validate_phone_number(phone_number)
        self.assertEqual(validated_phone_number, phone_number)