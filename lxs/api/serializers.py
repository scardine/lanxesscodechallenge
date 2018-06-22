import ast

from rest_framework import serializers

from .models import Actor, Slot


class SlotField(serializers.Field):
    def to_representation(self, value):
        return value

    def to_internal_value(self, data):
        return set(tuple(slot) for slot in data)


class ActorSerializer(serializers.ModelSerializer):
    slots = SlotField()

    class Meta:
        model = Actor
        fields = '__all__'