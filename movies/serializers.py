import datetime
from rest_framework import serializers
from django.db.models import Avg
from movies.models import Movie
from actors.serializers import ActorSerializer
from genres.serializers import GenreSerializer

class MovieListDetailSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True)
    genre  = GenreSerializer()
    rate = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 2) if rate is not None else 0.0
    
    def validate_release_date(self, value):
        """
        Check that the release date is not in the future.
        """
        if value > datetime.date.today():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value


class MovieModelSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        return round(rate, 2) if rate is not None else 0.0
        # reviews = obj.reviews.all()

        # if reviews:
        #     sum_reviews = 0
        #     for review in reviews:
        #         sum_reviews += review.stars

        #     reviews_count = reviews.count()

        #     return round(sum_reviews / reviews_count, 2)

        # return 0.0

    def validate_release_date(self, value):
        """
        Check that the release date is not in the future.
        """
        if value > datetime.date.today():
            raise serializers.ValidationError("Release date cannot be in the future.")
        return value
