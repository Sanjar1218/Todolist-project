from django.contrib import admin
from django.urls import path
from datalist.views import main, create, delete, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('create', create, name='create'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit, name='edit'),
]
