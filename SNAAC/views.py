from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_celery_beat.models import PeriodicTask
from .serializers import TaskSerializer, IntervalScheduleSerializer

@api_view(['GET', 'POST'])
def scheduled_tasks(request):
    if request.method == 'GET':
        tasks = PeriodicTask.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        interval_data = request.data.pop('interval', None)
        if interval_data:
            interval_serializer = IntervalScheduleSerializer(data=interval_data)
            if interval_serializer.is_valid():
                interval = interval_serializer.save()
                request.data['interval'] = interval.id
            else:
                return Response(interval_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        task_serializer = TaskSerializer(data=request.data)
        if task_serializer.is_valid():
            task_serializer.save()
            return Response(task_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_scheduled_task(request, pk):
    try:
        task = PeriodicTask.objects.get(id=pk)
    except PeriodicTask.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    task.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
