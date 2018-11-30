from django.contrib.auth.models import User, Group
from rest_framework import serializers
from services.models import Customer,Friend


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'email', )


class FriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Friend
        fields = ('first_name', 'birthday')