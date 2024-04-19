from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer

@api_view(['GET'])
def directors(request):
    directors = Director.objects.all()
    serializer = DirectorSerializer(directors, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def director_detail(request, id):
    director = Director.objects.get(id=id)
    direc = DirectorDetailSerializer(director, many=False)

    return Response(direc.data)

@api_view(['GET'])
def movies(request):
    movies = Movie.objects.all()
    serializermov = MovieSerializer(movies, many=True)

    return Response(serializermov.data)


@api_view(['GET'])
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    mov = MovieDetailSerializer(movie, many=False)

    return Response(mov.data)

@api_view(['GET'])
def reviews(request):
    reviews = Review.objects.all()
    serializerrev = ReviewSerializer(reviews, many=True)

    return Response(serializerrev.data)


@api_view(['GET'])
def review_detail(request, id):
    review = Review.objects.get(id=id)
    rev = ReviewDetailSerializer(review, many=False)

    return Response(rev.data)
