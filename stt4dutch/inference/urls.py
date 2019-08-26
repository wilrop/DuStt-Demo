from django.urls import path

from . import views

app_name = 'inference'
urlpatterns = [
    path('', views.index, name='index'),
    path('run_inference/', views.run_inference, name='run_inference'),
    path('upload/', views.upload, name='upload'),
    path('play_audio/', views.play_audio, name='play_audio'),
]