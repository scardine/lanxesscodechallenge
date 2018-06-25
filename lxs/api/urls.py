from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'actors', views.ActorViewSet)
router.register(r'availability', views.AvalableSlotsViewSet, base_name='availability')

urlpatterns = [
    #url(r'^/', views.AvalableSlotsView.as_view()),
    url(r'^', include(router.urls))
]
