# Los métodos on_start() y on_stoṕ() son similares a los Set Up Thread Groups y Tear Down Thread Groups de JMeter
# Se ejecutan una sola vez y no llevan decorator
# En una clase User, on_start() se ejecuta que el usuario es iniciado y on_stop() cuando es finalizado
# En una clase TaskSet, on start() se ejecuta antes de que empiece la primera task y on_stop() cuando termina de ejecutar todas las task.
# A continuación un ejemplo con una clase HttpUser que usa SequentialTaskSet

from locust import HttpUser, task, constant, SequentialTaskSet


class MyTest(SequentialTaskSet):

    def on_start(self):
        print('Start')

    @task
    def cart_page(self):
        self.client.get('/', name=self.browse_product.__name__)
        print('Home Page')

    def on_stop(self):
        print('Stop')


class LoadTest(HttpUser):
    host = 'https://reqres.in'
    tasks = [MyTest]
    wait_time = constant(1)