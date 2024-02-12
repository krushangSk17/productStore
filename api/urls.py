from django.contrib import admin
from django.urls import path
from home.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('delete-product/', delete_product, name='delete_product'),
    path('change-password/', change_password, name='change_password'),
    path('register/', register_user, name='register_user'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('get-products/', get_products, name='get_products'),  # Assign a name here
    path('save-product/', save_product, name='save_product'),  # Assign a name here
    path('save-category/', save_category, name='save_category')  # And here
]