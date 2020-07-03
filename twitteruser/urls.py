from django.urls import path
from django.conf import settings
from twitteruser import views

user_url_patterns = [
    path('', views.index, name='home'),
    path('profile/<int:id>', views.UserPage),
    path('log_in/', views.UserLogin, name='log_in'),
    path('new_user/', views.create_user_view),
    path('logout/', views.logoutView)
]
