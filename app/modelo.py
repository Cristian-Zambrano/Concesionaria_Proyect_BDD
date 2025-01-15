class Cliente():
    def __init__(self, nombre):
        self.nombre = nombre
        self.vehiculo_seleccionado = None

    def seleccionar_vehiculo(self, vehiculo):
        self.vehiculo_seleccionado = vehiculo

    def abonar(self, monto):
        if monto > 0 and self.vehiculo_seleccionado.obtener_estado() != "reservado": #-1
            self.vehiculo_seleccionado.actualizar_abono_total(monto)
            return True
        return False

    def cancelar_reserva(self, vehiculo):
        self.vehiculo_seleccionado = None

    def pagar_restante(self, valor_restante):
        if self.vehiculo_seleccionado.obtener_estado() == "reservado" and self.vehiculo_seleccionado.valor_comercial - self.vehiculo_seleccionado.total_abonado == valor_restante:
            self.vehiculo_seleccionado.actualizar_abono_total(valor_restante)
            return True
        return False

class Vehiculo():
    def __init__(self, nombre, valor_comercial):
        self.nombre = nombre
        self.valor_comercial = valor_comercial
        self.estado = "disponible"
        self.total_abonado = 0

    def actualizar_abono_total(self, monto):
        self.total_abonado += monto
        print(monto)
        self.actualizar_estado(self.total_abonado)

    def obtener_total_abonado(self):
        return self.total_abonado

    def obtener_valor_comercial(self):
        return self.valor_comercial

    def obtener_estado(self):
        return self.estado

    def regresar_abono(self, cartera):
        if self.estado == "abonando":
            cartera.agregar_dinero(self.total_abonado)
            return 1
        if self.estado == "reservado":
            cartera.agregar_dinero(self.total_abonado * 0.85)
            return 2



    def actualizar_estado(self, total_abonado):
        if total_abonado >= self.valor_comercial * 0.3:
            self.estado = "reservado"
        if total_abonado == self.valor_comercial:
            self.estado = "vendido"
        if 0 < total_abonado < self.valor_comercial * 0.3:
            self.estado = "abonando"
        if total_abonado == 0:
            self.estado = "disponible"

    def liberar_reserva(self):
        self.total_abonado = 0
        self.actualizar_estado(self.total_abonado)

class Catalogo():
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self.vehiculos

    def esta_vehiculo_en_catalogo(self, vehiculo):
        if vehiculo in self.vehiculos:
            return True
        return False

class Cartera():
    def __init__(self):
        self.dinero = 0

    def obtener_dinero(self):
        return self.dinero

    def agregar_dinero(self, monto):
        self.dinero += monto

    def restar_dinero(self, monto):
        if monto <= self.dinero:
            self.dinero -= monto
            return True
        return False

    def obtener_dinero(self):
        return self.dinero
