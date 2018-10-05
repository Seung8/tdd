from django.contrib import admin
from django.urls import path

from lists.views import *

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', home_page, name='home_page'),
)
