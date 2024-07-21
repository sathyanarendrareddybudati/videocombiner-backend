from celery import Celery

app = Celery('myapp', broker='redis://redis:6379/0', backend='redis://redis:6379/0')

from routes.tasks import combine_videos

app.conf.update(
    task_routes={
        'tasks.combine_videos': {'queue': 'default'},
    }
)

if __name__ == '__main__':
    app.start()
