#Locust no trae una herramienta particular de logs, por lo tanto debemos usar el logging por defecto de Python
#Sin embargo, Locust tiene comandos para configurar el nivel de los logs:
# 
# ***********************************************************************************
# *  --skip-loggin-setup                                                            *
# *  --logfile <file_path> (el archivo tiene q tener extensión .log)                *
# *  --loglevel <DEBUG/INFO/WARNING/ERROR/CRITICAL> (por defecto el nivel es INFO)  *
# ***********************************************************************************
#  

from locust import HttpUser, task, constant, tag, SequentialTaskSet
import logging


class MyTaskSet(SequentialTaskSet):

    @task
    @tag('janet','user_info')
    def get_janet_info(self):
        expected_status_code = 200
        expected_first_name = 'Janet'

        with self.client.get("/api/users/2", catch_response=True, name="JSON") as response:
            logging.info(response.json())
            logging.info(response.json()['data']['first_name'])
            if response.status_code == expected_status_code and response.json()['data']['first_name'] == expected_first_name:
                logging.info('PASSED')
                response.success() 
            else:
                logging.info('FAILED')
                response.failure('Test fail!!')    

    @task
    @tag('george')
    def get_george_info(self):
        expected_status_code = 200
        expected_first_name = 'Janet'

        with self.client.get("/api/users/2", catch_response=True, name="JSON") as response:
            logging.info(response.json())
            logging.info(response.json()['data']['first_name'])
            if response.status_code == expected_status_code and response.json()['data']['first_name'] == expected_first_name:
                logging.info('PASSED')
                response.success() 
            else:
                logging.info('FAILED')
                response.failure('Test fail!!')     

class VerificationTest(HttpUser):
    host = 'https://reqres.in'
    wait_time = constant(1)
    tasks = [MyTaskSet]