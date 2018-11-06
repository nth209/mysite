from django.conf.urls import url

from django.contrib import admin
from home import views


app_name='home'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/index/', views.index, name="index")
]



