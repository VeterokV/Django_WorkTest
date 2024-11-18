from django.urls import path
from .views import CarsListCreateAPIView, CarsDetailAPIView, CommentListCreateAPIView
from .views import index, car_list, car_detail, car_create, car_edit, car_delete, signup, logout_view, add_comment
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('cars/', CarsListCreateAPIView.as_view(), name='CarList'),
    path('cars/<int:pk>/', CarsDetailAPIView.as_view(), name='CarDetail'),
    path('cars/<int:car_pk>/comments', CommentListCreateAPIView.as_view(), name='CommentList'),
    path('', index),
    path('main/', car_list, name='car-list'),
    path('main/cars/<int:pk>/', car_detail, name='car-detail'),
    path('main/cars/create/', car_create, name='car-create'),
    path('main/cars/<int:pk>/edit/', car_edit, name='car-edit'),
    path('main/cars/<int:pk>/delete/', car_delete, name='car-delete'),
    path('main/cars/<int:pk>/add-comment/', add_comment, name='add-comment'),
    path('main/accounts/login/', LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('main/accounts/logout/', logout_view, name='logout'),
    path('main/accounts/signup/', signup, name='signup'),
]

