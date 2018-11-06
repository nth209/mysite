from django.conf.urls import url

from django.contrib import admin
from link import views


app_name='link'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^link/index/', views.index, name="index")
]



