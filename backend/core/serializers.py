from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.ModelSerializer):
	"""docstring for TodoSerializer"""
	class Meta:
		model = Movie
		fields = ('id', 'title', 'plot', 'year', 'rating', 'runtime', 'website')