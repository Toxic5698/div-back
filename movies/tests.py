from django.test import TestCase
from .models import Movie
import json


class TestMovieAPI(TestCase):

    def setUp(self):
        Movie.objects.create(name='Movie 1', rate=25)
        Movie.objects.create(name='Movie 2', rate=50)
        Movie.objects.create(name='Movie 3', rate=75)

    def test_get_movies(self):
        response = self.client.get('/get-all')
        assert response.status_code == 200
        self.assertEqual(response.json()["count"], 3)

    def test_create_movie(self):
        data = {'name': 'New Movie', 'rate': 5}
        response = self.client.post('/save', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200
        assert Movie.objects.filter(name='New Movie').exists()

    def test_update_movie(self):
        data = {'name': 'Updated Name', 'rate': 8}
        response = self.client.patch('/update/2', data=json.dumps(data), content_type='application/json')
        assert response.status_code == 200
        assert Movie.objects.filter(name='Updated Name', rate=8).exists()

    def test_delete_movie(self):
        movie_id = 2
        response = self.client.delete(f'/delete/{movie_id}')
        assert response.status_code == 200
        assert not Movie.objects.filter(id=movie_id).exists()

    def test_get_stats(self):
        response = self.client.get('/stats')
        assert response.status_code == 200
        self.assertEqual(response.json()["highest_rate"], 75)

    def test_search_by_name(self):
        response = self.client.get('/get-all?name=2')
        assert response.status_code == 200
        self.assertEqual(response.json()["items"][0]["name"], "Movie 2")
