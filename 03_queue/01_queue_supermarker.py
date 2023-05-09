import random
import time

# Define los parámetros de la simulación para mayor facilidad

num_clientes = 3  # número de clientes a simular
intervalo_llegada = 2  # tiempo medio entre llegadas de clientes (segundos)
tiempo_compra = 5  # tiempo medio que tarda un cliente en hacer la compra (segundos)

# Define la cola de clientes
cola: list = []


# Define la función para agregar clientes a la cola
def agregar_cliente(cliente):
    cola.append(cliente)
    print(f"Client {cliente} was add to the queue")


# Define la función para atender a un cliente
def atender_cliente():
    if len(cola) == 0:
        print("there's clientes in the queue")
        return

    cliente: int = cola.pop(0)
    print(f"Client {cliente} is being attended ")

    tiempo: float = random.expovariate(1.0 / tiempo_compra)
    time.sleep(tiempo)
    print(f"Client {cliente} has completed its purchase in {tiempo:.2f} seconds")


# Simula la llegada de los clientes
for i in range(num_clientes):
    tiempo = random.expovariate(1.0 / intervalo_llegada)
    time.sleep(tiempo)

    cliente: int = i + 1
    agregar_cliente(cliente)

# Atiende a los clientes en orden de llegada
while len(cola) > 0:
    atender_cliente()

print("All customers have been served")
