from django.conf.urls import url
from django.conf.urls import url

from rest_framework import routers
from demo import views

router = routers.SimpleRouter()
router.register(r'notes', views.NotesViewSet)
urlpatterns = router.urls
