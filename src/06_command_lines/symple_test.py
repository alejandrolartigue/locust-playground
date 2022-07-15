# Para ejecutar las pruebas por comandos de consola (sin utilizar el UI) podemos usar el siguiente comando
# *********************************************************************************************************** 
# *     locust -f <file_path> -f -u <number_of_users> -r <respawn_time> -t <duration_of_test>  --headless    *
# ***********************************************************************************************************
# 
# Otros comandos últiles que se pueden agregar a la ejecución son:
# ***************************************************************************************************************************
# * --print-stats           : imprimpre los stats por la consola                                                            *
# * --csv <file_path>       : guarda los resultados en un archivo csv. (el archivo tiene que tener la extensión csv)        *
# * --csv-full-history      : para tener un informe completo. por default solo se muestra una fila con las estadísticas,    * 
# *                           con esta opción cada dos segundos te va mostrando las estadísticas                            *   
# *                           y no se piede el historial de las mismas                                                      *
# * --host <host_url>       : si se quiere enviar la url del host por variable de entorno                                   *
# * -L <log_level>          : para elegir el nivel de los logs. Por defecto, es INFO                                        *
# * --logsfile <file_path>  : guarda los logs en un archivo log. (el archivo debe tener extensión log)                      *
# * -l                      : list all User class names                                                                     *
# * --show-task-ratio       : muesta la relación entre clases y tareas en tabla por consola                                 *
# * --show-task-ratio-json  : guarda la reslación entre clases y tareas en un archivo json                                  *
# * --html <file_path>      : guarda los resultados en un archivo html (no es necesario escribir la extensión del archivo)  *
# * --only-summary          : muestra resument de los resultados de la ejecución por consola                                *   
# ***************************************************************************************************************************
from locust import HttpUser, task, constant

class SimpleTest(HttpUser):
    
    wait_time = constant(1)


    @task
    def launch_page(self):
        self.client.get('/')

