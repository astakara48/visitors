from django.urls import path
from. import views

app_name = 'visitors_data'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('new/', views.new, name='new'),
    path('new_en/', views.new_en, name='new_en'),
    path('confirm/<int:pk>/', views.confirm, name='confirm'),
    # path('confirm_en/<int:pk>/', views.confirm_en, name='confirm_en'),
    path('qr/<int:pk>/', views.qr, name='qr'),
    # path('qr_en/<int:pk>/', views.qr_en, name='qr_en'),
    path('read_qr/', views.read_qr, name='read_qr'),
    path('create_qr/', views.create_qr, name='create_qr'),
    path('result/<int:visitor_pk>/', views.result, name='result'),
    # path('make_crop_image/', views.make_crop_image, name='make_crop_image'),
    path('get_crop_image/<int:pk>/', views.get_crop_image_2, name='get_crop_image'),


]