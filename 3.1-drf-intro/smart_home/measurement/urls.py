from django.urls import path

from measurement.views import SensorListCreateView, MeasurementCreateView, SensorUpdateDetailView

urlpatterns = [
    path('sensor/', SensorListCreateView.as_view()),
    path('sensor/<int:pk>/', SensorUpdateDetailView.as_view()),
    path('measurements/', MeasurementCreateView.as_view()),
]
