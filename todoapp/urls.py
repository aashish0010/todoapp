from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('add',views.add,name='add'),
    path('delete/<int:todo_id>/',views.delete, name='delete'),
]
