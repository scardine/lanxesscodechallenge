import ast

from django.utils.datastructures import OrderedSet
from rest_framework import serializers

from .models import Actor, Slot


class SlotField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return OrderedSet(tuple(slot) for slot in data)


class ActorDetailSerializer(serializers.ModelSerializer):
    slots = SlotField()

    class Meta:
        model = Actor
        fields = '__all__'


class ActorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'
