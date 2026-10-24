#!/bin/bash
# 01-curl-get.sh
# Ejercicio: GET simple

echo "=== GET simple ==="
curl https://httpbin.org/get
echo -e "\n\n=== GET con parámetros ==="
curl "https://httpbin.org/get?curso=preparacion-ia&modulo=api"
echo -e "\n\n"
