from datetime import date, datetime

def execution_time(func):
     def wraper(*args, **kwargs):
          initial_time = datetime.now()
          func(*args, **kwargs)
          final_time = datetime.now()
          time_elapsed = final_time - initial_time
          print("Pasaron " + str(time_elapsed.total_seconds()) + " segundos")
     return wraper

@execution_time
def random_func():
     for _ in range(1,10000000):
          pass 

@execution_time
def suma(a: int, b: int) -> int:
     return a + b 

@execution_time
def saludo(nombre="David"):
     print("Hola " + nombre)

random_func()
suma(5, 5)
saludo("Damaris")
