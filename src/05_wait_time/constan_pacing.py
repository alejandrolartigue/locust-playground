from locust import HttpUser, constant, task, between, constant_pacing

class MyHttpUser(HttpUser):
    host = 'https://reqres.in/'
    wait_time = constant_pacing(5)

    @task
    def print_message(self):
        print('this messsage will be displayed every 5 second')