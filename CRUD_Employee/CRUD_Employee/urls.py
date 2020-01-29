
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('config.urls')),
    path('admin/', admin.site.urls),
    path('crud/', include('crud.urls'))
    #agregamos las vistas de crud app
]
