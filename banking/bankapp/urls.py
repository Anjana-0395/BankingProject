from . import views
from django.urls import path

app_name='bankapp'
urlpatterns= [
    path('',views.home,name='demo'),
    path('register/',views.registration,name='register'),
    path('login/',views.login,name='login'),
]