

from locust import HttpUser, constant, task


class MyHttpUser(HttpUser):

    host = 'https://reqres.in/'
    wait_time = constant(1)

    @task
    def get_users(self):
        res = self.client.get('api/users?page=2')
        print(res.text)
        print(res.status_code)

    @task
    def create_user(self):
        payload = {
            "name": "morpheus",
            "job": "leader"
        }

        res = self.client.post('api/users', data=payload)
        print(res.text)
        print(res.status_code)