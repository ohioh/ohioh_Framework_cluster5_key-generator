from main import celery

@celery.task
def test_task():
    print('On call task')
