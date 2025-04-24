from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from todoapi.views import TaskViewSet, home
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', home),
    path('admin/', admin.site.urls),
    path('api-token-auth/', obtain_auth_token),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls'))
]



