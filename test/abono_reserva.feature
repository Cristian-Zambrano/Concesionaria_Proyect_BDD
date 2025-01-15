# language: es
  Característica: Abono para reserva de automovil
    Como vendedor de Mercedez Benz
    Quiero que los clientes paguen un abono para reservar un automovil
    Para asegurar la venta del automovil

  Escenario: Abonar dinero para reservar automovil
    Dado que el cliente selecciono un vehiculo "vehiculo_1" con un precio de "100000" del catalogo de vehiculos
    Cuando el cliente abona "25000" para reservar el "vehiculo_1"
    Entonces el "vehiculo_1" tendra un estado de "abonando"
    Pero si el "total_abonado" es igual al 30% de "100000" que es el costo del vehiculo
    Y el "vehiculo_1" tendra un estado de "reservado"


  Escenario: Entrega del carro al cliente
    Dado que el cliente tiene el "vehiculo_1" en estado "reservado"
    Cuando el cliente abone los restantes "70000" del "vehiculo_1"
    Entonces el "vehiculo_1" tendra un estado de "vendido"