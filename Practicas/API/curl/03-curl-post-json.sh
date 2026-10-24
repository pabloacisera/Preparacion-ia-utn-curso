#!/bin/bash
# Ejercicio 3: POST con datos JSON
# Enviamos información al servidor

curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"nombre": "estudiante", "tema": "apis", "pregunta": "como funciona?"}'
echo -e "\n"
