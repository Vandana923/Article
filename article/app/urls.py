from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('one/<int:pk>',views.display,name='details'),
    path('about',views.about,name='about')
]
