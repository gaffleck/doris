from services.models import Customer,Friend
from rest_framework import viewsets
from services.serializers import CustomerSerializer, FriendSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Customer
    serializer_class = CustomerSerializer


class FriendViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Friend
    serializer_class = FriendSerializer