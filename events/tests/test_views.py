
import pytest
from rest_framework.test import APIClient
from django.urls import reverse
from .models import Event

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def create_event():
    def _create_event(**kwargs):
        return Event.objects.create(**kwargs)
    return _create_event

def test_event_creation(api_client):
    response = api_client.post(reverse('event-list'), {
        "title": "Test Event",
        "description": "This is a test event.",
        "date": "2024-01-01T10:00:00Z",
        "location": "Test Location"
    })
    assert response.status_code == 201

def test_event_retrieval(api_client, create_event):
    event = create_event(title="Sample", description="Desc", date="2024-01-01T10:00:00Z", location="Loc")
    response = api_client.get(reverse('event-detail', args=[event.id]))
    assert response.status_code == 200
    assert response.data['title'] == "Sample"
