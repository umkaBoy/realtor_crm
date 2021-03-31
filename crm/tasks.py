from project.celery import app



@app.task
def whitelist_parsing():
    print(23456789)
