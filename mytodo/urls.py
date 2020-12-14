from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:num>', views.index, name='index'),
    path('achieved/<int:num>', views.achieved, name='achieved'),
    path('did/', views.youdid, name='did'),
    path('did/<int:num>', views.youdid, name='did'),
    path('diddelete/<int:num>', views.diddelete, name='diddelete'),
]