import operator
from functools import reduce

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Actor
from .serializers import ActorDetailSerializer, ActorListSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return ActorListSerializer
        return ActorDetailSerializer


class AvalableSlotsViewSet(viewsets.ViewSet):
    """Receives a list of desired attendees (IDs) and returns slots
    suitable for a meeting.

     Example: /api/availability/?id=1&id=2"""
    def list(self, request):
        data = request.GET.getlist('id')
        if not data:
            return Response([])
        actors = [get_object_or_404(Actor, pk=pk) for pk in data]
        return Response(sorted(reduce(operator.and_, [set(actor.slots) for actor in actors])))
