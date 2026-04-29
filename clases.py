from abc import ABC, abstractmethod

#-----------------------
# EXCEPCIONES PERSONALIZADAS
#-----------------------    
class ErrorReserva(Exception):
    pass


#-----------------------
# CLASES CLIENTES
#-----------------------
class Cliente:
    def __init__(self, nombre, correo):
        if not nombre:
            raise ValueError("El nombre del cliente no puede estar vacío.")
        if "@" not in correo:
            raise ValueError("El correo electrónico no es válido.")
        self.nombre = nombre
        self.correo = correo
    
    def mostrar_info(self):
        return f"¨{self.nombre} - {self.correo}"
    

#-----------------------
# CLASE ABSTRACTA SERVICIO
class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass



#-----------------------
# SERVICIOS (HERENCIA)
#-----------------------
class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        self.horas = horas

    def calcular_costo(self):
        if self.horas <= 0:
            raise ValueError("La cantidad de horas debe Validas.")
        return self.horas * 50000  # Costo por hora
    

class AlquilerEquipo(Servicio):
    def __init__(self, dias):
            super().__init__("Alquiler de Equipo")
            self.dias = dias

    def calcular_costo(self):
        if self.dias <= 0:
            raise ValueError("Días Invalidos.")
        return self.dias * 20000  # Costo por día


class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoría")
        self.horas = horas

    def calcular_costo(self):
        if self.horas <= 0:
            raise ValueError("Sesiones Invalidas.")
        return self.horas * 80000  # Costo por hora
    


#-----------------------
# CLASE RESERVA
#-----------------------
class Reserva:
    def __init__(self, cliente, servicio):
        self.cliente = cliente
        self.servicio = servicio
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            costo = self.servicio.calcular_costo()
        except ValueError as e:
            self.registrar_error(e)
            return "❌ Error al calcular costo"
        
        else:
            self.estado = "Confirmada"
            return f"✅ Reserva confirmada. Costo total: {costo}"
        
        finally:
            print("Proceso de confirmación finalizado.")

    def cancelar(self):
        if self.estado == "Confirmada":
            self.estado = "Cancelada"
            return "✅ Reserva cancelada."
        
    def registrar_error(self, error):
        with open("logs.txt", "a") as f:
            f.write(str(error) + "\n")



        
    
    
    

