# Locust no ofrece en sí una forma de parametrízar por ende si queres parametrizar tenemos parametrizar distintas maneras, por ejemplo:
# - mediante código python
# - mediante archivos
# - mediante librerias
# Es importante tener en cuenta que Locust detecta si buscamos parametrizar una ejecución, por ejemplo, utilizando un csv.
# A continuación un ejemplo.
from locust import HttpUser, task, constant, SequentialTaskSet
from read_csv_data import CsvReader

class MyScript(SequentialTaskSet):
    
    # def __init__(self, parent):
    #     super().__init__(parent)
    #     self.test_data = CsvRead('DataParameterization\\customer-data.csv').read()

    @task
    def get_user_info(self):
        
        test_data = CsvReader('src/09_data_parameterization/user_list.csv').read()
        print('***************')
        print(test_data)
        print('***************')


        data = {
            'id': test_data['id'],
            'first_name': test_data['first_name']
        }

        test_case_name = 'Getting info from user {first_name}'.format(first_name= data['first_name'])
        path_url = '/api/users/{id}'.format(id= data['id'])

        with self.client.get(path_url, catch_response=True, name=test_case_name) as response:
            if response.status_code == 200 and test_data['first_name'] == response.json()['data']['first_name']:
                response.success()
            else:
                response.failure('TEST FAIL')


class MyLoadTest(HttpUser):
    host = 'https://reqres.in'
    wait_time = constant(1)
    tasks = [MyScript]
