# Locust permite validar tantos respuestas JSON como XML
# Para validar la respuesta es necesario especificar que queremos guardar la respuesta luego del request:
#
#   **************************
#   *   catch_response=True  *
#   **************************   
# 
# Luego se debe realizar las evaluaciones correspondientes y determinar si el test paso o fallo con
# success() o failure()   
from locust import HttpUser, task, constant, SequentialTaskSet


class MyTaskSet(SequentialTaskSet):

    @task
    def get_json(self):
        expected_status_code = 200
        expected_first_name = 'Janet'

        with self.client.get("/api/users/2", catch_response=True, name="JSON") as response:
            print(response.json())
            print(response.json()['data']['first_name'])
            if response.status_code == expected_status_code and response.json()['data']['first_name'] == expected_first_name:
                response.success() 
            else:
                response.failure('Test fail!!')    



class VerificationTest(HttpUser):
    host = 'https://reqres.in'
    wait_time = constant(1)
    tasks = [MyTaskSet]