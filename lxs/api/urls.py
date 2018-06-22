from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'actors', views.ActorViewSet)

urlpatterns = [
    url(r'^available_slots/', views.AvalableSlotsView.as_view()),
    url(r'^', include(router.urls))
]
