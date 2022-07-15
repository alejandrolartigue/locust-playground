from locust import HttpUser, constant, task, between, constant_pacing

class MyHttpUser(HttpUser):
    host = 'https://reqres.in/'
    wait_time = between(1,5)

    @task
    def print_message(self):
        print('this messsage will be displayed between 1 -5 seconds')


 