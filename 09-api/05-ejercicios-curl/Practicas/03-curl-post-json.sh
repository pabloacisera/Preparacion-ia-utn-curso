#!/bin/bash
# 03-curl-post-json.sh
# Ejercicio: POST con datos JSON

echo "=== POST con JSON ==="
curl -X POST https://httpbin.org/post \
  -H "Content-Type: application/json" \
  -d '{"nombre": "estudiante", "tema": "apis", "activo": true}'
echo -e "\n\n"
