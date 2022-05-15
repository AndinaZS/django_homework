from django.db.models import Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer


class AdvertisementViewSet(ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_class = AdvertisementFilter

    def get_queryset(self):
        if not self.request.auth:
            queryset = Advertisement.objects.filter(~Q(status__exact='DRAFT'))
        else:
            queryset = Advertisement.objects.filter(Q(creator__exact=self.request.user)|
                                                    (~Q(status__exact='DRAFT')&~Q(creator__exact=self.request.user)))
        return queryset

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsOwner()]
        return []


