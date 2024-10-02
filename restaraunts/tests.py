import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user():
    return User.objects.create_user(username="testuser", password="password")


def test_create_restaurant(api_client, user):
    api_client.force_authenticate(user=user)
    response = api_client.post("/api/v1/restaurants/", {"name": "Test Restaurant", "location": "Test Location"})
    assert response.status_code == 201
