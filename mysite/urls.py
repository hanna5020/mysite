"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import include, path
# from .views import get_users, get_user, create_user, update_user, delete_user
from django.contrib import admin
from django.urls import include, path
from users import views
from users.views import get_users, get_user, create_user, update_user, delete_user, gmail_users_api, update_user_kafka

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),




    path('users/', get_users, name='get_users'),  # 获取所有用户
    path('users/<int:id>/', get_user, name='get_user'),  # 获取单个用户
    path('users/create/', create_user, name='create_user'),  # 创建用户
    path('users/update/<int:id>/', update_user, name='update_user'),  # 更新用户
    path('users/delete/<int:id>/', delete_user, name='delete_user'),  # 删除用户
    path('users/gmail-users/', gmail_users_api, name='gmail_users_api'),

    path('users/update_user_kafka/<int:id>/', update_user_kafka, name='update_user_kafka'),
]



