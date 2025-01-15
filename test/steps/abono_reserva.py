from app.modelo import *
from behave import *


@step('que el cliente selecciono un vehiculo "vehiculo_1" con un precio de "100000" del catalogo de vehiculos')
def step_impl(context):
    context.cliente = Cliente("Juan Pablo")
    context.vehiculo = Vehiculo("vehiculo_1", 100000)
    context.catalogo = Catalogo()
    context.catalogo.agregar_vehiculo(context.vehiculo)
    context.cliente.seleccionar_vehiculo(context.vehiculo)
    assert context.catalogo.esta_vehiculo_en_catalogo(context.cliente.vehiculo_seleccionado)

@step('el cliente abona "25000" para reservar el "vehiculo_1"')
def step_impl(context):
    assert context.cliente.abonar(context.vehiculo, 25000)

@step('el "vehiculo_1" tendra un estado de "abonando"')
def step_impl(context):
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "abonando"

@step('si el "total_abonado" es igual al 30% de "100000" que es el costo del vehiculo')
def step_impl(context):
    assert context.cliente.abonar(context.vehiculo, 5000)

@step('el "vehiculo_1" tendra un estado de "reservado"')
def step_impl(context):
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "reservado"


@step('que el cliente tiene el "vehiculo_1" en estado "reservado"')
def step_impl(context):
    context.cliente = Cliente("Juan Pablo")
    context.vehiculo = Vehiculo("vehiculo_1", 100000)
    context.catalogo = Catalogo()
    context.catalogo.agregar_vehiculo(context.vehiculo)
    context.cliente.seleccionar_vehiculo(context.vehiculo)
    context.cliente.abonar(context.vehiculo, 30000)
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "reservado"

@step('el cliente abone los restantes "70000" del "vehiculo_1"')
def step_impl(context):
    context.cliente.abonar(context.vehiculo, 70000)

@step('el "vehiculo_1" tendra un estado de "vendido"')
def step_impl(context):
    assert context.cliente.vehiculo_seleccionado.obtener_estado() == "vendido"

