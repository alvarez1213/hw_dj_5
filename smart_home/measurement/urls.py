from django.urls import path

from .views import SensorDetailView, SensorView, MeasureView

urlpatterns = [
    path('sensors/', SensorView.as_view()),
    path('sensors/<int:pk>/', SensorView.as_view()),
    path('sensor-details/<int:pk>/', SensorDetailView.as_view(), name='sensor_detail'),
    path('measures/', MeasureView.as_view()),

]
