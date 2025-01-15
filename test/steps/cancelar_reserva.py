from behave import *
from app.modelo import *

@step('que el cliente tiene el "vehiculo_2" en estado "abonando"')
def step_impl(context):
    context.cliente = Cliente("Cristian Zambrano")
    context.cartera = Cartera()
    context.cliente.cartera = context.cartera
    context.vehiculo = Vehiculo("vehiculo_2", 200000)
    context.catalogo = Catalogo()
    context.catalogo.agregar_vehiculo(context.vehiculo)
    context.cliente.seleccionar_vehiculo(context.vehiculo)
    context.cliente.abonar(context.vehiculo, 50000)
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "abonando"

@step('el cliente cancele la reserva del "vehiculo_2"')
def step_impl(context):
    context.cliente.cancelar_reserva(context.vehiculo)
    assert context.cliente.vehiculo_seleccionado is None

@step('se le dara el "total_abonado" a la "cartera" del cliente')
def step_impl(context):
    assert context.vehiculo.regresar_abono(context.cliente.cartera) == 1

@step('el "vehiculo_2" tendra un estado de "disponible"')
def step_impl(context):
    context.vehiculo.liberar_reserva()
    assert context.vehiculo.obtener_estado() == "disponible"

###################################
@step('que el cliente tiene el "vehiculo_3" en estado "reservado"')
def step_impl(context):
    context.cliente = Cliente("Cristina Castillo")
    context.cartera = Cartera()
    context.cliente.cartera = context.cartera
    context.vehiculo = Vehiculo("vehiculo_3", 200000)
    context.catalogo = Catalogo()
    context.catalogo.agregar_vehiculo(context.vehiculo)
    context.cliente.seleccionar_vehiculo(context.vehiculo)
    context.cliente.abonar(context.vehiculo, 150000)
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "reservado"


@step('el cliente cancele la reserva del "vehiculo_3"')
def step_impl(context):
    context.cliente.cancelar_reserva(context.vehiculo)
    assert context.cliente.vehiculo_seleccionado is None

@step('se le dara el "total_abonado" menos el 15% del mismo a la "cartera" del cliente')
def step_impl(context):
    context.vehiculo.regresar_abono(context.cliente.cartera)
    assert context.vehiculo.regresar_abono(context.cliente.cartera) == 2


@step('el "vehiculo_3" tendra un estado de "disponible"')
def step_impl(context):
    context.vehiculo.liberar_reserva()
    assert context.vehiculo.obtener_estado() == "disponible"