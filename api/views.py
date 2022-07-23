from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, TaskSerializer
from .models import Task, Test

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    print(queryset)

    def put(request, pk):
        pass

def testFunction(request):
    data = Test.objects.all()
    return render(request, 'test.html', {'users':data})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print (queryset)
