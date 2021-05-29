from django.urls import path
from . import views

app_name="accounts"
urlpatterns = [
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.user_registration, name="register"),
    path('token/' , views.token_send , name="token_send"),
    path('success/' , views.success , name='success'),
    path('verify/<auth_token>' , views.verify , name="verify"),
    path('error' , views.error_page , name="error"),
    path('profile/',views.profile,name="profile"),
]
