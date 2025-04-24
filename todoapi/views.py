from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from django.http import JsonResponse, HttpResponse
from rest_framework.authentication import TokenAuthentication, SessionAuthentication

class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer


def login(request):
    return HttpResponse({
        "message": "🎉 Welcome to the Todo API!",
        "routes": {
            "Tasks endpoint": "/api/tasks/",
            "Token auth": "/api-token-auth/"
        }
    })

def home(request):
    return JsonResponse({
        "message": "🎉 Welcome to the Todo API!",
        "routes": {
            "Tasks endpoint": "/api/tasks/",
            "Token auth": "/api-token-auth/"
        }
    })
