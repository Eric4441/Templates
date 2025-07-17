from django.contrib import admin
from django.urls import path,include
from .views import all_data_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', all_data_view),
]