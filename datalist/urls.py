from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('create', views.create, name='create'),
    # path('register/', register, name='register'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('done/<int:id>', views.done, name='done'),
]
