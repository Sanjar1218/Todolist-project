from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as views_auth

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('datalist.urls'), name='main'),
    path('login/', views_auth.LoginView.as_view(template_name='pages/login.html'), name='loginname'),
    path('logout/', views_auth.LogoutView.as_view(template_name='pages/logget_out.html'), name='logoutname'),
]
