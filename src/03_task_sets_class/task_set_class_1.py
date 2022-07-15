from locust import TaskSet, HttpUser, constant, task

class MyTaskSet(TaskSet):

    @task
    def get_info_of_user_2(self):
        self.client.get('api/users/2')
        print('Getting info of User 2')

    @task
    def get_info_of_user_3(self):
        self.client.get('api/users/3')
        print('Getting info of User 3')  

    @task
    def get_error(self):
        self.client.get('api//')
        print('Getting info of User 3')          

class MyHttpUser(HttpUser):
    host = 'https://reqres.in/'
    wait_time = constant(1)
    tasks = [MyTaskSet]        