# language: es
  Característica: Cancelar reserva de automovil
    Como cliente de la concesionaria Mercedez Benz
    Quiero cancelar el abono realizado para reservar un automovil
    Para no perder el dinero abonado


  Escenario: Cancelar abono de reserva de automovil sin penalizacion
    Dado que el cliente tiene el "vehiculo_2" en estado "abonando"
    Cuando el cliente cancele la reserva del "vehiculo_2"
    Entonces se le dara el "total_abonado" a la "cartera" del cliente
    Y el "vehiculo_2" tendra un estado de "disponible"

  Escenario: Calcelar abono de reserva de automovil con penalizacion
    Dado que el cliente tiene el "vehiculo_3" en estado "reservado"
    Cuando el cliente cancele la reserva del "vehiculo_3"
    Entonces se le dara el "total_abonado" menos el 15% del mismo a la "cartera" del cliente
    Y el "vehiculo_3" tendra un estado de "disponible" 