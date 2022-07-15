# Locust permite utilizar un archivo de configuración para los valores de las distintas de la ejecución 
# Se puede usar tanto archivos .config o .yml
# Tambien permite, en vez de usar archivos de configuración se puede usar variables de entornos
#     https://docs.locust.io/en/stable/configuration.html?#environment-variables
#
# Para elegir el archivo de configuración a utilizar usamos el siguiente comando:
# 
#  **************************
#  * --config <file_path>   *
#  **************************

from locust import HttpUser, task, constant


class ConfigTest(HttpUser):
    wait_time = constant(1)

    def __init__(self, parent):
        super().__init__(parent)
        self.hostname = self.host

    @task
    def home_page(self):
        res = self.client.get("/", name=self.hostname)
        print(res.text)