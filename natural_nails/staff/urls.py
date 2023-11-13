from django.urls import path
from . import views

urlpatterns = [
    path('', views.staff, name='staff'),
    path('add', views.staff_add, name='staff_add'),
    path('update/<id>', views.staff_update, name='staff_update'),

]