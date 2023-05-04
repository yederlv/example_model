#!/bin/bash

# Función para mostrar carga
function loading_animation {
  # Caracteres de la animación
  spinner="/|\-"

  # Ejecutar animación mientras espera a que el script termine
  while :
  do
    for i in `seq 0 3`
    do
      echo -ne "\r[${spinner:$i:1}] Cargando resultados del modelo... "
      sleep 0.2
    done
  done
}

# Iniciar la animación de carga en segundo plano
loading_animation &

# Obtener el ID del proceso de la animación de carga
spinner_pid=$!

# Ejecutar el script de Python
python3 modeloXGBoot.py

# Detener la animación de carga
kill $spinner_pid > /dev/null 2>&1
