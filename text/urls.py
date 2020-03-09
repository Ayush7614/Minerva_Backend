from django.conf.urls import include
from django.urls import path

from rest_framework import routers

from text.views import TextView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'auth', TextView)

urlpatterns = [
	path('', include(router.urls))
]