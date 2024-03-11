The following is a sample JSON input for the POST endpoint to create a Celery task.

{
    "name": "My Scheduled Task",
    "task": "your_app.tasks.your_task",
    "interval": {
        "every": 10,
        "period": "seconds"
    },
    "args": "[]",
    "kwargs": "{}",
    "start_time": "2024-03-07T12:00:00"
}
