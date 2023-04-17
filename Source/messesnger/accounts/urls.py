from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.UserFormView.as_view(), name='accounts'),
    path('MyFriends/', views.MyFriend.as_view(), name='MyFriends'),
    path('home/', views.home, name='home'),
    path('show_user/', views.show_user, name='show_user'),
    path('my_posts/', views.PostView.as_view(), name='my_posts'),
    path('logout_user/', views.logout_user, name='logout_user'),
    path('change_password/', views.change_password, name='change_password'),
    path('connect/<slug:operation>/<int:pk>', views.change_friends, name='change_friends')
]