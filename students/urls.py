from django.conf.urls import include
from django.urls import path

from rest_framework import routers


from students.views import RegiserViewSet
router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', RegiserViewSet)

urlpatterns = [
	path('', include(router.urls))
]