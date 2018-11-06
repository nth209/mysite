from django.conf.urls import url

from django.contrib import admin
from accounts import views


app_name='accounts'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/', views.login, name="login"),
    url(r'^accounts/loginHome/', views.login, name="login"),
    url(r'^accounts/logout/', views.logout, name="logout")
]