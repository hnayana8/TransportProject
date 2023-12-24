from django.urls import path,include
from . import views 



urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('registration/', views.registration, name='registration'),
    path('about/',views.about,name='about'),
    path('pricing/',views.pricing,name='pricing'),
    path('user_home/',views.user_home,name='user_home'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('driver_login/', views.driver_login, name='driver_login'),
    path('driver_registration/', views.driver_registration, name='driver_registration'),
    path('driver_home/', views.driver_home, name='driver_home'),
    path('driver_logout/', views.driver_logout, name='driver_logout'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_registration/', views.admin_registration, name='admin_registration'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('admin_home/', views.admin_home, name='admin_home'),
    path('views_user/', views.views_user, name='views_user'),
    path('views_drivers/', views.views_drivers, name='views_drivers'),
    path('book_car/',views.book_car,name='book_car'),
    path('search/',views.search,name='search'),
    path('views_bookings/',views.views_bookings,name='views_bookings'),
    path('order/',views.order,name='order'),
    path('delete/<int:id>/', views.delete_data, name='deletdata'),
    path('cargo_details/', views.cargo_details, name='cargo_details'),
    path('load-courses/', views.load_courses, name='ajax_load_courses'),
    path('demo/', views.demo, name='demo'),

] 