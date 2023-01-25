from rest_framework import serializers
from.models import Movie, Review, Director


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class DirectorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = 'id name'.split()


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie stars'.split()


class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = 'id text movie'.split()


class MovieSerializer(serializers.ModelSerializer):
    movie_reviews = ReviewSerializer(many=True)

    class Meta:
        model = Movie
        fields = 'id movie_reviews rating title description duration director'.split()


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = 'id title rating description duration director'.split()