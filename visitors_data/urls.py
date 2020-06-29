from django.urls import path
from. import views

app_name = 'visitors_data'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('citizen/', views.citizen, name='citizen'),
    path('foreigner/', views.foreigner, name='foreigner'),
    # path('new/', views.new, name='new'),
    path('confirm/<int:pk>/', views.confirm, name='confirm'),
    path('qr/<int:pk>/', views.qr, name='qr'),
    path('read_qr/', views.read_qr, name='read_qr'),
    path('create_qr/', views.create_qr, name='create_qr'),
]