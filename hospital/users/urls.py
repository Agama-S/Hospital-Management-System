from django.urls import path
from .import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('wait_for_approval/', views.user_wait_approval, name='user_wait_approval'),

    path('signout/', views.signout, name='signout')

]
