from locust import TaskSet, HttpUser, constant, task

class MyTaskSet(TaskSet):

    @task
    def get_info_of_user_2(self):
        self.client.get('api/users/2')
        print('Getting info of User 2')
        self.interrupt()

class MyErrorTaskSet(TaskSet):
    @task
    def get_error_404(self):
        self.client.get('api///')
        print('Getting error 400')     
        self.interrupt()

class MyHttpUser(HttpUser):
    host = 'https://reqres.in/'
    wait_time = constant(1)
    tasks = [MyTaskSet,MyErrorTaskSet]        