from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, get_object_or_404
from rest_framework.response import Response
from .models import Sensor
from .serializers import SensorSerializer, SensorSpecificSerializer, MeasurementSpecificSerializer


class SensorDetailView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSpecificSerializer


class SensorView(APIView):
    def get(self, request, pk=None):
        if pk:
            sensor = get_object_or_404(Sensor.objects.all(), pk=pk)
            serializer = SensorSerializer(sensor)
            return Response({"sensor": serializer.data})
        sensors = Sensor.objects.all()
        serializer = SensorSerializer(sensors, many=True)
        return Response(serializer.data)

    # for add sensor
    def post(self, request):
        sensor = SensorSerializer(data=request.data)
        saved_data = None
        if sensor.is_valid(raise_exception=True):
            saved_data = sensor.save()
        return Response({"MESSAGE": f"Sensor {saved_data} created successfully"}, status=status.HTTP_201_CREATED)

    # for update sensor
    def put(self, request, pk):
        saved_sensor = get_object_or_404(Sensor.objects.all(), pk=pk)
        sensor = SensorSerializer(instance=saved_sensor, data=request.data, partial=True)
        saved_data = None
        if sensor.is_valid(raise_exception=True):
            saved_data = sensor.save()
        return Response({"MESSAGE": f"Sensor {saved_data} updated successfully"})

    # for delete
    def delete(self, request, pk):
        sensor = get_object_or_404(Sensor.objects.all(), pk=pk)
        sensor.delete()
        return Response({"MESSAGE": f"Article with id {pk} has been deleted."}, status=204)


class MeasureView(APIView):
    # for add measure
    def post(self, request):
        measure = MeasurementSpecificSerializer(data=request.data)
        saved_data = None
        if measure.is_valid(raise_exception=True):
            saved_data = measure.save()
        return Response({"MESSAGE": f"Measure {saved_data} created successfully"}, status=status.HTTP_201_CREATED)

    def get(self, request):
        return Response(status=status.HTTP_200_OK)