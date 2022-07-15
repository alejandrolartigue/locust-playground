# Locus trae incorporados eventos los cuales pueden ser utilizados para realizar distintas acciones
# Por ejemplo, enviar notificaciones cuando un test falla o es exitoso
# Para usar los eventos tenemos que  usar distintos decoradores
# Más información sobre eventos puede encontrarse en:
# https://docs.locust.io/en/stable/extending-locust.html
from locust import HttpUser, task, constant, SequentialTaskSet
from locust import events


@events.spawning_complete.add_listener
def spawn_users(user_count, **kwargs):
    print('Se terminaron de ejecutar {user_number} usuarios'.format(user_number= user_count))


@events.request_success.add_listener
def send_notification(**kwargs):
    print('Enviando notificación por email cuando un request se realiza correctamente')


@events.request_failure.add_listener
def send_notification(**kwargs):
    print('Enviando un notificación por slack cuando un request falla')


@events.quitting.add_listener
def sla(environment, **kwargs):
    if environment.stats.total.fail_ratio > 0.01:
        print('Si el total de fallos es supera 0.01% entonces hacemos algo') 
        environment.process_exit_code = 1
        print(environment.process_exit_code)

    else:
        environment.process_exit_code = 0
        print(environment.process_exit_code)


class EventTest(SequentialTaskSet):

    @task
    def home_page(self):
        self.client.get("/")