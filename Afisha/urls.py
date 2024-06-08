from django.contrib import admin
from django.urls import path, include
from muvie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/directors/', views.DirectorListAPIView.as_view()),
    path('api/v1/directors/<int:id>/', views.DirectorDetailAPIView.as_view()),
    path('api/v1/movies/', views.MovieListAPIView.as_view()),
    path('api/v1/movies/<int:id>/', views.MovieDetailAPIView.as_view()),
    path('api/v1/reviews/', views.ReviewsListAPIView.as_view()),
    path('api/v1/reviews/<int:id>/', views.ReviewsDetailAPIView.as_view()),
    path('api/v1/users/', include('users.urls')),

]
