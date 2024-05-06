from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Director, Movie, Review
from .serializers import DirectorSerializer, MovieSerializer, ReviewSerializer, DirectorDetailSerializer, MovieDetailSerializer, ReviewDetailSerializer,DirectorValidateSerializer,MovieValidateSerializer,ReviewValidateSerializer


@api_view(['GET', 'POST'])
def directors(request):
    if request.method == 'GET':
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True)

        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        name = serializer.validated_data.get('name')
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
        serializer = DirectorValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        director.name = serializer.validated_data.get('name')
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
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
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
        serializer = MovieValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description')
        duration = serializer.validated_data.get('duration')
        director_id = serializer.validated_data.get('director_id')
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
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        star = serializer.validated_data.get('star')
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
        serializer = ReviewValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        text = serializer.validated_data.get('text')
        movie_id = serializer.validated_data.get('movie_id')
        star = serializer.validated_data.get('star')
        review = Review.objects.create(text=text, star=star, movie_id=movie_id)
        review.save()
        return Response(data={'review_id': review.id}, status=status.HTTP_201_CREATED)
    elif request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
