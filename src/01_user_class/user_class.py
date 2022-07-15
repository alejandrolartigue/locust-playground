from cgi import print_arguments
from multiprocessing.connection import wait
from locust import User, task, constant


class MyFirstUser(User):
    wait = constant(1)

    @task
    def first_task(self):
        print('Executing first task......')

    @task
    def śecond_task(self):
        print('Executing second task.....')