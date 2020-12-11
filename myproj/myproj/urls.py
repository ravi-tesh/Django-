from django.contrib import admin
from django.urls import path,include

admin.site.site_header = "UMSRA Kella"
admin.site.site_title = "UMSRA Kella"
admin.site.index_title = "Welcome to Kella Kaho World"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]