# Los métodos on_start() y on_stoṕ() son similares a los Set Up Thread Groups y Tear Down Thread Groups de JMeter
# Se ejecutan una sola vez y no llevan decorator
# En una clase User, on_start() se ejecuta que el usuario es iniciado y on_stop() cuando es finalizado
# En una clase TaskSet, on start() se ejecuta antes de que empiece la primera task y on_stop() cuando termina de ejecutar todas las task.
# A continuación un ejemplo con una clase User

from locust import User, task, constant

class MyUserTest(User):
    wait_time = constant(1)

    def on_start(self):
        print('Starting')

    @task
    def task_1(self):
        print('Working')

    def on_stop(self):
        print('Stopping') 