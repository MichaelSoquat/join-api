from unicodedata import category
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, TaskSerializer
from .models import Task, Test
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    print(queryset)


def testFunction(request):
    data = Test.objects.all()
    return render(request, 'test.html', {'users':data})

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    print (queryset)

    
    def update(self, request, *args, **kwargs):
        task_object = self.get_object()
        data = request.data
        task_object.category = data["category"]
        task_object.description = data["description"]
        task_object.dueDate = data["dueDate"]
        task_object.title = data["title"]
        task_object.urgency = data["urgency"]
        task_object.status = data["status"]
        task_object.save()
        serializer = TaskSerializer(task_object)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        task_object = self.get_object()
        task_object.delete()
        return Response('Object deleted')

        
