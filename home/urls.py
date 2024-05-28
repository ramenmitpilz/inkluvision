from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('process/', views.process, name='process'),
    path('blog/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
]
