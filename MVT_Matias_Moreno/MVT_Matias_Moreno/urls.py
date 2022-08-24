from django.contrib import admin
from django.urls import path
from Familiar.views import ver_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('familiar/', ver_familiar)
]
