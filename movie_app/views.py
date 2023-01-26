from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MovieDetailSerializer, MovieSerializer, ReviewSerializer, ReviewDetailSerializer,\
    DirectorSerializer, DirectorDetailSerializer
from .models import Movie, Review, Director
from rest_framework import status


@api_view(['GET', 'POST'])
def director_view(request):
    if request.method == 'GET':
        director = Director.objects.all()
        serializer = DirectorSerializer(director, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def director_detail_view(request, id):
    try:
        director = Director.objects.get(id=id)
    except Director.DoesNotExist:
        return Response(data={'error': 'Director not found!'},
                        status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = DirectorDetailSerializer(director, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        name = request.data.get('name')
        director.name = name
        director.save()
        return Response(data=DirectorDetailSerializer(director).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'POST'])
def review_view(request):
    if request.method == 'GET':
        review = Review.objects.all()
        serializer = ReviewSerializer(review, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review = Review.objects.create(text=text)
        review.movie.set(movie)
        review.stars.set(stars)
        review.save()
        return Response(data=ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_view(request, id):
    try:
        review = Review.objects.get(id=id)
    except Review.DoesNotExist:
        return Response(data={'error': 'Review not found!'},
                        status=404)
    if request.method == 'GET':
        serializer = ReviewDetailSerializer(review, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        text = request.data.get('text')
        movie = request.data.get('movie')
        stars = request.data.get('stars')
        review.text = text
        review.movie.set(movie)
        review.stars.set(stars)
        review.save()
        return Response(data=ReviewDetailSerializer(review).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET','POST'])
def movie_view(request):
    if request.method == 'GET':
        movie = Movie.objects.all()
        serializer = MovieSerializer(movie, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie = Movie.objects.create(title=title, description=description, duration=duration)
        movie.director.set(director)
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_view(request, id):
    try:
        movie = Movie.objects.get(id=id)
    except Movie.DoesNotExist:
        return Response(data={'error': 'Movie not found!'},
                        status=404)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie, many=False)
        return Response(data=serializer.data)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director = request.data.get('director')
        movie.title = title
        movie.description = description
        movie.duration = duration
        movie.director.set(director)
        movie.save()
        return Response(data=MovieDetailSerializer(movie).data,
                        status=status.HTTP_201_CREATED)
