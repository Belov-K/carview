from django.urls import path

from . import views

app_name='cars'
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:car_id>/', views.detail, name='detail'),
]