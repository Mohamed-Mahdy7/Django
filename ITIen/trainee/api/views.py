from .serializers import TraineeSerializer
from trainee.models import Trainee
from rest_framework import viewsets
from rest_framework.decorators import permission_classes
from rest_framework.response import Response
from rest_framework import status

class TraineeViewset(viewsets.ViewSet):
    def list(self, requset):
        queryset=Trainee.objects.all()
        serailzer=TraineeSerializer(queryset, many=True)
        return Response(serailzer.data, status=status.HTTP_200_OK)
