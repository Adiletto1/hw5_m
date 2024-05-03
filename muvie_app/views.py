from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer

@api_view(['GET', 'POST'])
def directors(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        name = request.data.get('name')
        director = Director.objects.create(name=name)
        director.save()
        return Response(data={'director_id': director.id}, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def director_detail(request, id):
    director = Director.objects.get(id=id)
    if request.method == 'GET':
        direc = DirectorDetailSerializer(director, many=False)
        return Response(direc.data)
    elif request.method == 'PUT':
        director.name = request.data.get('name')
        director.save()
        return Response(data=DirectorDetailSerializer(director).data, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        director.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




@api_view(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializermov = MovieSerializer(movies, many=True)

        return Response(serializermov.data)
    elif request.method == 'POST':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)



@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == 'GET':
        mov = MovieDetailSerializer(movie, many=False)

        return Response(mov.data)
    elif request.method == 'PUT':
        title = request.data.get('title')
        description = request.data.get('description')
        duration = request.data.get('duration')
        director_id = request.data.get('director_id')
        movie = Movie.objects.create(title=title, description=description, duration=duration, director_id=director_id)
        movie.save()
        return Response(data={'movie_id': movie.id}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def reviews(request):
    if request.method == 'GET':
        reviews = Review.objects.all()
        serializerrev = ReviewSerializer(reviews, many=True)

        return Response(serializerrev.data)
    elif request.method == 'POST':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        star = request.data.get('star')
        review = Review.objects.create(text=text, star=star, movie_id=movie_id)
        review.save()
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def review_detail(request, id):
    review = Review.objects.get(id=id)
    if request.method == 'GET':
        rev = ReviewDetailSerializer(review, many=False)

        return Response(rev.data)
    elif request.method == 'PUT':
        text = request.data.get('text')
        movie_id = request.data.get('movie_id')
        star = request.data.get('star')
        review = Review.objects.create(text=text, star=star, movie_id=movie_id)
        review.save()
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
