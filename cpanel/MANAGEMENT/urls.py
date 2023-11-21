"""
URL configuration for cpanel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from log import views as logview
from members import views   as membersview
from money import views as moneyview
from schedule import views as scheduleview


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('signIn/', logview.signIn, name ='login'),
    path('index/', views.index, name ="index"),
    path('postsign/', logview.postsign, name ='postsign'),
    path('create/', views.create, name="create"),
    path('post_create/', views.post_create, name="post_create"),
    path('members/', membersview.members, name="members"),
    path('money/', moneyview.money, name="money"),
    path('calendar/', scheduleview.calendar, name="calendar"),
    path('logout/', logview.logout_view, name='logout')

]