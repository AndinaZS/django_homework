from django_filters import rest_framework as filters, DateFromToRangeFilter, AllValuesFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    created_at = DateFromToRangeFilter()
    status = AllValuesFilter(field_name='status')

    class Meta:
        model = Advertisement
        fields = ['created_at', 'status']

