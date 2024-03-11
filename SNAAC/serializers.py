from rest_framework import serializers
from django_celery_beat.models import PeriodicTask, IntervalSchedule

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = PeriodicTask
        fields = ['id', 'name', 'task', 'args', 'kwargs', 'interval', 'start_time', 'last_run_at', 'total_run_count', 'date_changed', 'description']

class IntervalScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = IntervalSchedule
        fields = ['every', 'period']
