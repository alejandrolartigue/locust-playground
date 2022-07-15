# Para definir un tag se debe agregar el decorador @tag a la task correspondiente.
# Un task puede tener varios tags
# Luego, al momento de ejecutar los test podemos agregar los siguientes comandos:
#   ***********************************************************
#   * --tags : para incluir los tags en la ejecución          *
#   * --exclude-tags : para excluir los tags en la ejecución  *
#   ***********************************************************

from locust import HttpUser, task, constant, tag, SequentialTaskSet


class MyTaskSet(SequentialTaskSet):

    @task
    @tag('janet','user_info')
    def get_janet_info(self):
        expected_status_code = 200
        expected_first_name = 'Janet'

        with self.client.get("/api/users/2", catch_response=True, name="JSON") as response:
            print(response.json())
            print(response.json()['data']['first_name'])
            if response.status_code == expected_status_code and response.json()['data']['first_name'] == expected_first_name:
                response.success() 
            else:
                response.failure('Test fail!!')    

    @task
    @tag('george')
    def get_george_info(self):
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