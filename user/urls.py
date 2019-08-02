
from django.urls import path,include
from django.conf.urls import url,re_path

# from rest_framework.routers import DefaultRouter
from django.contrib.auth.views import PasswordResetDoneView,PasswordResetConfirmView,PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetView,PasswordResetCompleteView

from . import views


app_name = 'user'

urlpatterns = [
    # path('',include(router.urls)),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUserView.as_view(), name='me'),
    path('reset-password/', views.ChangePasswordView.as_view(), name='reset-password'),

     # path('change-password', .change_password, name='change-password'),
    # path('reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('reset-password/done', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset-password/confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset-password/complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]
