from django.shortcuts import render, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import CarsSerializer, CommentSerializer
from .models import Car, Comment
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import redirect


def index(request):
    return redirect('car-list')


class CarsListCreateAPIView(generics.ListCreateAPIView):  #API списка записей
    queryset = Car.objects.all()
    serializer_class = CarsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CarsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):  #API Детальной информации записи
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(id_owner=self.request.user)


class CommentListCreateAPIView(generics.ListCreateAPIView):  #API Комментариев
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(id_car=self.kwargs['car_id'])

    def perform_create(self, serializer):
        cars = Car.objects.get(id_car=self.kwargs['car_id'])
        serializer.save(id_auth=self.request.user, id_car=cars)


def car_list(request):  #Список записей
    cars = Car.objects.all()
    users = User.objects.all()
    return render(request, 'cars_list.html', {'cars': cars, 'users': users})


def car_detail(request, pk):  #Детальная информация записи
    car = get_object_or_404(Car, pk=pk)
    comments = Comment.objects.filter(id_car_id=car)
    return render(request, 'cars_detail.html', {'car': car, 'comments': comments})


@login_required
def car_create(request):  #Создание записи
    if request.method == "POST":
        make = request.POST.get('make')
        carmodel = request.POST.get('carmodel')
        year = request.POST.get('year')
        desc = request.POST.get('desc')
        Car.objects.create(make=make, carmodel=carmodel, year=year, desc=desc, id_owner=request.user)
        return redirect('car-list')
    return render(request, 'cars_form.html')


@login_required
def car_edit(request, pk):  #Редактирование записи
    car = get_object_or_404(Car, pk=pk, id_owner=request.user)

    # Редирект в случае попытки доступа к чужим записям
    if car.id_owner != request.user:
        return redirect('car_list')

    #Модель POST запроса для формы редактирования записи
    if request.method == "POST":
        car.make = request.POST.get('make')
        car.carmodel = request.POST.get('carmodel')
        car.year = request.POST.get('year')
        car.desc = request.POST.get('desc')
        car.save()
        return redirect('car-detail', pk=car.pk)
    return render(request, 'cars_form.html', {'car': car})


@login_required
def car_delete(request, pk):  #Удаление записи
    car = get_object_or_404(Car, pk=pk, id_owner=request.user)

    # Редирект в случае попытки доступа к чужим записям
    if car.id_owner != request.user:
        return redirect('car-list')

    car.delete()
    return redirect('car-list')


@login_required
def add_comment(request, pk):  #Добавление комментария
    car = Car.objects.get(pk=pk)

    # Модель POST запроса для формы создания комментария
    if request.method == 'POST':
        content = request.POST.get('content')
        Comment.objects.create(content=content, id_car=car, id_auth=request.user)
        return redirect('car-detail', pk=pk)

    return redirect('car-detail', pk=pk)


def signup(request):  #Авторизация
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def logout_view(request):  #Выход из аккаунта пользователя
    logout(request)
    return redirect('car-list')
