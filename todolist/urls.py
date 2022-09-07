from django.contrib import admin
from django.urls import path
from datalist.views import main, create, edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main, name='main'),
    path('create', create, name='create'),
    path('edit/<int:id>', edit, name='edit')
]
