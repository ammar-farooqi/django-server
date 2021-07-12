from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('helloworld/', views.hmlyl, name='helloworld'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('memant/', views.Memant_list_rest),
    path('memant/<int:pk>/', views.getOneMemant_rest)
]
