from http.client import ResponseNotReady

from .serializers import TraineeSerializer
from trainee.models import Trainee
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

class TraineeViewset(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    def list(self, requset):
        queryset=Trainee.objects.all()
        serailzer=TraineeSerializer(queryset, many=True)
        return Response(serailzer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = TraineeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response({
                "message": "User not found!"},
                status=status.HTTP_404_NOT_FOUND)

        serializer = TraineeSerializer(trainee)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def update(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(
                {"message": "User not found!"},
                status=status.HTTP_404_NOT_FOUND)
        
        serializer = TraineeSerializer(trainee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        try:
            trainee = Trainee.objects.get(pk=pk)
        except Trainee.DoesNotExist:
            return Response(
                {"message": "User not found!"},
                status=status.HTTP_404_NOT_FOUND)
        trainee.delete()
        return Response(
            {"message": "User Deleted Successfully!"},
            status=status.HTTP_200_OK
        )