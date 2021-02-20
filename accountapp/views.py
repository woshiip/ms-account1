# Create your views here.

from rest_framework import permissions
from rest_framework.viewsets import GenericViewSet, mixins

from account.models import Account
from account.serializers import *


class AccountViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.RetrieveModelMixin,
                     GenericViewSet):
    lookup_field = "id"
    permission_classes = [permissions.AllowAny, ]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

