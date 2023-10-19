from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('edit/<int:employee_id>/', views.edit_employee, name='edit_employee'),

]
