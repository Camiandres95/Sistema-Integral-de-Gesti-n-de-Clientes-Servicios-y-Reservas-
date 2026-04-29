from clases import *

Clientes = []
reservas = []

def registrar_error(error):
    with open("logs.txt", "a") as f:
        f.write(str(error) + "\n")



# --------------------------
# PRUEBAS (10 CASOS)
# --------------------------

print("\n--- INICIO DE PRUEBAS ---\n")


# 1 - Cliente válido
try:
    c1 = Cliente("Camilo", "camilo@mail.com")
    Clientes.append(c1)
    print("Cliente creado correctamente")
except Exception as e:
    registrar_error(e)


# 2 - Cliente inválido (nombre vacío)
try:
    c2 = Cliente("", "error@mail.com")
    Clientes.append(c2)
except Exception as e:
    print("Error cliente:", e)
    registrar_error(e)


# 3 - Cliente inválido (correo)
try:
    c3 = Cliente("Juan", "correo_invalido")
    Clientes.append(c3)
except Exception as e:
    print("Error cliente:", e)
    registrar_error(e)


# 4 - Servicio válido
try:
    s1 = ReservaSala(2)
except Exception as e:
    registrar_error(e)


# 5 - Servicio inválido
try:
    s2 = ReservaSala(-1)
except Exception as e:
    print("Error servicio:", e)
    registrar_error(e)


# 6 - Reserva correcta
try:
    r1 = Reserva(c1, s1)
    print(r1.confirmar())
    reservas.append(r1)
except Exception as e:
    registrar_error(e)


# 7 - Reserva con error
try:
    s_error = AlquilerEquipo(0)
    r2 = Reserva(c1, s_error)
    print(r2.confirmar())
except Exception as e:
    registrar_error(e)


# 8 - Otra reserva válida
try:
    s3 = Asesoria(3)
    r3 = Reserva(c1, s3)
    print(r3.confirmar())
    reservas.append(r3)
except Exception as e:
    registrar_error(e)


# 9 - Cancelación
try:
    print(r1.cancelar())
except Exception as e:
    registrar_error(e)


# 10 - Error manual
try:
    raise ErrorReserva("Error manual de prueba")
except Exception as e:
    print("Error detectado:", e)
    registrar_error(e)


print("\n--- FIN DE PRUEBAS ---\n")