import operator
from functools import reduce

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Actor
from .serializers import ActorSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer


class AvalableSlotsViewSet(viewsets.ViewSet):
    """Pass a list of IDs in order to get available slots.

     Example: /api/availability/?id=1&id=2"""
    def list(self, request):
        data = request.GET.getlist('id')
        if not data:
            return Response([])
        actors = [get_object_or_404(Actor, pk=pk) for pk in data]
        return Response(reduce(operator.and_, [actor.slots for actor in actors]))

